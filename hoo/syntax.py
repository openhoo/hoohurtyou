"""Hoo's handwritten lexer and recursive-descent prefix parser."""
from dataclasses import dataclass

WORDS = {
    2:'end', 3:'let', 4:'set', 5:'function', 6:'body', 7:'return',
    8:'void', 9:'number', 10:'text', 11:'boolean', 12:'list', 13:'widget',
    14:'callback', 15:'if', 16:'else', 17:'while', 18:'do', 19:'print',
    20:'integer', 21:'string', 22:'true', 23:'false', 24:'ref', 25:'call',
    26:'add', 27:'subtract', 28:'multiply', 29:'divide', 30:'remainder',
    31:'equal', 32:'less', 33:'not', 34:'and', 35:'or', 36:'array',
    37:'get', 38:'length', 39:'handler', 40:'concat', 41:'decimal',
    42:'read', 43:'write', 44:'window', 45:'label', 46:'input', 47:'button',
    48:'text_get', 49:'text_set', 50:'run', 51:'quit', 52:'push',
    53:'put', 54:'argument', 55:'argument_count', 56:'negate',
    57:'break', 58:'continue', 59:'parse_number', 60:'exists',
    61:'textarea', 62:'alert', 80:'open_file', 81:'save_file',
    82:'place', 83:'enabled', 84:'home',
}
TYPES = {WORDS[i] for i in range(8,15)}
ARITY = {26:2,27:2,28:2,29:2,30:2,31:2,32:2,33:1,34:2,35:2,
         37:2,38:1,40:2,41:1,42:1,43:2,44:3,45:2,46:2,47:3,
         48:1,49:2,50:0,51:0,52:2,53:3,54:1,55:0,56:1,59:1,60:1,61:2,62:2,80:1,81:1,82:5,83:2,84:0}

@dataclass(frozen=True)
class Token:
    code: int
    line: int
    column: int

class HooError(Exception):
    def __init__(self, message, token=None):
        self.token = token
        super().__init__(f'{token.line}:{token.column}: {message}' if token else message)

@dataclass
class Node:
    op: str
    args: list
    token: Token

@dataclass
class Function:
    name: int
    result: str
    params: list
    body: list
    token: Token

@dataclass
class Program:
    functions: list
    body: list


def lex(source):
    tokens = []
    i, line, col = 0, 1, 1
    while i < len(source):
        c = source[i]
        if c in ' \t\r\n':
            if c == '\n': line, col = line + 1, 1
            else: col += 1
            i += 1
            continue
        start, column = i, col
        if c != 'h':
            raise HooError('only hoo words and ASCII whitespace are allowed', Token(0,line,col))
        i += 1
        while i < len(source) and source[i] == 'o': i += 1
        count = i - start - 1
        if count < 2 or (i < len(source) and source[i] not in ' \t\r\n'):
            raise HooError('a word must be h followed by at least two o characters', Token(count,line,column))
        if count > 4095:
            raise HooError('word exceeds the 4095-o limit', Token(count,line,column))
        tokens.append(Token(count,line,column))
        col += i - start
    tokens.append(Token(0,line,col))
    return tokens

class Parser:
    def __init__(self, tokens): self.tokens, self.pos, self.depth = tokens, 0, 0
    def peek(self): return self.tokens[self.pos]
    def take(self):
        t = self.peek()
        if t.code == 0: raise HooError('unexpected end of source', t)
        self.pos += 1
        return t
    def need(self, code):
        t = self.take()
        if t.code != code: raise HooError(f'expected {WORDS.get(code,code)}, found {WORDS.get(t.code,t.code)}',t)
        return t
    def name(self):
        t = self.take()
        if t.code < 128: raise HooError('identifiers need 128 or more o characters',t)
        return t.code
    def type(self, allow_void=False):
        t = self.take()
        s = WORDS.get(t.code)
        if s not in TYPES or (s == 'void' and not allow_void): raise HooError('expected a value type',t)
        return s
    def parse(self):
        funcs, body = [], []
        while self.peek().code:
            if self.peek().code == 5:
                t = self.take(); name = self.name(); result = self.type(True); params = []
                while self.peek().code != 6: params.append((self.name(),self.type()))
                self.need(6); block = self.block({2}); self.need(2)
                funcs.append(Function(name,result,params,block,t))
            else: body.append(self.statement())
        return Program(funcs,body)
    def block(self, stops):
        result = []
        while self.peek().code not in stops:
            if not self.peek().code: raise HooError('unterminated block',self.peek())
            result.append(self.statement())
        return result
    def statement(self):
        t = self.take(); c = t.code
        if c == 3: return Node('let',[self.name(),self.type(),self.expr()],t)
        if c == 4: return Node('set',[self.name(),self.expr()],t)
        if c == 7:
            value = None if self.peek().code == 2 else self.expr()
            self.need(2)
            return Node('return',[value],t)
        if c == 15:
            cond = self.expr(); self.need(6); yes = self.block({2,16}); no = []
            if self.peek().code == 16: self.take(); no = self.block({2})
            self.need(2)
            return Node('if',[cond,yes,no],t)
        if c == 17:
            cond = self.expr(); self.need(6); body = self.block({2}); self.need(2)
            return Node('while',[cond,body],t)
        if c in (18,19): return Node(WORDS[c],[self.expr()],t)
        if c in (57,58): return Node(WORDS[c],[],t)
        raise HooError('expected a statement',t)
    def expr(self):
        self.depth += 1
        if self.depth > 200: raise HooError('expression nesting exceeds 200',self.peek())
        try: return self._expr()
        finally: self.depth -= 1
    def _expr(self):
        t = self.take(); c = t.code
        if c in (20,21):
            digits = []
            while self.peek().code != 2:
                d = self.take()
                if not 64 <= d.code <= 79: raise HooError('literal requires hexadecimal hoo digits (64..79)',d)
                digits.append(d.code-64)
            self.need(2)
            if c == 20:
                if not digits or len(digits)>16: raise HooError('integer requires 1..16 hexadecimal digits',t)
                n = 0
                for d in digits: n = n*16+d
                if n > 9223372036854775807: raise HooError('integer exceeds signed 64-bit range; use negate',t)
                return Node('integer',[n],t)
            if len(digits)%2: raise HooError('UTF-8 strings require pairs of hexadecimal digits',t)
            raw = bytes(digits[i]*16+digits[i+1] for i in range(0,len(digits),2))
            if b'\0' in raw: raise HooError('strings cannot contain NUL bytes',t)
            try: value = raw.decode('utf-8')
            except UnicodeDecodeError: raise HooError('string is not valid UTF-8',t) from None
            return Node('string',[value],t)
        if c in (22,23): return Node(WORDS[c],[],t)
        if c in (24,39): return Node(WORDS[c],[self.name()],t)
        if c == 25:
            name = self.name(); args = []
            while self.peek().code != 2: args.append(self.expr())
            self.need(2)
            return Node('call',[name,args],t)
        if c == 36:
            values = []
            while self.peek().code != 2: values.append(self.expr())
            self.need(2)
            return Node('array',values,t)
        if c in ARITY: return Node(WORDS[c],[self.expr() for _ in range(ARITY[c])],t)
        raise HooError('expected an expression',t)

def parse(source): return Parser(lex(source)).parse()
