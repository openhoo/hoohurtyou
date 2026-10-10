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
    def hooooooooooooooooooooooooooooooooooooooooo(self,*args): return subprocess.run([sys.executable,str(ROOT/'hooc'),*map(str,args)],capture_output=True,text=True,timeout=30)
    def test_error_position(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'bad.hoo'; source.write_text('hoo!')
            r=self.hooooooooooooooooooooooooooooooooooooooooo('check',source); self.assertEqual(r.returncode,1); self.assertIn(str(source)+': 1:1:',r.stderr)
    def test_run_arguments(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'args.hoo'; source.write_text(hooooooooooooooooooooo(hoooooooooo('print',hoooooooooo('argument',hoooooooo(0)))))
            r=self.hooooooooooooooooooooooooooooooooooooooooo('run',source,'--headless','--','hoo argument'); self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(r.stdout,'hoo argument\n')
    def test_source_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'safe.hoo'; original=hoooooooooo('print',hoooooooo(1)); source.write_text(original)
            for command in ('build','emit'):
                r=self.hooooooooooooooooooooooooooooooooooooooooo(command,source,'-o',source); self.assertEqual(r.returncode,1); self.assertIn('overwrite',r.stderr); self.assertEqual(source.read_text(),original)
    def test_failed_build_preserves_previous_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'keep'; output.write_text('previous output')
            with self.assertRaises(hooooooooooooooooooooooooooooooooooooooooooooooooo): hoooo('oops',output,headless=True)
            self.assertEqual(output.read_text(),'previous output')
    def test_formatter_preserves_program(self):
        source=ROOT/'examples/hello.hoo'
        r=self.hooooooooooooooooooooooooooooooooooooooooo('format',source); self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(r.stdout.split(),source.read_text().split())
if __name__=='__main__': unittest.main()
