"""Compiler driver: Hoo -> checked AST -> C -> platform machine code."""
import os
import platform
import plistlib
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path
from . import __version__
from .hooooooooo import hoo as hooooo
from .hooooo import hooooooooooooooooooooooooooooooooooooooooooooooooo
from .hooo import hoooooooooooooooooooooooooooooooooooooooooooooo
from .hoooo import hooooooooooooooooooooooooooooooooooooooooooooooo

RUNTIME = Path(__file__).resolve().parent / 'runtime'

def hooo(source, hoo=None, hoooooo=None):
    try:
        program = hooooo(source,hoo,hoooooo)
        checker = hoooooooooooooooooooooooooooooooooooooooooooooo(program).hoooooooooooooooooooooooooo()
        return hooooooooooooooooooooooooooooooooooooooooooooooo(program,checker).hoooooooooooooooooooooooooooooooooo()
    except RecursionError:
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('source nesting exceeds the compiler stack limit') from None

def hoooo(source,output,headless=False,app=False,sanitize=False,hoo=None):
    code = hooo(source,hoo,output)
    output = Path(output).resolve()
    if app and (platform.system() != 'Darwin' or headless):
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('--hooooooo requires a macOS desktop build')
    if app and (output.suffix != '.app' or output.exists()):
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('--hooooooo output must be a new .app directory')
    compiler = os.environ.get('CC','clang')
    if not shutil.which(compiler): raise hooooooooooooooooooooooooooooooooooooooooooooooooo(f'C compiler {compiler!r} is unavailable; install Clang or set CC')
    flags = ['-std=c11','-O2','-Wall','-Wextra','-Wno-unused-variable','-Wno-unused-function','-I',str(RUNTIME)]
    if sanitize: flags += ['-fsanitize=address,undefined','-fno-omit-frame-pointer','-g']
    native = []
    if headless: native = [str(RUNTIME/'hoooo.c')]
    elif platform.system() == 'Darwin':
        native = [str(RUNTIME/'hoo.m'),'-fobjc-arc','-framework','Cocoa']
    elif platform.system() == 'Linux':
        if not shutil.which('pkg-config'): raise hooooooooooooooooooooooooooooooooooooooooooooooooo('desktop builds need pkg-config and GTK 3 development headers')
        result = subprocess.run(['pkg-config','--cflags','--libs','gtk+-3.0'],capture_output=True,text=True)
        if result.returncode: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('desktop builds need GTK 3 development headers (libgtk-3-dev)')
        native = [str(RUNTIME/'hooo.c'),*shlex.split(result.stdout)]
    else: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('desktop backend is supported on macOS and Linux; use --hoooo for console programs')
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.hoo-build-',dir=output.parent) as tmp:
        tmp = Path(tmp); generated = tmp/'program.c'; generated.write_text(code)
        executable = tmp/'program'
        command = [compiler,*flags,str(generated),str(RUNTIME/'hoo.c'),*native,'-o',str(executable)]
        result = subprocess.run(command,capture_output=True,text=True)
        if result.returncode: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('native compilation failed:\n'+result.stderr)
        if app:
            bundle = tmp/output.name; macos = bundle/'Contents'/'MacOS'; macos.mkdir(parents=True)
            shutil.copy2(executable,macos/'hoo-program')
            info = {'CFBundleExecutable':'hoo-program','CFBundleName':output.stem,'CFBundleIdentifier':'dev.openhoo.hoo.'+''.join(c.lower() if c.isalnum() else '-' for c in output.stem),
                    'CFBundlePackageType':'APPL','CFBundleVersion':'1','CFBundleShortVersionString':__version__,'NSHighResolutionCapable':True,'NSPrincipalClass':'NSApplication'}
            with (bundle/'Contents'/'Info.plist').open('wb') as f: plistlib.dump(info,f)
            bundle.rename(output)
        else: os.replace(executable,output)
    return output
