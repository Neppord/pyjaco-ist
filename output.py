from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd
from ast import Invert, Not, UAdd, USub
from ast import And, Or
from ast import Eq, NotEq, Is, IsNot
from ast import Lt, LtE, Gt, GtE

from ast import Num, Name, Attribute

from ast import BoolOp, BinOp, Compare

from ast import arguments as Arguments

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
    BitAnd: '&',
    Invert: '~',
    Not: '!',
    UAdd: '+',
    USub: '-',
    Eq: '==',
    NotEq: '!=',
    Is: '===',
    IsNot: '!==',
    Lt: '<',
    LtE: '<=',
    Gt: '>',
    GtE: '>=',
    Or: '||',
    And: '&&'
}
def output(ast):
    if ast.__class__ == Num:
        return str(ast.n)
    elif ast.__class__ == Name:
        return ast.id
    elif ast.__class__ == Attribute:
        return '%s.%s' % (output(ast.value), output(ast.attr))
    elif ast.__class__ == BinOp:
        return "%s %s %s" %(
            output(ast.left),
            output(ast.op),
            output(ast.right)
            )
    elif ast.__class__ == BoolOp:
        return (" %s " % output(ast.op)).join(
            output(value) for value in ast.values
        )
    elif ast.__class__ == Compare:
        comparators = [output(comparator) for comparator in ast.comparators]
        return (" %s " % output(And())).join(
            "(%s %s %s)" % tp for tp in zip(
                [output(ast.left)] + comparators,
                (output(op) for op in ast.ops),
                comparators
                )
        )
    elif ast.__class__ == Arguments:
        return  ", ".join(output(arg) for arg in ast.args) 
    return ops.get(ast.__class__,'')
