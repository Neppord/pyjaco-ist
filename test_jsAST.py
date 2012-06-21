from jsAST import *
import ast

def test_string_to_name():
    name_node = name('a')
    assert name_node['nodeType'] == 'name'
    assert name_node['value'] == 'a'

def test_PyAst_to_name():
    name_node = name(ast.Name('a', None))
    assert name_node['nodeType'] == 'name'
    assert name_node['value'] == 'a'

def test_int_to_value():
    thing = 1
    assert value(thing) == thing

def test_long_to_value():
    thing = long(1)
    assert value(thing) == thing

def test_float_to_value():
    thing = 1.
    assert value(thing) == thing

def test_str_to_value():
    thing = "hello world"
    assert value(thing) == thing

def test_PyAst_Num_to_value():
    value_node = value(ast.Num(1))
    assert value_node == 1

def test_ops():
    node = op('||')
    assert node['nodeType'] == 'op'
    assert node['value'] == '||'

def test_binary():
    _op = op('||')
    node = binary(1, _op, 2)
    assert node['nodeType'] == 'binary'
    assert node['left'] == 1
    assert node['op'] == _op
    assert node['right'] == 2

def test_function_expr():
    args = ('a', 'b', 'c')
    body = (binary(1, op('+'),2),)
    name = 'helloWorld' 
    function = function_expr(args, body, name)
    assert function['name'] == name
    assert function['args'] == args
    assert function['body'] == body
    assert function['nodeType'] == 'function_expr'

def test_convert():
    num = convert(ast.Num(1))
    assert num == 1
    name = convert(ast.Name('a', ast.Load()))
    assert name['nodeType'] == 'name'
    assert name['value'] == 'a'

