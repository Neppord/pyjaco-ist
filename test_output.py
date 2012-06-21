from output import output
from jsAST import *

from ast import Load, Param

from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd
from ast import Invert, Not, UAdd, USub
from ast import And, Or
from ast import Eq, NotEq, Is, IsNot
from ast import Lt, LtE, Gt, GtE

from ast import Attribute

from ast import BoolOp, BinOp, Compare

from ast import arguments as Arguments
from ast import Lambda

def test_binary_operators():
    assert output(Add()) == '+'
    assert output(Sub()) == '-'
    assert output(Mult()) == '*'
    assert output(Div()) == '/'
    assert output(Mod()) == '%'
    assert output(LShift()) == '<<'
    assert output(RShift()) == '>>'
    assert output(BitOr()) == '|'
    assert output(BitXor()) == '^'
    assert output(BitAnd()) == '&'
    assert output(Or()) == '||'
    assert output(And()) == '&&'

def test_unaray_operators():
    assert output(Invert()) == '~'
    assert output(Not()) == '!'
    assert output(UAdd()) == '+'
    assert output(USub()) == '-'

def test_cmpop():
    assert output(Eq()) == '=='
    assert output(NotEq()) == '!='
    assert output(Is()) == '==='
    assert output(IsNot()) == '!=='
    assert output(Lt()) == '<'
    assert output(LtE()) == '<='
    assert output(Gt()) == '>'
    assert output(GtE()) == '>='

def test_values():
    assert output(value(1)) == '1'
    assert output(name('a')) == 'a'
    assert output(Attribute(value=name('a'), attr=name('b'))) == 'a.b'

def test_binop():
    assert output(BinOp(left=value(1), op=Add(), right=value(2))) == '1 + 2'

def test_boolop():
    assert output(BoolOp(Or(),[value(1), value(2)])) == '1 || 2'
def test_compare():
    assert output(Compare(value(5),[Gt(), Lt()], [value(2), value(3)])) == '(5 > 2) && (2 < 3)'

def test_arguments():
    """JS dont suport kwargs or vargs or dafaults"""
    arguments = Arguments(
        args=[
            name('x'),
            name('y'),
            name('z')
        ],
        vararg=None,
        kwarg=None,
        defaults=[]
    )
    assert output(arguments) == 'x, y, z'
def test_lambda():
    _lambda = Lambda(
                args=Arguments(
                    args=[name('x')],
                    vararg=None,
                    kwarg=None,
                    defaults=[]
                ),
                body=name('x')
    )
    assert output(_lambda) == 'function (x) {return x;}'
