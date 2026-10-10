"""Static type, symbol, arity, scope, control-flow and callback checking."""
from .syntax import HooError

SIGNATURES = {
 'add':('number',['number','number']), 'subtract':('number',['number','number']),
 'multiply':('number',['number','number']), 'divide':('number',['number','number']),
 'remainder':('number',['number','number']), 'less':('boolean',['number','number']),
 'not':('boolean',['boolean']), 'and':('boolean',['boolean','boolean']),
 'or':('boolean',['boolean','boolean']), 'negate':('number',['number']),
 'get':('number',['list','number']), 'concat':('text',['text','text']),
 'decimal':('text',['number']), 'read':('text',['text']), 'write':('void',['text','text']),
 'window':('widget',['text','number','number']), 'label':('widget',['widget','text']),
 'input':('widget',['widget','text']), 'button':('widget',['widget','text','callback']),
 'text_get':('text',['widget']), 'text_set':('void',['widget','text']),
 'run':('void',[]), 'quit':('void',[]), 'push':('void',['list','number']),
 'put':('void',['list','number','number']), 'argument':('text',['number']),
 'textarea':('widget',['widget','text']), 'alert':('void',['widget','text']),
 'open_file':('text',['widget']), 'save_file':('text',['widget']),
 'place':('void',['widget','number','number','number','number']),
 'enabled':('void',['widget','boolean']), 'home':('text',[]),
 'argument_count':('number',[]), 'parse_number':('number',['text']), 'exists':('boolean',['text'])
}

class Checker:
    def __init__(self, program):
        self.program, self.functions, self.globals = program, {}, {}
    def fail(self,n,message): raise HooError(message,n.token)
    def check(self):
        for f in self.program.functions:
            if f.name in self.functions: self.fail(f,'duplicate function')
            if len({p[0] for p in f.params}) != len(f.params): self.fail(f,'duplicate parameter')
            self.functions[f.name] = f
        # Globals are a contiguous declaration prelude, permitting callback access.
        prelude = True
        for s in self.program.body:
            if s.op == 'let':
                if not prelude: self.fail(s,'global declarations must precede executable statements')
                if s.args[0] in self.globals: self.fail(s,'duplicate global')
                self.globals[s.args[0]] = s.args[1]
            else: prelude = False
        self.block(self.program.body,{},None,0,global_body=True)
        for f in self.program.functions:
            env = dict(self.globals); env.update(f.params)
            returns = self.block(f.body,env,f.result,0)
            if f.result != 'void' and not returns: self.fail(f,'function can finish without returning a value')
        return self
    def expect(self,n,env,type_):
        actual = self.expr(n,env)
        if actual != type_: self.fail(n,f'expected {type_}, found {actual}')
    def expr(self,n,env):
        op = n.op
        if op == 'integer': return 'number'
        if op == 'string': return 'text'
        if op in ('true','false'): return 'boolean'
        if op == 'ref':
            if n.args[0] not in env: self.fail(n,'unknown variable')
            return env[n.args[0]]
        if op == 'handler':
            f = self.functions.get(n.args[0])
            if f is None or f.params or f.result != 'void': self.fail(n,'callback requires a zero-parameter void function')
            return 'callback'
        if op == 'call':
            f = self.functions.get(n.args[0])
            if not f: self.fail(n,'unknown function')
            if len(n.args[1]) != len(f.params): self.fail(n,'function argument count mismatch')
            for value,(_,type_) in zip(n.args[1],f.params): self.expect(value,env,type_)
            return f.result
        if op == 'array':
            for a in n.args: self.expect(a,env,'number')
            return 'list'
        if op == 'length':
            if self.expr(n.args[0],env) not in ('list','text'): self.fail(n,'length requires text or list')
            return 'number'
        if op == 'equal':
            a,b = (self.expr(v,env) for v in n.args)
            if a != b or a not in ('number','text','boolean'): self.fail(n,'equality requires matching scalar types')
            return 'boolean'
        result,params = SIGNATURES[op]
        for a,t in zip(n.args,params): self.expect(a,env,t)
        return result
    def block(self,body,env,result,loops,global_body=False):
        env = dict(env); terminated = False; returned = False
        for n in body:
            if terminated: self.fail(n,'unreachable statement')
            op = n.op
            if op == 'let':
                name,type_,expr = n.args
                if name in env: self.fail(n,'variable already declared in this scope; shadowing is forbidden')
                self.expect(expr,env,type_); env[name] = type_
            elif op == 'set':
                name,expr = n.args
                if name not in env: self.fail(n,'assignment to unknown variable')
                self.expect(expr,env,env[name])
            elif op == 'return':
                if result is None: self.fail(n,'return is only valid in functions')
                if result == 'void':
                    if n.args[0] is not None: self.fail(n,'void function cannot return a value')
                else:
                    if n.args[0] is None: self.fail(n,'return value is required')
                    self.expect(n.args[0],env,result)
                terminated = returned = True
            elif op == 'if':
                self.expect(n.args[0],env,'boolean')
                a = self.block(n.args[1],env,result,loops)
                b = self.block(n.args[2],env,result,loops)
                if a and b: terminated = returned = True
            elif op == 'while':
                self.expect(n.args[0],env,'boolean'); self.block(n.args[1],env,result,loops+1)
            elif op in ('break','continue'):
                if not loops: self.fail(n,f'{op} is only valid in loops')
                terminated = True
            elif op == 'print':
                if self.expr(n.args[0],env) not in ('number','text','boolean'): self.fail(n,'print requires a scalar')
            elif op == 'do': self.expr(n.args[0],env)
        return returned
