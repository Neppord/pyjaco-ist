from output import output

from ast import Load, Param

from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd
from ast import Invert, Not, UAdd, USub
from ast import And, Or
from ast import Eq, NotEq, Is, IsNot
from ast import Lt, LtE, Gt, GtE

from ast import Num, Name, Attribute

from ast import BoolOp, BinOp, Compare

from ast import arguments as Arguments

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
    assert output(Num(1)) == '1'
    assert output(Num(1.5)) == '1.5'
    assert output(Name('a', Load())) == 'a'
    assert output(Name('a', Param())) == 'a'
    assert output(Attribute(value=Name('a', Load()), attr=Name('b', Load()))) == 'a.b'

def test_binop():
    assert output(BinOp(left=Num(n=1), op=Add(), right=Num(n=2))) == '1 + 2'

def test_boolop():
    assert output(BoolOp(Or(),[Num(1), Num(2)])) == '1 || 2'
def test_compare():
    assert output(Compare(Num(5),[Gt(), Lt()], [Num(2), Num(3)])) == '(5 > 2) && (2 < 3)'

def test_arguments():
    """JS dont suport kwargs or vargs or dafaults"""
    arguments = Arguments(
        args=[
            Name(id='x', ctx=Param()),
            Name(id='y', ctx=Param()),
            Name(id='z', ctx=Param())
        ],
        vararg=None,
        kwarg=None,
        defaults=[]
    )
    assert output(arguments) == 'x, y, z'
