import os
import platform
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from hoo.syntax import HooError, lex, parse
from hoo.compiler import build, compile_source
from hoo.encoding import *

E=expression
ROOT=Path(__file__).resolve().parents[1]

class FrontendTests(unittest.TestCase):
    def test_source_alphabet(self):
        for path in (ROOT/'examples').glob('*.hoo'):
            self.assertRegex(path.read_text(),r'\A(?:hoo+\s*)+\Z')
            compile_source(path.read_text())
    def test_positions(self):
        self.assertEqual((lex('hoo\n  hooo')[1].line,lex('hoo\n  hooo')[1].column),(2,3))
    def test_forbidden_characters(self):
        for s in ['hello','hoo!','hoo # hi','ho','hOo','hoohoo','hoo\u00a0hoo','hoo 42']:
            with self.subTest(s=s),self.assertRaises(HooError): lex(s)
    def test_word_limit(self):
        with self.assertRaises(HooError): lex('h'+'o'*4096)
    def reject(self,source,match):
        with self.assertRaisesRegex(HooError,match): compile_source(source)
    def test_unknown_symbol(self): self.reject(E('print',ref(0)),'unknown variable')
    def test_type_mismatch(self): self.reject(let(0,'number',text('oops')),'expected number')
    def test_assignment_type(self): self.reject(program(let(0,'number',integer(1)),set_(0,text('oops'))),'expected number')
    def test_unknown_assignment(self): self.reject(set_(0,integer(1)),'unknown variable')
    def test_duplicate_variable(self): self.reject(program(let(0,'number',integer(1)),let(0,'number',integer(2))),'duplicate global')
    def test_duplicate_function(self): self.reject(program(function(0,'void',[],''),function(0,'void',[],'')),'duplicate function')
    def test_duplicate_parameter(self): self.reject(function(0,'void',[(0,'number'),(0,'number')],''),'duplicate parameter')
    def test_forward_function(self): compile_source(program(function(0,'number',[],return_(call(1))),function(1,'number',[],return_(integer(1))),E('print',call(0))))
    def test_missing_return(self): self.reject(function(0,'number',[],E('print',integer(1))),'without returning')
    def test_partial_return(self): self.reject(function(0,'number',[],if_(token('true'),return_(integer(1)))),'without returning')
    def test_wrong_return(self): self.reject(function(0,'number',[],return_(text('x'))),'expected number')
    def test_void_return(self): self.reject(function(0,'void',[],return_(integer(1))),'cannot return')
    def test_top_return(self): self.reject(return_(),'only valid in functions')
    def test_unreachable(self): self.reject(function(0,'number',[],program(return_(integer(1)),E('print',integer(2)))),'unreachable')
    def test_arity(self): self.reject(program(function(0,'void',[(0,'number')],''),E('do',call(0))),'argument count')
    def test_unknown_function(self): self.reject(E('do',call(0)),'unknown function')
    def test_bad_handler(self): self.reject(program(function(0,'number',[],return_(integer(1))),E('do',handler(0))),'callback requires')
    def test_parameter_handler(self): self.reject(program(function(0,'void',[(0,'number')],''),E('do',handler(0))),'callback requires')
    def test_if_condition(self): self.reject(if_(integer(1),''),'expected boolean')
    def test_outside_break(self): self.reject(token('break'),'only valid in loops')
    def test_outside_continue(self): self.reject(token('continue'),'only valid in loops')
    def test_scope_leak(self): self.reject(program(if_(token('true'),let(0,'number',integer(1))),E('print',ref(0))),'unknown variable')
    def test_late_global(self): self.reject(program(E('print',integer(1)),let(0,'number',integer(0))),'must precede')
    def test_heterogeneous_array(self): self.reject(E('do',array(integer(1),text('x'))),'expected number')
    def test_scalar_equality(self): self.reject(E('do',E('equal',integer(1),text('1'))),'matching scalar')
    def test_unterminated_block(self): self.reject(E('if',token('true'),token('body')),'unterminated')
    def test_bad_digit(self): self.reject(E('print',E('integer',token('true'),token('end'))),'hexadecimal')
    def test_invalid_utf8(self): self.reject(E('print',E('string',word(79),word(79),token('end'))),'UTF-8')
    def test_odd_string(self): self.reject(E('print',E('string',word(65),token('end'))),'pairs')
    def test_nul_string(self): self.reject(E('print',E('string',word(64),word(64),token('end'))),'NUL')
    def test_huge_integer(self): self.reject(E('print',E('integer',*[word(79)]*16,token('end'))),'64-bit')
    def test_empty_integer(self): self.reject(E('print',E('integer',token('end'))),'1..16')
    def test_reserved_word(self): self.reject(word(63),'statement')
    def test_expression_depth(self): self.reject(E('print',(token('negate')+' ')*201+integer(1)),'nesting')

