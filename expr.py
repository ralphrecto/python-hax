from abc import ABCMeta, abstractmethod
from enum import Enum

# class ExprType(Enum):
    # CONST = "CONST"
    # ADD = "SUM"

class Expr(metaclass=ABCMeta):

    @abstractmethod
    def eval(self):
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

    def eval(self):
        return self.val

class BinopExpr(Expr, metaclass=ABCMeta):

    def __init__(self, valA, valB):
        super()
        self.valA = valA
        self.valB = valB

    @abstractmethod
    def op(self, lhs, rhs):
        pass

    def eval(self):
        return self.op(self.valA.eval(), self.valB.eval())

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


c = Const(2) * Const(5) + Const(1)
print(c.eval())
