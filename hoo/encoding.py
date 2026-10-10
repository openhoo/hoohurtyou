"""Word encoders for tests, templates and editor integrations; not a second language."""
from .syntax import WORDS
CODES = {v:k for k,v in WORDS.items()}
def word(code):
    if not 2 <= code <= 4095: raise ValueError('word length outside 2..4095')
    return 'h'+'o'*code

def token(name): return word(CODES[name])
def identifier(index):
    if not 0 <= index <= 3967: raise ValueError('identifier index outside 0..3967')
    return word(128+index)
def integer(value):
    if value < 0: return expression('negate',integer(-value))
    if value > 9223372036854775807: raise ValueError('integer outside signed 64-bit range')
    return ' '.join([token('integer'),*[word(64+int(d,16)) for d in f'{value:x}'],token('end')])
def text(value):
    if '\0' in value: raise ValueError('NUL is not allowed')
    return ' '.join([token('string'),*[word(64+int(d,16)) for d in value.encode('utf-8').hex()],token('end')])
def expression(name,*values): return ' '.join([token(name),*values])
def ref(index): return expression('ref',identifier(index))
def handler(index): return expression('handler',identifier(index))
def call(index,*args): return ' '.join([token('call'),identifier(index),*args,token('end')])
def let(index,type_,value): return ' '.join([token('let'),identifier(index),token(type_),value])
def set_(index,value): return ' '.join([token('set'),identifier(index),value])
def function(index,result,params,body):
    return ' '.join([token('function'),identifier(index),token(result),*[identifier(p)+' '+token(t) for p,t in params],token('body')])+'\n'+body+'\n'+token('end')
def return_(value=''): return ' '.join(v for v in [token('return'),value,token('end')] if v)
def if_(condition,yes,no=''):
    return expression('if',condition,token('body'))+'\n'+yes+('\n'+token('else')+'\n'+no if no else '')+'\n'+token('end')
def while_(condition,body): return expression('while',condition,token('body'))+'\n'+body+'\n'+token('end')
def array(*args): return ' '.join([token('array'),*args,token('end')])
def program(*lines): return '\n'.join(lines)+'\n'
