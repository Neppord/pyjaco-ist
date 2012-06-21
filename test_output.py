from output import output

from ast import Add, Sub, Mult, Div, Mod, LShift, RShift
from ast import BitOr, BitXor, BitAnd

from ast import Num

from ast import BinOp

def test_operators():
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

def test_values():
    assert output(Num(1)) == '1'
    assert output(Num(1.5)) == '1.5'

def test_binop():
    assert output(BinOp(left=Num(n=1), op=Add(), right=Num(n=2))) == '1 + 2'

