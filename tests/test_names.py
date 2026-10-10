import ast
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from hoo.hoooooo import hooo
from hoo.hooooooo import hoooooooooo,hoooooooo,hooooooooooooooooooooo,hoooooooooooooooo,hooooooooooooooooo,hooooooooooooo

ROOT=Path(__file__).resolve().parents[1]
class NamingTests(unittest.TestCase):
    def test_custom_python_definitions_are_hoo(self):
        for path in [*ROOT.joinpath('hoo').glob('*.py'),ROOT/'tools/generate_examples.py']:
            tree=ast.parse(path.read_text())
            for n in ast.walk(tree):
                if isinstance(n,(ast.FunctionDef,ast.ClassDef)):
                    with self.subTest(file=path.name,symbol=n.name):
                        if n.name=='__init__': continue
                        self.assertRegex(n.name,r'\Ahoo+\Z')
    def test_native_abi_is_hoo(self):
        source=(ROOT/'hoo/runtime/hoo.h').read_text()
        names=re.findall(r'^.*?\b(\w+)\([^;{}]*\);',source,re.M)
        self.assertGreater(len(names),40)
        for name in names: self.assertRegex(name,r'\Ahoo+\Z')
    def test_gtk_cleanup_callback_reference_is_hoo(self):
        source=(ROOT/'hoo/runtime/hooo.c').read_text()
        cleanup=re.findall(r'g_signal_connect_data\([^;]+,(\w+),0\)',source)
        self.assertEqual(len(cleanup),1)
        self.assertRegex(cleanup[0],r'\Ahoo+\Z')
        self.assertRegex(source,r'static void '+cleanup[0]+r'\(')
    def test_generated_symbols_are_hoo_and_deterministic(self):
        source=hooooooooooooooooooooo(hoooooooooooooooo(0,'number',[],hooooooooooooooooo(hoooooooo(42))),hoooooooooo('print',hooooooooooooo(0)))
        generated=hooo(source)
        self.assertEqual(generated,hooo(source))
        definitions=re.findall(r'^static \w+ (\w+)\(',generated,re.M)
        self.assertEqual(len(definitions),2)  # prototype and function body
        for name in definitions: self.assertRegex(name,r'\Ahoo+\Z')
        self.assertNotRegex(generated,r'\b(?:ho_[a-z_]+|[fvt]\d+|(?:scope|statement|function|iteration|short)\d+)\b')
        self.assertRegex(generated,r'int main\(int hoo+, char \*\*hoo+\)')
    def test_hoo_cli_spelling_runs_native_program(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'hoo.hoo'; path.write_text(hoooooooooo('print',hoooooooo(42)))
            r=subprocess.run([sys.executable,str(ROOT/'bin/hoo'),'hooooooo',str(path),'--hoooo'],capture_output=True,text=True,timeout=30)
            self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,'42\n')
    def test_hoo_cli_spellings_reject_english_aliases(self):
        path=ROOT/'examples/hello.hoo'
        for alias,name in [('hoo','check'),('hooo','emit'),('hoooo','tokens'),('hooooo','format')]:
            with self.subTest(alias=alias):
                a=subprocess.run([sys.executable,str(ROOT/'bin/hoo'),alias,str(path)],capture_output=True,text=True)
                b=subprocess.run([sys.executable,str(ROOT/'bin/hoo'),name,str(path)],capture_output=True,text=True)
                self.assertEqual(a.returncode,0,a.stderr); self.assertEqual(b.returncode,2,b.stderr)
if __name__=='__main__': unittest.main()
