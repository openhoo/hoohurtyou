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
class hoooooooooooooooooooooooooooooooooooooooooooooooo:
    code: int
    line: int
    column: int

class hooooooooooooooooooooooooooooooooooooooooooooooooo(Exception):
    def __init__(self, message, token=None):
        self.token = token
        super().__init__(f'{token.line}:{token.column}: {message}' if token else message)

@dataclass
class hoooooooooooooooooooooooooooooooooooooooooooooooooo:
    op: str
    args: list
    token: hoooooooooooooooooooooooooooooooooooooooooooooooo

@dataclass
class hooooooooooooooooooooooooooooooooooooooooooooooooooo:
    name: int
    result: str
    params: list
    body: list
    token: hoooooooooooooooooooooooooooooooooooooooooooooooo

@dataclass
class hoooooooooooooooooooooooooooooooooooooooooooooooooooo:
    functions: list
    body: list


def hoooooooooooooooooooooo(source):
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
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('only hoo words and ASCII whitespace are allowed', hoooooooooooooooooooooooooooooooooooooooooooooooo(0,line,col))
        i += 1
        while i < len(source) and source[i] == 'o': i += 1
        count = i - start - 1
        if count < 2 or (i < len(source) and source[i] not in ' \t\r\n'):
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('a word must be h followed by at least two o characters', hoooooooooooooooooooooooooooooooooooooooooooooooo(count,line,column))
        if count > 4095:
            raise hooooooooooooooooooooooooooooooooooooooooooooooooo('word exceeds the 4095-o limit', hoooooooooooooooooooooooooooooooooooooooooooooooo(count,line,column))
        tokens.append(hoooooooooooooooooooooooooooooooooooooooooooooooo(count,line,column))
        col += i - start
    tokens.append(hoooooooooooooooooooooooooooooooooooooooooooooooo(0,line,col))
    return tokens

