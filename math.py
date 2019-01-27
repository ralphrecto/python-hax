from abc import ABCMeta, abstractmethod
from enum import Enum

class Expr(metaclass=ABCMeta):

    @abstractmethod
    def eval(self, varmap):
        pass

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Div(self, other)

class Const(Expr):

    def __init__(self, val):
        super()
        self.val = val

    def eval(self, varmap):
        return self.val

class BinopExpr(Expr, metaclass=ABCMeta):

    def __init__(self, valA, valB):
        super()
        self.valA = valA
        self.valB = valB

    @abstractmethod
    def op(self, lhs, rhs):
        pass

    def eval(self, varmap):
        return self.op(self.valA.eval(varmap), self.valB.eval(varmap))

class Add(BinopExpr):

    def op(self, lhs, rhs):
        return lhs + rhs


class Mul(BinopExpr):

    def op(self, lhs, rhs):
        return lhs * rhs

class Div(BinopExpr):

    def op(self, lhs, rhs):
        return lhs * rhs

class Mul(BinopExpr):

    def op(self, lhs, rhs):
        return lhs * rhs

class Var(Expr):

    def __init__(self, var):
        super()
        self.var = var

    def eval(self, varmap):
        return varmap[self.var]

c = Const(2) * Const(5) + Const(1) * Var("x")
varmap = {"x": 10}
print(c.eval(varmap))
