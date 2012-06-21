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
    value_node = value(1)
    assert value_node['nodeType'] == 'value'
    assert value_node['value'] == 1

def test_long_to_value():
    value_node = value(long(1))
    assert value_node['nodeType'] == 'value'
    assert value_node['value'] == long(1)

def test_float_to_value():
    value_node = value(1.)
    assert value_node['nodeType'] == 'value'
    assert value_node['value'] == 1.

def test_str_to_value():
    value_node = value("Hello World")
    assert value_node['nodeType'] == 'value'
    assert value_node['value'] == "Hello World"

def test_PyAst_Num_to_value():
    value_node = value(ast.Num(1))
    assert value_node['nodeType'] == 'value'
    assert value_node['value'] == 1

def test_ops_():
   assert op('||') == '||'

def test_convert():
    num = convert(ast.Num(1))
    assert num['nodeType'] == 'value'
    assert num['value'] == 1
    name = convert(ast.Name('a', ast.Load()))
    assert name['nodeType'] == 'name'
    assert name['value'] == 'a'

