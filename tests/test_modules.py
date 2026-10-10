import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from hoo.hoooooo import hooo, hoooo
from hoo.hooooo import hooooooooooooooooooooooooooooooooooooooooooooooooo
from hoo.hooooooo import *

ROOT=Path(__file__).resolve().parents[1]
E=hoooooooooo

class ModuleTests(unittest.TestCase):
    def hoooooooooooooooooooooooooooooooooooooooooooooo(self,source,path,args=(),headless=True):
        with tempfile.TemporaryDirectory() as tmp:
            binary=hoooo(source,Path(tmp)/'hoo',headless=headless,sanitize=os.getenv('HOO_SANITIZE')=='1',hoo=path)
            env=dict(os.environ)
            if not headless: env['ASAN_OPTIONS']='detect_leaks=0'
            result=subprocess.run([str(binary),*args],capture_output=True,text=True,timeout=20,env=env)
            self.assertNotIn('AddressSanitizer',result.stderr)
            self.assertNotIn('UndefinedBehaviorSanitizer',result.stderr)
            return result

    def test_nested_diamond_initialization_and_forward_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); entry=root/'hoo.hoo'
            (root/'hoooo.hoo').write_text(hoooooooooooooo(0,'number',hoooooooo(40)))
            (root/'hooo.hoo').write_text(hooooooooooooooooooooo(E('import',hooooooooo('hoooo.hoo')),hoooooooooooooooo(0,'number',[],hooooooooooooooooo(E('add',hooooooooooo(0),hoooooooo(2))))))
            source=hooooooooooooooooooooo(E('import',hooooooooo('hoooo.hoo')),E('import',hooooooooo('hooo.hoo')),E('import',hooooooooo('hooo.hoo')),E('print',hooooooooooooo(0)))
            entry.write_text(source)
            a=hooo(source,entry); self.assertEqual(a,hooo(source,entry))
            result=self.hoooooooooooooooooooooooooooooooooooooooooooooo(source,entry)
            self.assertEqual(result.returncode,0,result.stderr); self.assertEqual(result.stdout,'42\n')

    def test_cycles_report_import_site(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); entry=root/'hoo.hoo'
            source=E('import',hooooooooo('hooo.hoo')); entry.write_text(source)
            other=root/'hooo.hoo'; other.write_text(E('import',hooooooooo('hoo.hoo')))
            with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo) as error: hooo(source,entry)
            self.assertIn('import cycle',str(error.exception))
            self.assertTrue(str(error.exception).startswith(str(other.resolve())+':1:1:'))

    def test_imports_need_literal_and_precede_other_declarations(self):
        for source in [E('import',hoooooooo(0)),hooooooooooooooooooooo(E('print',hoooooooo(1)),E('import',hooooooooo('hoo.hoo')))]:
            with self.subTest(source=source[:100]):
                with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo): hooo(source)

    def test_imports_require_source_origin(self):
        with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'source file path'): hooo(E('import',hooooooooo('hoo.hoo')))

    def test_paths_require_hoo_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            for path in ['','../hoo.hoo','/hoo.hoo','hello.hoo','hoo.txt','hoo/../hoo.hoo','hoo\\hooo.hoo']:
                with self.subTest(path=path):
                    with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'Hoo-only'): hooo(E('import',hooooooooo(path)),Path(tmp)/'hoo.hoo')

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as other:
            target=Path(other)/'hoo.hoo'; target.write_text('')
            (Path(tmp)/'hooo.hoo').symlink_to(target)
            with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'outside'): hooo(E('import',hooooooooo('hooo.hoo')),Path(tmp)/'hoo.hoo')

    def test_missing_and_invalid_utf8_imports_report_import_site(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=E('import',hooooooooo('hooo.hoo'))
            for contents in [None,b'\xff']:
                if contents: (root/'hooo.hoo').write_bytes(contents)
                with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'cannot read import') as error: hooo(source,root/'hoo.hoo')
                self.assertTrue(str(error.exception).startswith(str((root/'hoo.hoo').resolve())+':1:1:'))

    def test_imported_lexer_and_type_errors_name_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=E('import',hooooooooo('hooo.hoo')); dependency=root/'hooo.hoo'
            for contents in ['hoo!',hoooooooooooooo(0,'number',hooooooooo('wrong type'))]:
                dependency.write_text(contents)
                with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo) as error: hooo(source,root/'hoo.hoo')
                self.assertTrue(str(error.exception).startswith(str(dependency.resolve())+':1:'))

    def test_imports_reject_top_level_effects_and_duplicate_definitions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=E('import',hooooooooo('hooo.hoo'))
            (root/'hooo.hoo').write_text(E('print',hoooooooo(1)))
            with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'global declarations only'): hooo(source,root/'hoo.hoo')
            declaration=hoooooooooooooooo(0,'void',[],'')
            (root/'hooo.hoo').write_text(declaration)
            with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'duplicate function'): hooo(hooooooooooooooooooooo(source,declaration),root/'hoo.hoo')

    def test_runtime_error_reports_dependency_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); other=root/'hooo.hoo'
            other.write_text(hoooooooooooooooo(0,'number',[],hooooooooooooooooo(E('divide',hoooooooo(1),hoooooooo(0)))))
            source=hooooooooooooooooooooo(E('import',hooooooooo('hooo.hoo')),E('print',hooooooooooooo(0)))
            result=self.hoooooooooooooooooooooooooooooooooooooooooooooo(source,root/'hoo.hoo')
            self.assertEqual(result.returncode,70)
            self.assertIn(str(other.resolve())+':2:10:',result.stderr)
            self.assertIn('division by zero',result.stderr)

    def test_output_cannot_overwrite_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); other=root/'hooo.hoo'; original=hoooooooooooooo(0,'number',hoooooooo(1)); other.write_text(original)
            source=E('import',hooooooooo('hooo.hoo')); entry=root/'hoo.hoo'; entry.write_text(source)
            for command in ['hooo','hoooooo']:
                result=subprocess.run([sys.executable,str(ROOT/'bin/hoo'),command,str(entry),'--hoooooo',str(other)],capture_output=True,text=True,timeout=20)
                self.assertEqual(result.returncode,1,result.stderr); self.assertIn('overwrite',result.stderr)
                self.assertEqual(other.read_text(),original)

    def test_depth_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); folder=root
            for index in range(65):
                folder.mkdir(exist_ok=True)
                (folder/'hoo.hoo').write_text(E('import',hooooooooo('hoo/hoo.hoo')) if index<64 else '')
                folder=folder/'hoo'
            entry=root/'hoo.hoo'
            with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'depth exceeds'): hooo(entry.read_text(),entry)

    def test_graph_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); imports=[]
            for directory in ['hoo','hooo']:
                (root/directory).mkdir()
                for index in range(128):
                    name='h'+'o'*(2+index)+'.hoo'
                    (root/directory/name).write_text('')
                    imports.append(E('import',hooooooooo(directory+'/'+name)))
            hooo(hooooooooooooooooooooo(*imports[:255]),root/'hoo.hoo')
            with self.assertRaisesRegex(hooooooooooooooooooooooooooooooooooooooooooooooooo,'graph exceeds'): hooo(hooooooooooooooooooooo(*imports),root/'hoo.hoo')

    def test_modular_console_example(self):
        path=ROOT/'examples/hoo/hooooo.hoo'
        result=self.hoooooooooooooooooooooooooooooooooooooooooooooo(path.read_text(),path)
        self.assertEqual(result.returncode,0,result.stderr); self.assertEqual(result.stdout,'42\n')

    @unittest.skipUnless(os.getenv('HOO_GUI_TEST')=='1','set HOO_GUI_TEST=1 for native desktop controls')
    def test_modular_desktop_callbacks(self):
        path=ROOT/'examples/hoo/hoooo.hoo'
        result=self.hoooooooooooooooooooooooooooooooooooooooooooooo(path.read_text(),path,headless=False)
        self.assertEqual(result.returncode,0,result.stderr); self.assertEqual(result.stdout,'1\n0\n')

if __name__=='__main__': unittest.main()
