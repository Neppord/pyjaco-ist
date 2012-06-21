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
