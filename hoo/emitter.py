"""Lower the checked syntax tree to native C with explicit GC root lifetimes."""

class Emitter:
    def __init__(self,program,checker):
        self.program,self.checker = program,checker
        self.lines=[]; self.serial=0; self.indent=0; self.function_frame=None; self.loop_frames=[]
    def line(self,s): self.lines.append('    '*self.indent+s)
    def unique(self,prefix='t'):
        self.serial+=1; return f'{prefix}{self.serial}'
    def temp(self,code):
        name=self.unique(); self.line(f'HValue {name} = {code};'); self.line(f'ho_root(&{name});'); return name
    def expr(self,n):
        op=n.op
        self.line(f'ho_location({n.token.line}, {n.token.column});')
        if op=='integer': return self.temp(f'ho_number(INT64_C({n.args[0]}))')
        if op=='string':
            # ASCII-only octal escapes keep every UTF-8 byte unambiguous to C.
            literal='"'+''.join(f'\\{b:03o}' for b in n.args[0].encode())+'"'
            return self.temp(f'ho_text({literal})')
        if op in ('true','false'): return self.temp(f'ho_boolean({1 if op=="true" else 0})')
        if op=='ref': return self.temp(f'ho_load(v{n.args[0]})')
        if op=='handler': return self.temp(f'ho_callback(f{n.args[0]})')
        if op in ('and','or'):
            a=self.expr(n.args[0]); value=self.temp(a)
            self.line(f'if ({"!" if op=="or" else ""}{a}.as.number) {{'); self.indent+=1
            frame=self.unique('short'); self.line(f'size_t {frame} = ho_frame();')
            b=self.expr(n.args[1]); self.line(f'{value} = {b};'); self.line(f'ho_restore({frame});')
            self.indent-=1; self.line('}'); return value
        if op=='call':
            args=[self.expr(a) for a in n.args[1]]
            return self.temp(f'f{n.args[0]}({", ".join(args)})')
        if op=='array':
            args=[self.expr(a) for a in n.args]
            values='(HValue[]){'+', '.join(args)+'}' if args else 'NULL'
            return self.temp(f'ho_array({len(args)}, {values})')
        args=[self.expr(a) for a in n.args]
        self.line(f'ho_location({n.token.line}, {n.token.column});')
        return self.temp(f'ho_{op}({", ".join(args)})')
    def block(self,body,global_body=False):
        frame=self.unique('scope'); self.line(f'size_t {frame} = ho_frame();')
        for n in body: self.statement(n,global_body)
        self.line(f'ho_restore({frame});')
    def statement(self,n,global_body=False):
        op=n.op
        if op=='let' and not global_body: self.line(f'HValue v{n.args[0]} = ho_void();')
        mark=self.unique('statement'); self.line(f'size_t {mark} = ho_frame();')
        self.line(f'ho_location({n.token.line}, {n.token.column});')
        if op in ('let','set'):
            value=self.expr(n.args[-1]); self.line(f'v{n.args[0]} = {value};')
        elif op in ('do','print'):
            value=self.expr(n.args[0])
            if op=='print': self.line(f'ho_print({value});')
        elif op=='return':
            value=self.expr(n.args[0]) if n.args[0] else 'ho_void()'
            self.line(f'ho_restore({self.function_frame});'); self.line(f'return {value};')
            return
        elif op=='if':
            cond=self.expr(n.args[0]); self.line(f'if ({cond}.as.number) {{'); self.indent+=1
            self.block(n.args[1]); self.indent-=1; self.line('} else {'); self.indent+=1
            self.block(n.args[2]); self.indent-=1; self.line('}')
        elif op=='while':
            self.line('while (1) {'); self.indent+=1
            iteration=self.unique('iteration'); self.line(f'size_t {iteration} = ho_frame();')
            cond=self.expr(n.args[0]); self.line(f'if (!{cond}.as.number) {{ ho_restore({iteration}); break; }}')
            self.loop_frames.append(iteration); self.block(n.args[1]); self.loop_frames.pop()
            self.line(f'ho_restore({iteration});'); self.line('ho_collect();')
            self.indent-=1; self.line('}')
        elif op in ('break','continue'):
            self.line(f'ho_restore({self.loop_frames[-1]});'); self.line(f'{op};'); return
        self.line(f'ho_restore({mark});')
        if op=='let' and not global_body: self.line(f'ho_root(&v{n.args[0]});')
        self.line('ho_collect();')
    def emit(self):
        self.line('#include "hoo_runtime.h"')
        for name in self.checker.globals: self.line(f'static HValue v{name};')
        for f in self.program.functions:
            params=', '.join(f'HValue v{p}' for p,_ in f.params) or 'void'
            self.line(f'static HValue f{f.name}({params});')
        for f in self.program.functions:
            params=', '.join(f'HValue v{p}' for p,_ in f.params) or 'void'
            self.line(f'static HValue f{f.name}({params}) {{'); self.indent+=1
            self.function_frame=self.unique('function'); self.line(f'size_t {self.function_frame} = ho_frame();')
            for p,_ in f.params: self.line(f'ho_root(&v{p});')
            self.block(f.body)
            self.line(f'ho_restore({self.function_frame});'); self.line('return ho_void();')
            self.indent-=1; self.line('}')
        self.line('int main(int argc, char **argv) {'); self.indent+=1
        self.line('ho_init(argc, argv);')
        for name in self.checker.globals: self.line(f'ho_root(&v{name});')
        self.block(self.program.body,True)
        self.line('ho_shutdown();'); self.line('return 0;'); self.indent-=1; self.line('}')
        return '\n'.join(self.lines)+'\n'
