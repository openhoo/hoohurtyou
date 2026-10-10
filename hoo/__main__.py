import argparse
import subprocess
import sys
import tempfile
from pathlib import Path
from . import __version__
from .hoooooo import hoooo, hooo
from .hooooo import hooooooooooooooooooooooooooooooooooooooooooooooooo, WORDS, hoooooooooooooooooooooo

HOO = {'h'+'o'*(2+i):name for i,name in enumerate(('check','emit','tokens','format','build','run'))}

def hoo():
    p=argparse.ArgumentParser(prog='hooc',description='Compile Hoo. Every word is hoo. Every mistake is yours.')
    p.add_argument('--version',action='version',version=f'Hoo {__version__}')
    sub=p.add_subparsers(dest='command',required=True)
    for alias,name in HOO.items():
        s=sub.add_parser(name,aliases=[alias]); s.add_argument('source',type=Path)
        if name in ('build','run'):
            s.add_argument('--headless',action='store_true',help='console-only runtime; no GUI dependencies')
            s.add_argument('--sanitize',action='store_true',help='AddressSanitizer and UndefinedBehaviorSanitizer')
        if name=='build':
            s.add_argument('-o','--output',required=True,type=Path)
            s.add_argument('--app',action='store_true',help='create a macOS .app bundle')
        if name=='emit': s.add_argument('-o','--output',type=Path)
        if name=='run': s.add_argument('args',nargs='*',help='program arguments (after --)')
    options=p.parse_args()
    options.command=HOO.get(options.command,options.command)
    try:
        source=options.source.read_text(encoding='utf-8')
        if getattr(options,'output',None) and options.source.resolve()==options.output.resolve():
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('output must not overwrite the source file')
        if options.command=='check': hooo(source); print(f'{options.source}: Hoo is well typed. Somehow.')
        elif options.command=='tokens':
            for t in hoooooooooooooooooooooo(source)[:-1]:
                meaning=WORDS.get(t.code, f'digit {t.code-64:X}' if 64<=t.code<=79 else f'identifier {t.code-128}' if t.code>=128 else 'reserved')
                print(f'{t.line}:{t.column}\t{t.code} o\t{meaning}')
        elif options.command=='format':
            hooo(source)
            print('\n'.join('h'+'o'*t.code for t in hoooooooooooooooooooooo(source)[:-1]))
        elif options.command=='emit':
            code=hooo(source)
            if options.output: options.output.write_text(code)
            else: print(code,end='')
        elif options.command=='build':
            result=hoooo(source,options.output,options.headless,options.app,options.sanitize)
            print(f'Compiled: {result}')
        elif options.command=='run':
            with tempfile.TemporaryDirectory(prefix='hoo-run-') as tmp:
                executable=hoooo(source,Path(tmp)/'program',options.headless,sanitize=options.sanitize)
                return subprocess.run([str(executable),*options.args]).returncode
    except (hooooooooooooooooooooooooooooooooooooooooooooooooo,OSError,UnicodeError) as e:
        print(f'{options.source}: {e}',file=sys.stderr); return 1
    return 0

if __name__=='__main__': sys.exit(hoo())