class hooooooooooooooooooooooooooooooooooooooooooooooooooooo:
    def __init__(self, tokens): self.tokens, self.pos, self.depth = tokens, 0, 0
    def hooooooooooooooooooooooooooooooooooo(self): return self.tokens[self.pos]
    def hoooooooooooooooooooooooooooooooooooo(self):
        t = self.hooooooooooooooooooooooooooooooooooo()
        if t.code == 0: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('unexpected end of source', t)
        self.pos += 1
        return t
    def hooooooooooooooooooooooooooooooooooooo(self, code):
        t = self.hoooooooooooooooooooooooooooooooooooo()
        if t.code != code: raise hooooooooooooooooooooooooooooooooooooooooooooooooo(f'expected {WORDS.get(code,code)}, found {WORDS.get(t.code,t.code)}',t)
        return t
    def hoooooooooooooooooooooooooooooooooooooo(self):
        t = self.hoooooooooooooooooooooooooooooooooooo()
        if t.code < 128: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('identifiers need 128 or more o characters',t)
        return t.code
    def hooooooooooooooooooooooooooooooooooooooo(self, allow_void=False):
        t = self.hoooooooooooooooooooooooooooooooooooo()
        s = WORDS.get(t.code)
        if s not in TYPES or (s == 'void' and not allow_void): raise hooooooooooooooooooooooooooooooooooooooooooooooooo('expected a value type',t)
        return s
    def hooooooooooooooooooooooo(self):
        funcs, body = [], []
        while self.hooooooooooooooooooooooooooooooooooo().code:
            if self.hooooooooooooooooooooooooooooooooooo().code == 5:
                t = self.hoooooooooooooooooooooooooooooooooooo(); name = self.hoooooooooooooooooooooooooooooooooooooo(); result = self.hooooooooooooooooooooooooooooooooooooooo(True); params = []
                while self.hooooooooooooooooooooooooooooooooooo().code != 6: params.append((self.hoooooooooooooooooooooooooooooooooooooo(),self.hooooooooooooooooooooooooooooooooooooooo()))
                self.hooooooooooooooooooooooooooooooooooooo(6); block = self.hooooooooooooooooooooooooooooo({2}); self.hooooooooooooooooooooooooooooooooooooo(2)
                funcs.append(hooooooooooooooooooooooooooooooooooooooooooooooooooo(name,result,params,block,t))
            else: body.append(self.hooooooooooooooooooooooooooooooooo())
        return hoooooooooooooooooooooooooooooooooooooooooooooooooooo(funcs,body)
    def hooooooooooooooooooooooooooooo(self, stops):
        result = []
        while self.hooooooooooooooooooooooooooooooooooo().code not in stops:
            if not self.hooooooooooooooooooooooooooooooooooo().code: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('unterminated block',self.hooooooooooooooooooooooooooooooooooo())
            result.append(self.hooooooooooooooooooooooooooooooooo())
        return result
    def hooooooooooooooooooooooooooooooooo(self):
        t = self.hoooooooooooooooooooooooooooooooooooo(); c = t.code
        if c == 3: return hoooooooooooooooooooooooooooooooooooooooooooooooooo('let',[self.hoooooooooooooooooooooooooooooooooooooo(),self.hooooooooooooooooooooooooooooooooooooooo(),self.hoooooooooooooooooooooooooooo()],t)
        if c == 4: return hoooooooooooooooooooooooooooooooooooooooooooooooooo('set',[self.hoooooooooooooooooooooooooooooooooooooo(),self.hoooooooooooooooooooooooooooo()],t)
        if c == 7:
            value = None if self.hooooooooooooooooooooooooooooooooooo().code == 2 else self.hoooooooooooooooooooooooooooo()
            self.hooooooooooooooooooooooooooooooooooooo(2)
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('return',[value],t)
        if c == 15:
            cond = self.hoooooooooooooooooooooooooooo(); self.hooooooooooooooooooooooooooooooooooooo(6); yes = self.hooooooooooooooooooooooooooooo({2,16}); no = []
            if self.hooooooooooooooooooooooooooooooooooo().code == 16: self.hoooooooooooooooooooooooooooooooooooo(); no = self.hooooooooooooooooooooooooooooo({2})
            self.hooooooooooooooooooooooooooooooooooooo(2)
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('if',[cond,yes,no],t)
        if c == 17:
            cond = self.hoooooooooooooooooooooooooooo(); self.hooooooooooooooooooooooooooooooooooooo(6); body = self.hooooooooooooooooooooooooooooo({2}); self.hooooooooooooooooooooooooooooooooooooo(2)
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('while',[cond,body],t)
        if c in (18,19): return hoooooooooooooooooooooooooooooooooooooooooooooooooo(WORDS[c],[self.hoooooooooooooooooooooooooooo()],t)
        if c in (57,58): return hoooooooooooooooooooooooooooooooooooooooooooooooooo(WORDS[c],[],t)
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('expected a statement',t)
    def hoooooooooooooooooooooooooooo(self):
        self.depth += 1
        if self.depth > 200: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('expression nesting exceeds 200',self.hooooooooooooooooooooooooooooooooooo())
        try: return self.hoooooooooooooooooooooooooooooooooooooooo()
        finally: self.depth -= 1
    def hoooooooooooooooooooooooooooooooooooooooo(self):
        t = self.hoooooooooooooooooooooooooooooooooooo(); c = t.code
        if c in (20,21):
            digits = []
            while self.hooooooooooooooooooooooooooooooooooo().code != 2:
                d = self.hoooooooooooooooooooooooooooooooooooo()
                if not 64 <= d.code <= 79: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('literal requires hexadecimal hoo digits (64..79)',d)
                digits.append(d.code-64)
            self.hooooooooooooooooooooooooooooooooooooo(2)
            if c == 20:
                if not digits or len(digits)>16: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('integer requires 1..16 hexadecimal digits',t)
                n = 0
                for d in digits: n = n*16+d
                if n > 9223372036854775807: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('integer exceeds signed 64-bit range; use negate',t)
                return hoooooooooooooooooooooooooooooooooooooooooooooooooo('integer',[n],t)
            if len(digits)%2: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('UTF-8 strings require pairs of hexadecimal digits',t)
            raw = bytes(digits[i]*16+digits[i+1] for i in range(0,len(digits),2))
            if b'\0' in raw: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('strings cannot contain NUL bytes',t)
            try: value = raw.decode('utf-8')
            except UnicodeDecodeError: raise hooooooooooooooooooooooooooooooooooooooooooooooooo('string is not valid UTF-8',t) from None
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('string',[value],t)
        if c in (22,23): return hoooooooooooooooooooooooooooooooooooooooooooooooooo(WORDS[c],[],t)
        if c in (24,39): return hoooooooooooooooooooooooooooooooooooooooooooooooooo(WORDS[c],[self.hoooooooooooooooooooooooooooooooooooooo()],t)
        if c == 25:
            name = self.hoooooooooooooooooooooooooooooooooooooo(); args = []
            while self.hooooooooooooooooooooooooooooooooooo().code != 2: args.append(self.hoooooooooooooooooooooooooooo())
            self.hooooooooooooooooooooooooooooooooooooo(2)
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('call',[name,args],t)
        if c == 36:
            values = []
            while self.hooooooooooooooooooooooooooooooooooo().code != 2: values.append(self.hoooooooooooooooooooooooooooo())
            self.hooooooooooooooooooooooooooooooooooooo(2)
            return hoooooooooooooooooooooooooooooooooooooooooooooooooo('array',values,t)
        if c in ARITY: return hoooooooooooooooooooooooooooooooooooooooooooooooooo(WORDS[c],[self.hoooooooooooooooooooooooooooo() for _ in range(ARITY[c])],t)
        raise hooooooooooooooooooooooooooooooooooooooooooooooooo('expected an expression',t)

def hooooooooooooooooooooooo(source): return hooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooo(source)).hooooooooooooooooooooooo()
