import platform
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from hoo.hooooooo import hoooooooooo,hoooooooo,hooooooooooooooooooooo
from hoo.hoooooo import hoooo
from hoo.hooooo import hooooooooooooooooooooooooooooooooooooooooooooooooo

ROOT=Path(__file__).resolve().parents[1]
class CLITests(unittest.TestCase):
    def hooooooooooooooooooooooooooooooooooooooooo(self,*args): return subprocess.run([sys.executable,str(ROOT/'bin/hoo'),*map(str,args)],capture_output=True,text=True,timeout=30)
    def test_error_position(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'bad.hoo'; source.write_text('hoo!')
            r=self.hooooooooooooooooooooooooooooooooooooooooo('hoo',source); self.assertEqual(r.returncode,1); self.assertIn(str(source)+': 1:1:',r.stderr)
    def test_run_arguments(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'args.hoo'; source.write_text(hooooooooooooooooooooo(hoooooooooo('print',hoooooooooo('argument',hoooooooo(0)))))
            r=self.hooooooooooooooooooooooooooooooooooooooooo('hooooooo',source,'--hoooo','--','hoo argument'); self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,'hoo argument\n')
    def test_source_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'safe.hoo'; original=hoooooooooo('print',hoooooooo(1)); source.write_text(original)
            for command in ('hoooooo','hooo'):
                r=self.hooooooooooooooooooooooooooooooooooooooooo(command,source,'--hoooooo',source); self.assertEqual(r.returncode,1); self.assertIn('overwrite',r.stderr); self.assertEqual(source.read_text(),original)
    def test_failed_build_preserves_previous_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'keep'; output.write_text('previous output')
            with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo): hoooo('oops',output,headless=True)
            self.assertEqual(output.read_text(),'previous output')
    def test_formatter_preserves_program(self):
        source=ROOT/'examples/hello.hoo'
        r=self.hooooooooooooooooooooooooooooooooooooooooo('hooooo',source); self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(r.stdout.split(),source.read_text().split())
    def test_help_version_and_option_names(self):
        for command in [[], *[[word] for word in ('hoo','hooo','hoooo','hooooo','hoooooo','hooooooo')]]:
            result=self.hooooooooooooooooooooooooooooooooooooooooo(*command,'--hoo')
            self.assertEqual(result.returncode,0,result.stderr)
            flags=re.findall(r'(?<![\w-])(--?[a-z]+)',result.stdout)
            self.assertTrue(flags)
            for flag in flags: self.assertRegex(flag,r'^--hoo+$')
            self.assertTrue(result.stdout.startswith('usage: hoo '))
        result=self.hooooooooooooooooooooooooooooooooooooooooo('--hooo')
        self.assertEqual(result.returncode,0,result.stderr)
        from hoo import __version__
        self.assertEqual(result.stdout.strip(),f'Hoo {__version__}')

    def test_english_and_short_flags_rejected(self):
        source=ROOT/'examples/hello.hoo'
        for flag in ('--help','-h','--version','--headless','--sanitize','--output','-o','--app','--ho'):
            with self.subTest(flag=flag):
                result=self.hooooooooooooooooooooooooooooooooooooooooo('hooo',source,flag)
                self.assertEqual(result.returncode,2,result.stderr)
        for flag in ('--help','-h','--version'):
            result=self.hooooooooooooooooooooooooooooooooooooooooo(flag)
            self.assertEqual(result.returncode,2,result.stderr)
        with tempfile.TemporaryDirectory() as tmp:
            for flag in ('--headless','--sanitize','--output','-o','--app'):
                result=self.hooooooooooooooooooooooooooooooooooooooooo('hoooooo',source,'--hoooooo',Path(tmp)/'hoo',flag)
                self.assertEqual(result.returncode,2,result.stderr)
        result=self.hooooooooooooooooooooooooooooooooooooooooo('hoooooo',source,'--hoooo')
        self.assertEqual(result.returncode,2)
        self.assertIn('--hoooooo',result.stderr)

    def test_emission_and_sanitized_native_build(self):
        source=ROOT/'examples/hello.hoo'
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'hoo.c'
            result=self.hooooooooooooooooooooooooooooooooooooooooo('hooo',source,'--hoooooo',output)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('int main(',output.read_text())
            executable=Path(tmp)/'hoo'
            result=self.hooooooooooooooooooooooooooooooooooooooooo('hoooooo',source,'--hoooo','--hooooo','--hoooooo',executable)
            self.assertEqual(result.returncode,0,result.stderr)
            result=subprocess.run([str(executable)],capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('Hoo',result.stdout)

    def test_app_flag_builds_or_explains_platform_requirement(self):
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'Hoo.app'
            result=self.hooooooooooooooooooooooooooooooooooooooooo('hoooooo',ROOT/'examples/counter.hoo','--hoooooo',output,'--hooooooo')
            if platform.system()=='Darwin':
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertTrue((output/'Contents/MacOS/hoo-program').is_file())
            else:
                self.assertEqual(result.returncode,1)
                self.assertIn('--hooooooo requires a macOS',result.stderr)

    def test_launcher_works_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=subprocess.run([str(ROOT/'bin/hoo'),'hoo',str(ROOT/'examples/hello.hoo')],cwd=tmp,capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)

if __name__=='__main__': unittest.main()
