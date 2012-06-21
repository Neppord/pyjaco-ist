from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd
from ast import Invert, Not, UAdd, USub
from ast import And, Or
from ast import Eq, NotEq, Is, IsNot
from ast import Lt, LtE, Gt, GtE

from ast import Num, Name, Attribute

from ast import BoolOp, BinOp, Compare

from ast import arguments as Arguments
from ast import Lambda

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
def output(node):
    if type(node) == dict:
        if 'value' in node:
            return str(node['value'])
        else:
            return '%s %s %s' % (
                output(node['left']),
                output(node['op']),
                output(node['right'])
            )
    elif type(node) in [str, long, int, float]:
        return repr(node)
    if node.__class__ == Num:
        return str(node.n)
    elif node.__class__ == Name:
        return node.id
    elif node.__class__ == Attribute:
        return '%s.%s' % (output(node.value), output(node.attr))
    elif node.__class__ == BinOp:
        return "%s %s %s" %(
            output(node.left),
            output(node.op),
            output(node.right)
            )
    elif node.__class__ == BoolOp:
        return (" %s " % output(node.op)).join(
            output(value) for value in node.values
        )
    elif node.__class__ == Compare:
        comparators = [output(comparator) for comparator in node.comparators]
        return (" %s " % output(And())).join(
            "(%s %s %s)" % tp for tp in zip(
                [output(node.left)] + comparators,
                (output(op) for op in node.ops),
                comparators
                )
        )
    elif node.__class__ == Arguments:
        return  ", ".join(output(arg) for arg in node.args) 
    elif node.__class__ == Lambda:
        return "function (%s) {return %s;}" % (
            output(node.args),
            output(node.body)
        )
    return ops.get(node.__class__,'')
