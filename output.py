from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd

from ast import Num

from ast import BinOp

ops = {
    Add: '+',
    Sub: '-',
    Mult: '*',
    Div: '/',
    Mod: '%',
    LShift: '<<',
    RShift: '>>',
    BitOr: '|',
    BitXor: '^',
    BitAnd: '&'
}
def output(ast):
    if ast.__class__ == Num:
        return str(ast.n)
    elif ast.__class__ == BinOp:
        return "%s %s %s" %(
            output(ast.left),
            output(ast.op),
            output(ast.right)
            )
    return ops.get(ast.__class__,'')
