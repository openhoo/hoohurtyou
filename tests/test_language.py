import os
import platform
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from hoo.hooooo import hooooooooooooooooooooooooooooooooooooooooooooooooo, hoooooooooooooooooooooo, hooooooooooooooooooooooo
from hoo.hoooooo import hoooo, hooo
from hoo.hooooooo import *

E=hoooooooooo
ROOT=Path(__file__).resolve().parents[1]

class FrontendTests(unittest.TestCase):
    def test_source_alphabet(self):
        for path in (ROOT/'examples').glob('*.hoo'):
            self.assertRegex(path.read_text(),r'\A(?:hoo+\s*)+\Z')
            hooo(path.read_text())
    def test_positions(self):
        self.assertEqual((hoooooooooooooooooooooo('hoo\n  hooo')[1].line,hoooooooooooooooooooooo('hoo\n  hooo')[1].column),(2,3))
    def test_forbidden_characters(self):
        for s in ['hello','hoo!','hoo # hi','ho','hOo','hoohoo','hoo\u00a0hoo','hoo 42']:
            with self.subTest(s=s),self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo): hoooooooooooooooooooooo(s)
    def test_word_limit(self):
        with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo): hoooooooooooooooooooooo('h'+'o'*4096)
    def hoooooooooooooooooooooooooooooooooooooooooo(self,source,match):
        with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,match): hooo(source)
    def test_unknown_symbol(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',hooooooooooo(0)),'unknown variable')
    def test_type_mismatch(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooo(0,'number',hooooooooo('oops')),'expected number')
    def test_assignment_type(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooo(0,'number',hoooooooo(1)),hooooooooooooooo(0,hooooooooo('oops'))),'expected number')
    def test_unknown_assignment(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooo(0,hoooooooo(1)),'unknown variable')
    def test_duplicate_variable(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooo(0,'number',hoooooooo(1)),hoooooooooooooo(0,'number',hoooooooo(2))),'duplicate global')
    def test_duplicate_function(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooooo(0,'void',[],''),hoooooooooooooooo(0,'void',[],'')),'duplicate function')
    def test_duplicate_parameter(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'void',[(0,'number'),(0,'number')],''),'duplicate parameter')
    def test_forward_function(self): hooo(hooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hooooooooooooooooo(hooooooooooooo(1))),hoooooooooooooooo(1,'number',[],hooooooooooooooooo(hoooooooo(1))),E('print',hooooooooooooo(0))))
    def test_missing_return(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],E('print',hoooooooo(1))),'without returning')
    def test_partial_return(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hoooooooooooooooooo(hoooooo('true'),hooooooooooooooooo(hoooooooo(1)))),'without returning')
    def test_wrong_return(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hooooooooooooooooo(hooooooooo('x'))),'expected number')
    def test_void_return(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'void',[],hooooooooooooooooo(hoooooooo(1))),'cannot return')
    def test_top_return(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooo(),'only valid in functions')
    def test_unreachable(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hooooooooooooooooooooo(hooooooooooooooooo(hoooooooo(1)),E('print',hoooooooo(2)))),'unreachable')
    def test_arity(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooooo(0,'void',[(0,'number')],''),E('do',hooooooooooooo(0))),'argument count')
    def test_unknown_function(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('do',hooooooooooooo(0)),'unknown function')
    def test_bad_handler(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hooooooooooooooooo(hoooooooo(1))),E('do',hoooooooooooo(0))),'callback requires')
    def test_parameter_handler(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooooo(0,'void',[(0,'number')],''),E('do',hoooooooooooo(0))),'callback requires')
    def test_if_condition(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooo(hoooooooo(1),''),'expected boolean')
    def test_outside_break(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooo('break'),'only valid in loops')
    def test_outside_continue(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hoooooo('continue'),'only valid in loops')
    def test_scope_leak(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooooooo(hoooooo('true'),hoooooooooooooo(0,'number',hoooooooo(1))),E('print',hooooooooooo(0))),'unknown variable')
    def test_late_global(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(E('print',hoooooooo(1)),hoooooooooooooo(0,'number',hoooooooo(0))),'must precede')
    def test_heterogeneous_array(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('do',hoooooooooooooooooooo(hoooooooo(1),hooooooooo('x'))),'expected number')
    def test_scalar_equality(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('do',E('equal',hoooooooo(1),hooooooooo('1'))),'matching scalar')
    def test_unterminated_block(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('if',hoooooo('true'),hoooooo('body')),'unterminated')
    def test_bad_digit(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('integer',hoooooo('true'),hoooooo('end'))),'hexadecimal')
    def test_invalid_utf8(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('string',hooooo(79),hooooo(79),hoooooo('end'))),'UTF-8')
    def test_odd_string(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('string',hooooo(65),hoooooo('end'))),'pairs')
    def test_nul_string(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('string',hooooo(64),hooooo(64),hoooooo('end'))),'NUL')
    def test_huge_integer(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('integer',*[hooooo(79)]*16,hoooooo('end'))),'64-bit')
    def test_empty_integer(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',E('integer',hoooooo('end'))),'1..16')
    def test_reserved_word(self): self.hoooooooooooooooooooooooooooooooooooooooooo(hooooo(63),'statement')
    def test_expression_depth(self): self.hoooooooooooooooooooooooooooooooooooooooooo(E('print',(hoooooo('negate')+' ')*201+hoooooooo(1)),'nesting')

class NativeTests(unittest.TestCase):
    def hooooooooooooooooooooooooooooooooooooooooooo(self,source,args=(),headless=True):
        with tempfile.TemporaryDirectory() as tmp:
            binary=hoooo(source,Path(tmp)/'test',headless=headless,sanitize=os.getenv('HOO_SANITIZE')=='1')
            env=dict(os.environ)
            if not headless:
                # GTK/AppKit keep toolkit-owned process caches. Still check UAF/UB.
                env['ASAN_OPTIONS']='detect_leaks=0'
            result=subprocess.run([str(binary),*args],capture_output=True,text=True,timeout=20,env=env)
            self.assertNotIn('AddressSanitizer',result.stderr)
            self.assertNotIn('UndefinedBehaviorSanitizer',result.stderr)
            return result
    def hoooooooooooooooooooooooooooooooooooooooooooo(self,source,expected,args=()):
        r=self.hooooooooooooooooooooooooooooooooooooooooooo(source,args); self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,expected)
    def hooooooooooooooooooooooooooooooooooooooooooooo(self,source,message):
        r=self.hooooooooooooooooooooooooooooooooooooooooooo(source); self.assertEqual(r.returncode,70,r.stderr); self.assertIn(message,r.stderr)
    def test_hello(self): self.hoooooooooooooooooooooooooooooooooooooooooooo((ROOT/'examples/hello.hoo').read_text(),'Hoo, world! 🦉\n')
    def test_factorial(self): self.hoooooooooooooooooooooooooooooooooooooooooooo((ROOT/'examples/factorial.hoo').read_text(),'3628800\n')
    def test_lists(self): self.hoooooooooooooooooooooooooooooooooooooooooooo((ROOT/'examples/lists.hoo').read_text(),'2\n3\n5\n7\n')
    def test_arithmetic(self):
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(*[E('print',E(op,hoooooooo(a),hoooooooo(b))) for op,a,b in [('add',2,3),('subtract',2,3),('multiply',4,5),('divide',9,2),('remainder',9,2)]]),'5\n-1\n20\n4\n1\n')
    def test_overflow(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('add',hoooooooo(9223372036854775807),hoooooooo(1))),'overflow')
    def test_divide_zero(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('divide',hoooooooo(1),hoooooooo(0))),'division by zero')
    def test_multiply_overflow(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('multiply',hoooooooo(9223372036854775807),hoooooooo(2))),'overflow')
    def test_negation_overflow(self):
        minimum=E('subtract',hoooooooo(-9223372036854775807),hoooooooo(1))
        self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('negate',minimum)),'negation overflow')
    def test_division_overflow(self):
        minimum=E('subtract',hoooooooo(-9223372036854775807),hoooooooo(1))
        self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('divide',minimum,hoooooooo(-1))),'division overflow')
    def test_bounds(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('get',hoooooooooooooooooooo(hoooooooo(1)),hoooooooo(1))),'out of bounds')
    def test_negative_bounds(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('get',hoooooooooooooooooooo(hoooooooo(1)),hoooooooo(-1))),'out of bounds')
    def test_array_mutation(self): self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooo(0,'list',hoooooooooooooooooooo()),E('do',E('push',hooooooooooo(0),hoooooooo(9))),E('do',E('put',hooooooooooo(0),hoooooooo(0),hoooooooo(7))),E('print',E('get',hooooooooooo(0),hoooooooo(0)))),'7\n')
    def test_unicode_length(self): self.hoooooooooooooooooooooooooooooooooooooooooooo(E('print',E('length',hooooooooo('Hoo 🦉'))),'5\n')
    def test_short_circuit(self):
        bad=E('equal',E('divide',hoooooooo(1),hoooooooo(0)),hoooooooo(1))
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(E('print',E('and',hoooooo('false'),bad)),E('print',E('or',hoooooo('true'),bad))),'false\ntrue\n')
    def test_order_of_evaluation(self):
        fn=hoooooooooooooooo(0,'number',[(0,'number')],hooooooooooooooooooooo(E('print',hooooooooooo(0)),hooooooooooooooooo(hooooooooooo(0))))
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(fn,E('print',E('add',hooooooooooooo(0,hoooooooo(1)),hooooooooooooo(0,hoooooooo(2))))),'1\n2\n3\n')
    def test_recursion_with_allocations(self):
        fn=hoooooooooooooooo(0,'text',[(0,'number')],hoooooooooooooooooo(E('less',hooooooooooo(0),hoooooooo(1)),hooooooooooooooooo(hooooooooo('')),hooooooooooooooooo(E('concat',hooooooooo('h'),hooooooooooooo(0,E('subtract',hooooooooooo(0),hoooooooo(1)))))))
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(fn,E('print',E('length',hooooooooooooo(0,hoooooooo(1000))))),'1000\n')
    def test_gc_roots_and_loop_control(self):
        fn=hoooooooooooooooo(0,'text',[],hooooooooooooooooooooo(hoooooooooooooo(3,'number',hoooooooo(0)),hoooooooooooooo(4,'text',hooooooooo('')),hooooooooooooooooooo(E('less',hooooooooooo(3),hoooooooo(1000)),hooooooooooooooooooooo(hooooooooooooooo(4,E('concat',hooooooooooo(4),hooooooooo('o'))),hooooooooooooooo(3,E('add',hooooooooooo(3),hoooooooo(1))))),hooooooooooooooooo(hooooooooooo(4))))
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(fn,hoooooooooooooo(0,'number',hoooooooo(0)),hoooooooooooooo(1,'text',hooooooooo('prefix')),hooooooooooooooooooo(E('less',hooooooooooo(0),hoooooooo(1000)),hooooooooooooooooooooo(hooooooooooooooo(0,E('add',hooooooooooo(0),hoooooooo(1))),hoooooooooooooooooo(E('less',hooooooooooo(0),hoooooooo(500)),hoooooo('continue')),hoooooooooooooooooo(E('equal',hooooooooooo(0),hoooooooo(600)),hoooooo('break')))),E('print',hooooooooooo(0)),E('print',E('length',E('concat',hooooooooooo(1),hooooooooooooo(0))))),'600\n1006\n')
    def test_loop_scope_gc(self):
        self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(hoooooooooooooo(0,'number',hoooooooo(0)),hooooooooooooooooooo(E('less',hooooooooooo(0),hoooooooo(2000)),hooooooooooooooooooooo(hoooooooooooooo(1,'text',hooooooooo('temporary')),E('do',E('concat',hooooooooooo(1),hooooooooo(' discarded'))),hooooooooooooooo(0,E('add',hooooooooooo(0),hoooooooo(1))))),E('print',hooooooooooo(0))),'2000\n')
    def test_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=hooooooooo(str(Path(tmp)/'note.txt'))
            self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(E('do',E('write',path,hooooooooo('A note 🦉\n'))),E('print',E('read',path)),E('print',E('exists',path))),'A note 🦉\n\ntrue\n')
    def test_bad_file_utf8(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'bad'; path.write_bytes(b'\xff')
            self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('read',hooooooooo(str(path)))),'UTF-8')
    def test_missing_file(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('read',hooooooooo('/hoo/no/such/file'))),'cannot open')
    def test_home_directory(self): self.hoooooooooooooooooooooooooooooooooooooooooooo(E('print',E('home')),os.environ['HOME']+'\n')
    def test_early_global_reference(self):
        fn=hoooooooooooooooo(0,'text',[],hooooooooooooooooo(hooooooooooo(1)))
        self.hooooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(fn,hoooooooooooooo(0,'text',hooooooooooooo(0)),hoooooooooooooo(1,'text',hooooooooo('too late'))),'before initialization')
    def test_arguments(self): self.hoooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooo(E('print',E('argument_count')),E('print',E('argument',hoooooooo(1)))),'2\nsecond\n',('first','second'))
    def test_parse_number(self): self.hoooooooooooooooooooooooooooooooooooooooooooo(E('print',E('parse_number',hooooooooo('-123'))),'-123\n')
    def test_bad_number(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('print',E('parse_number',hooooooooo('12oops'))),'invalid decimal')
    def test_headless_gui_rejection(self): self.hooooooooooooooooooooooooooooooooooooooooooooo(E('do',E('window',hooooooooo('Hoo'),hoooooooo(400),hoooooooo(200))),'requires a GUI build')
    @unittest.skipUnless(os.getenv('HOO_GUI_TEST')=='1','requires a desktop session')
    def test_desktop_controls(self):
        r=self.hooooooooooooooooooooooooooooooooooooooooooo((ROOT/'examples/desktop-smoke.hoo').read_text(),headless=False)
        self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,'1\nMultiline 🦉\nSecond line\n')

if __name__=='__main__': unittest.main()
