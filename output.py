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
        elif 'left' in node:
            return '%s %s %s' % (
                output(node['left']),
                output(node['op']),
                output(node['right'])
            )
        else:
            if 'name' in node and node['name']:
                return "function %s (%s) {%s;}" % (
                    output(node['name']),
                    ', '.join(output(arg) for arg in node['args']),
                    ';'.join(output(stmt) for stmt in node['stmts'])
                )
            else:
                return "function (%s) {%s;}" % (
                    ', '.join(output(arg) for arg in node['args']),
                    ';'.join(output(stmt) for stmt in node['stmts'])
                )
    elif type(node) in [str, long, int, float]:
        return repr(node)
    elif node.__class__ == Attribute:
        return '%s.%s' % (output(node.value), output(node.attr))
