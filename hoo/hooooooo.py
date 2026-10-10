"""Word encoders for tests, templates and editor integrations; not a second language."""
from .hooooo import WORDS
CODES = {v:k for k,v in WORDS.items()}
def hooooo(code):
    if not 2 <= code <= 4095: raise ValueError('word length outside 2..4095')
    return 'h'+'o'*code

def hoooooo(name): return hooooo(CODES[name])
def hooooooo(index):
    if not 0 <= index <= 3967: raise ValueError('identifier index outside 0..3967')
    return hooooo(128+index)
def hoooooooo(value):
    if value < 0: return hoooooooooo('negate',hoooooooo(-value))
    if value > 9223372036854775807: raise ValueError('integer outside signed 64-bit range')
    return ' '.join([hoooooo('integer'),*[hooooo(64+int(d,16)) for d in f'{value:x}'],hoooooo('end')])
def hooooooooo(value):
    if '\0' in value: raise ValueError('NUL is not allowed')
    return ' '.join([hoooooo('string'),*[hooooo(64+int(d,16)) for d in value.encode('utf-8').hex()],hoooooo('end')])
def hoooooooooo(name,*values): return ' '.join([hoooooo(name),*values])
def hooooooooooo(index): return hoooooooooo('ref',hooooooo(index))
def hoooooooooooo(index): return hoooooooooo('handler',hooooooo(index))
def hooooooooooooo(index,*args): return ' '.join([hoooooo('call'),hooooooo(index),*args,hoooooo('end')])
def hoooooooooooooo(index,type_,value): return ' '.join([hoooooo('let'),hooooooo(index),hoooooo(type_),value])
def hooooooooooooooo(index,value): return ' '.join([hoooooo('set'),hooooooo(index),value])
def hoooooooooooooooo(index,result,params,body):
    return ' '.join([hoooooo('function'),hooooooo(index),hoooooo(result),*[hooooooo(p)+' '+hoooooo(t) for p,t in params],hoooooo('body')])+'\n'+body+'\n'+hoooooo('end')
def hooooooooooooooooo(value=''): return ' '.join(v for v in [hoooooo('return'),value,hoooooo('end')] if v)
def hoooooooooooooooooo(condition,yes,no=''):
    return hoooooooooo('if',condition,hoooooo('body'))+'\n'+yes+('\n'+hoooooo('else')+'\n'+no if no else '')+'\n'+hoooooo('end')
def hooooooooooooooooooo(condition,body): return hoooooooooo('while',condition,hoooooo('body'))+'\n'+body+'\n'+hoooooo('end')
def hoooooooooooooooooooo(*args): return ' '.join([hoooooo('array'),*args,hoooooo('end')])
def hooooooooooooooooooooo(*lines): return '\n'.join(lines)+'\n'
