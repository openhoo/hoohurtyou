"""Lower the checked syntax tree to native C with explicit GC root lifetimes."""
from .hoo import HOO

class hooooooooooooooooooooooooooooooooooooooooooooooo:
    def __init__(self,program,checker):
        self.program,self.checker = program,checker
        self.lines=[]; self.serial=0; self.indent=0; self.function_frame=None; self.loop_frames=[]; self.symbols={}
    def hoooooooooooooooooooooooooooooo(self,s): self.lines.append('    '*self.indent+s)
    def hooooooooooooooooooooooooooooooo(self,prefix='t'):
        self.serial+=1; return 'h'+'o'*(128+self.serial)
    def hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(self,identity):
        key=('variable',identity)
        if key not in self.symbols: self.symbols[key]=self.hooooooooooooooooooooooooooooooo()
        return self.symbols[key]
    def hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(self,identity):
        key=('function_symbol',identity)
        if key not in self.symbols: self.symbols[key]=self.hooooooooooooooooooooooooooooooo()
        return self.symbols[key]
    def hoooooooooooooooooooooooooooooooo(self,code):
        name=self.hooooooooooooooooooooooooooooooo(); self.hoooooooooooooooooooooooooooooo(f'hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {name} = {code};'); self.hoooooooooooooooooooooooooooooo(f'hoooooooo(&{name});'); return name
    def hoooooooooooooooooooooooooooo(self,n):
        op=n.op
        self.hoooooooooooooooooooooooooooooo(f'hooooo({n.token.line}, {n.token.column});')
        if op=='integer': return self.hoooooooooooooooooooooooooooooooo(f'hoooooooooooooo(INT64_C({n.args[0]}))')
        if op=='string':
            # ASCII-only octal escapes keep every UTF-8 byte unambiguous to C.
            literal='"'+''.join(f'\\{b:03o}' for b in n.args[0].encode())+'"'
            return self.hoooooooooooooooooooooooooooooooo(f'hooooooooooooooooo({literal})')
        if op in ('true','false'): return self.hoooooooooooooooooooooooooooooooo(f'hooooooooooooooo({1 if op=="true" else 0})')
        if op=='ref': return self.hoooooooooooooooooooooooooooooooo(f'hoooooooooooo({self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])})')
        if op=='handler': return self.hoooooooooooooooooooooooooooooooo(f'hoooooooooooooooo({self.hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])})')
        if op in ('and','or'):
            a=self.hoooooooooooooooooooooooooooo(n.args[0]); value=self.hoooooooooooooooooooooooooooooooo(a)
            self.hoooooooooooooooooooooooooooooo(f'if ({"!" if op=="or" else ""}{a}.as.number) {{'); self.indent+=1
            frame=self.hooooooooooooooooooooooooooooooo('short'); self.hoooooooooooooooooooooooooooooo(f'size_t {frame} = hooooooooo();')
            b=self.hoooooooooooooooooooooooooooo(n.args[1]); self.hoooooooooooooooooooooooooooooo(f'{value} = {b};'); self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({frame});')
            self.indent-=1; self.hoooooooooooooooooooooooooooooo('}'); return value
        if op=='call':
            args=[self.hoooooooooooooooooooooooooooo(a) for a in n.args[1]]
            return self.hoooooooooooooooooooooooooooooooo(f'{self.hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])}({", ".join(args)})')
        if op=='array':
            args=[self.hoooooooooooooooooooooooooooo(a) for a in n.args]
            values='(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo[]){'+', '.join(args)+'}' if args else 'NULL'
            return self.hoooooooooooooooooooooooooooooooo(f'hooooooooooooooooooo({len(args)}, {values})')
        args=[self.hoooooooooooooooooooooooooooo(a) for a in n.args]
        self.hoooooooooooooooooooooooooooooo(f'hooooo({n.token.line}, {n.token.column});')
        return self.hoooooooooooooooooooooooooooooooo(f'{HOO[op]}({", ".join(args)})')
    def hooooooooooooooooooooooooooooo(self,body,global_body=False):
        frame=self.hooooooooooooooooooooooooooooooo('scope'); self.hoooooooooooooooooooooooooooooo(f'size_t {frame} = hooooooooo();')
        for n in body: self.hooooooooooooooooooooooooooooooooo(n,global_body)
        self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({frame});')
    def hooooooooooooooooooooooooooooooooo(self,n,global_body=False):
        op=n.op
        if op=='let' and not global_body: self.hoooooooooooooooooooooooooooooo(f'hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])} = hooooooooooooo();')
        mark=self.hooooooooooooooooooooooooooooooo('statement'); self.hoooooooooooooooooooooooooooooo(f'size_t {mark} = hooooooooo();')
        self.hoooooooooooooooooooooooooooooo(f'hooooo({n.token.line}, {n.token.column});')
        if op in ('let','set'):
            value=self.hoooooooooooooooooooooooooooo(n.args[-1]); self.hoooooooooooooooooooooooooooooo(f'{self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])} = {value};')
        elif op in ('do','print'):
            value=self.hoooooooooooooooooooooooooooo(n.args[0])
            if op=='print': self.hoooooooooooooooooooooooooooooo(f'hoooooooooooooooooooooooooooooooooooooooooo({value});')
        elif op=='return':
            value=self.hoooooooooooooooooooooooooooo(n.args[0]) if n.args[0] else 'hooooooooooooo()'
            self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({self.function_frame});'); self.hoooooooooooooooooooooooooooooo(f'return {value};')
            return
        elif op=='if':
            cond=self.hoooooooooooooooooooooooooooo(n.args[0]); self.hoooooooooooooooooooooooooooooo(f'if ({cond}.as.number) {{'); self.indent+=1
            self.hooooooooooooooooooooooooooooo(n.args[1]); self.indent-=1; self.hoooooooooooooooooooooooooooooo('} else {'); self.indent+=1
            self.hooooooooooooooooooooooooooooo(n.args[2]); self.indent-=1; self.hoooooooooooooooooooooooooooooo('}')
        elif op=='while':
            self.hoooooooooooooooooooooooooooooo('while (1) {'); self.indent+=1
            iteration=self.hooooooooooooooooooooooooooooooo('iteration'); self.hoooooooooooooooooooooooooooooo(f'size_t {iteration} = hooooooooo();')
            cond=self.hoooooooooooooooooooooooooooo(n.args[0]); self.hoooooooooooooooooooooooooooooo(f'if (!{cond}.as.number) {{ hoooooooooo({iteration}); break; }}')
            self.loop_frames.append(iteration); self.hooooooooooooooooooooooooooooo(n.args[1]); self.loop_frames.pop()
            self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({iteration});'); self.hoooooooooooooooooooooooooooooo('hooooooooooo();')
            self.indent-=1; self.hoooooooooooooooooooooooooooooo('}')
        elif op in ('break','continue'):
            self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({self.loop_frames[-1]});'); self.hoooooooooooooooooooooooooooooo(f'{op};'); return
        self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({mark});')
        if op=='let' and not global_body: self.hoooooooooooooooooooooooooooooo(f'hoooooooo(&{self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(n.args[0])});')
        self.hoooooooooooooooooooooooooooooo('hooooooooooo();')
    def hoooooooooooooooooooooooooooooooooo(self):
        self.hoooooooooooooooooooooooooooooo('#include "hoo.h"')
        for name in self.checker.globals: self.hoooooooooooooooooooooooooooooo(f'static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(name)};')
        for f in self.program.functions:
            params=', '.join(f'hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(p)}' for p,_ in f.params) or 'void'
            self.hoooooooooooooooooooooooooooooo(f'static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(f.name)}({params});')
        for f in self.program.functions:
            params=', '.join(f'hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(p)}' for p,_ in f.params) or 'void'
            self.hoooooooooooooooooooooooooooooo(f'static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo {self.hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(f.name)}({params}) {{'); self.indent+=1
            self.function_frame=self.hooooooooooooooooooooooooooooooo('function'); self.hoooooooooooooooooooooooooooooo(f'size_t {self.function_frame} = hooooooooo();')
            for p,_ in f.params: self.hoooooooooooooooooooooooooooooo(f'hoooooooo(&{self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(p)});')
            self.hooooooooooooooooooooooooooooo(f.body)
            self.hoooooooooooooooooooooooooooooo(f'hoooooooooo({self.function_frame});'); self.hoooooooooooooooooooooooooooooo('return hooooooooooooo();')
            self.indent-=1; self.hoooooooooooooooooooooooooooooo('}')
        argc=self.hooooooooooooooooooooooooooooooo(); argv=self.hooooooooooooooooooooooooooooooo()
        self.hoooooooooooooooooooooooooooooo(f'int main(int {argc}, char **{argv}) {{'); self.indent+=1
        self.hoooooooooooooooooooooooooooooo(f'hoo({argc}, {argv});')
        for name in self.checker.globals: self.hoooooooooooooooooooooooooooooo(f'hoooooooo(&{self.hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(name)});')
        self.hooooooooooooooooooooooooooooo(self.program.body,True)
        self.hoooooooooooooooooooooooooooooo('hooo();'); self.hoooooooooooooooooooooooooooooo('return 0;'); self.indent-=1; self.hoooooooooooooooooooooooooooooo('}')
        return '\n'.join(self.lines)+'\n'
