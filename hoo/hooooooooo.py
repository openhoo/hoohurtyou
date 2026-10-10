"""Compile-time Hoo imports: deterministic dependencies in a shared namespace."""
import re
from pathlib import Path
from .hooooo import (
    hooooooooooooooooooooooo,
    hooooooooooooooooooooooooooooooooooooooooooooooooo,
    hoooooooooooooooooooooooooooooooooooooooooooooooooooo,
)

def hoo(source, path=None, output=None):
    origin = Path(path).resolve() if path is not None else None
    base = origin.parent if origin else None
    active, visited, functions, body = [], set(), [], []

    def hooo(text, file, token=None):
        if file in active:
            chain = ' -> '.join(str(p) for p in [*active, file])
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('import cycle: '+chain,token)
        if file in visited:
            return
        if len(active) >= 64:
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('import depth exceeds 64 modules',token)
        if len(visited) + len(active) >= 256:
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('import graph exceeds 256 modules',token)
        active.append(file)
        program = hooooooooooooooooooooooo(text,str(file) if file else None)
        for dependency in program.imports:
            name = dependency.args[0]
            parts = name.split('/')
            if (not parts or not re.fullmatch(r'hoo+\.hoo',parts[-1])
                    or any(not re.fullmatch(r'hoo+',p) for p in parts[:-1])):
                raise hooooooooooooooooooooooooooooooooooooooooooooooooo('import path must contain Hoo-only directory names and a Hoo-only .hoo filename',dependency.token)
            if file is None:
                raise hooooooooooooooooooooooooooooooooooooooooooooooooo('imports require the source file path',dependency.token)
            target = (file.parent / name).resolve()
            if not target.is_relative_to(base):
                raise hooooooooooooooooooooooooooooooooooooooooooooooooo('import resolves outside the entry source directory',dependency.token)
            if target in active:
                hooo('',target,dependency.token)
            if target not in visited:
                try:
                    contents = target.read_text(encoding='utf-8')
                except (OSError,UnicodeError) as error:
                    raise hooooooooooooooooooooooooooooooooooooooooooooooooo(f'cannot read import {name!r}: {error}',dependency.token) from None
                hooo(contents,target,dependency.token)
        if file != origin:
            for statement in program.body:
                if statement.op != 'let':
                    raise hooooooooooooooooooooooooooooooooooooooooooooooooo('imported modules may contain functions and global declarations only',statement.token)
        functions.extend(program.functions)
        body.extend(program.body)
        active.pop()
        visited.add(file)

    hooo(source,origin)
    if output is not None and Path(output).resolve() in visited:
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('output must not overwrite a source file in the import graph')
    return hoooooooooooooooooooooooooooooooooooooooooooooooooooo(functions,body)
