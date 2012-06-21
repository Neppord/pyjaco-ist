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

def test_binary():
    assert output(binary(1,op('+'), 2)) == '1 + 2'

def test_function_expr():
    function = function_expr((name('x'),), (name('x'),))
    assert output(function) == 'function (x) {x;}'
    function = function_expr((name('x'),), (name('x'),), name('helloWorld'))
    assert output(function) == 'function helloWorld (x) {x;}'