class NativeTests(unittest.TestCase):
    def run_hoo(self,source,args=(),headless=True):
        with tempfile.TemporaryDirectory() as tmp:
            binary=build(source,Path(tmp)/'test',headless=headless,sanitize=os.getenv('HOO_SANITIZE')=='1')
            env=dict(os.environ)
            if not headless:
                # GTK/AppKit keep toolkit-owned process caches. Still check UAF/UB.
                env['ASAN_OPTIONS']='detect_leaks=0'
            result=subprocess.run([str(binary),*args],capture_output=True,text=True,timeout=20,env=env)
            self.assertNotIn('AddressSanitizer',result.stderr)
            self.assertNotIn('UndefinedBehaviorSanitizer',result.stderr)
            return result
    def good(self,source,expected,args=()):
        r=self.run_hoo(source,args); self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,expected)
    def failure(self,source,message):
        r=self.run_hoo(source); self.assertEqual(r.returncode,70,r.stderr); self.assertIn(message,r.stderr)
    def test_hello(self): self.good((ROOT/'examples/hello.hoo').read_text(),'Hoo, world! 🦉\n')
    def test_factorial(self): self.good((ROOT/'examples/factorial.hoo').read_text(),'3628800\n')
    def test_lists(self): self.good((ROOT/'examples/lists.hoo').read_text(),'2\n3\n5\n7\n')
    def test_arithmetic(self):
        self.good(program(*[E('print',E(op,integer(a),integer(b))) for op,a,b in [('add',2,3),('subtract',2,3),('multiply',4,5),('divide',9,2),('remainder',9,2)]]),'5\n-1\n20\n4\n1\n')
    def test_overflow(self): self.failure(E('print',E('add',integer(9223372036854775807),integer(1))),'overflow')
    def test_divide_zero(self): self.failure(E('print',E('divide',integer(1),integer(0))),'division by zero')
    def test_multiply_overflow(self): self.failure(E('print',E('multiply',integer(9223372036854775807),integer(2))),'overflow')
    def test_negation_overflow(self):
        minimum=E('subtract',integer(-9223372036854775807),integer(1))
        self.failure(E('print',E('negate',minimum)),'negation overflow')
    def test_division_overflow(self):
        minimum=E('subtract',integer(-9223372036854775807),integer(1))
        self.failure(E('print',E('divide',minimum,integer(-1))),'division overflow')
    def test_bounds(self): self.failure(E('print',E('get',array(integer(1)),integer(1))),'out of bounds')
    def test_negative_bounds(self): self.failure(E('print',E('get',array(integer(1)),integer(-1))),'out of bounds')
    def test_array_mutation(self): self.good(program(let(0,'list',array()),E('do',E('push',ref(0),integer(9))),E('do',E('put',ref(0),integer(0),integer(7))),E('print',E('get',ref(0),integer(0)))),'7\n')
    def test_unicode_length(self): self.good(E('print',E('length',text('Hoo 🦉'))),'5\n')
    def test_short_circuit(self):
        bad=E('equal',E('divide',integer(1),integer(0)),integer(1))
        self.good(program(E('print',E('and',token('false'),bad)),E('print',E('or',token('true'),bad))),'false\ntrue\n')
    def test_order_of_evaluation(self):
        fn=function(0,'number',[(0,'number')],program(E('print',ref(0)),return_(ref(0))))
        self.good(program(fn,E('print',E('add',call(0,integer(1)),call(0,integer(2))))),'1\n2\n3\n')
    def test_recursion_with_allocations(self):
        fn=function(0,'text',[(0,'number')],if_(E('less',ref(0),integer(1)),return_(text('')),return_(E('concat',text('h'),call(0,E('subtract',ref(0),integer(1)))))))
        self.good(program(fn,E('print',E('length',call(0,integer(1000))))),'1000\n')
    def test_gc_roots_and_loop_control(self):
        fn=function(0,'text',[],program(let(3,'number',integer(0)),let(4,'text',text('')),while_(E('less',ref(3),integer(1000)),program(set_(4,E('concat',ref(4),text('o'))),set_(3,E('add',ref(3),integer(1))))),return_(ref(4))))
        self.good(program(fn,let(0,'number',integer(0)),let(1,'text',text('prefix')),while_(E('less',ref(0),integer(1000)),program(set_(0,E('add',ref(0),integer(1))),if_(E('less',ref(0),integer(500)),token('continue')),if_(E('equal',ref(0),integer(600)),token('break')))),E('print',ref(0)),E('print',E('length',E('concat',ref(1),call(0))))),'600\n1006\n')
    def test_loop_scope_gc(self):
        self.good(program(let(0,'number',integer(0)),while_(E('less',ref(0),integer(2000)),program(let(1,'text',text('temporary')),E('do',E('concat',ref(1),text(' discarded'))),set_(0,E('add',ref(0),integer(1))))),E('print',ref(0))),'2000\n')
    def test_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=text(str(Path(tmp)/'note.txt'))
            self.good(program(E('do',E('write',path,text('A note 🦉\n'))),E('print',E('read',path)),E('print',E('exists',path))),'A note 🦉\n\ntrue\n')
    def test_bad_file_utf8(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'bad'; path.write_bytes(b'\xff')
            self.failure(E('print',E('read',text(str(path)))),'UTF-8')
    def test_missing_file(self): self.failure(E('print',E('read',text('/hoo/no/such/file'))),'cannot open')
    def test_home_directory(self): self.good(E('print',E('home')),os.environ['HOME']+'\n')
    def test_early_global_reference(self):
        fn=function(0,'text',[],return_(ref(1)))
        self.failure(program(fn,let(0,'text',call(0)),let(1,'text',text('too late'))),'before initialization')
    def test_arguments(self): self.good(program(E('print',E('argument_count')),E('print',E('argument',integer(1)))),'2\nsecond\n',('first','second'))
    def test_parse_number(self): self.good(E('print',E('parse_number',text('-123'))),'-123\n')
    def test_bad_number(self): self.failure(E('print',E('parse_number',text('12oops'))),'invalid decimal')
    def test_headless_gui_rejection(self): self.failure(E('do',E('window',text('Hoo'),integer(400),integer(200))),'requires a GUI build')
    @unittest.skipUnless(os.getenv('HOO_GUI_TEST')=='1','requires a desktop session')
    def test_desktop_controls(self):
        r=self.run_hoo((ROOT/'examples/desktop-smoke.hoo').read_text(),headless=False)
        self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,'1\nMultiline 🦉\nSecond line\n')

if __name__=='__main__': unittest.main()
