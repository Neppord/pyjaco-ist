from output import output
from jsAST import *

from ast import Attribute

from ast import BoolOp, BinOp, Compare

from ast import arguments as Arguments
from ast import Lambda

def test_binary_operators():
    assert output(op('+')) == '+'

def test_values():
    assert output(value(1)) == '1'
    assert output(name('a')) == 'a'
    assert output(Attribute(value=name('a'), attr=name('b'))) == 'a.b'

def test_binop():
    assert output(BinOp(left=value(1), op=op('+'), right=value(2))) == '1 + 2'

def test_boolop():
    assert output(BoolOp(op('||'),[value(1), value(2)])) == '1 || 2'
def test_compare():
    assert output(Compare(value(5),[op('>'), op('<')], [value(2), value(3)])) == '(5 > 2) && (2 < 3)'

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
