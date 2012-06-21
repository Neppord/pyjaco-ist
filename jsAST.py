"""
    Javascript AST module

    by: Samuel Ytterbrink 21-jun-2012

    Realized that we need oure own nodes for the JS AST nodes.
    Since I'm a fan of the JS object model, im gona let all nodes be dicts.
    and only let them be created throug handy functions.
    
    common members:
        nodeType: What kind of node it represents.
"""

import ast

def convert(thing):
    for func in (name, value, op):
        try:
            conv = func(thing)
            if conv:
                return conv
        except:
            continue

def name(thing):
    """
        creates a node for a var name
        like the a in the expression
            a + 1
    """
    if type(thing) == str:
        return {
            'nodeType': 'name',
            'value': thing
        }
    elif thing.__class__ == ast.Name:
        return name(thing.id)

def value(thing):
    if type(thing) in [str, int, long, float]:
        return {
            'nodeType': 'value',
            'value': thing
        }
    elif thing.__class__ == ast.Num:
        return value(thing.n)

def op(thing):
    ops = { 
        ast.Add: '+',
        ast.Sub: '-',
        ast.Mult: '*',
        ast.Div: '/',
        ast.Mod: '%',
        ast.LShift: '<<',
        ast.RShift: '>>',
        ast.BitOr: '|',
        ast.BitXor: '^',
        ast.BitAnd: '&',
        ast.Invert: '~',
        ast.Not: '!',
        ast.UAdd: '+',
        ast.USub: '-',
        ast.Eq: '==',
        ast.NotEq: '!=',
        ast.Is: '===',
        ast.IsNot: '!==',
        ast.Lt: '<',
        ast.LtE: '<=',
        ast.Gt: '>',
        ast.GtE: '>=',
        ast.Or: '||',
        ast.And: '&&'
    }
    if thing in ops.values():
        return thing
    return ops[thing.__class__]
