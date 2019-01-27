from abc import ABCMeta, abstractmethod
from enum import Enum

class ExprType(Enum):
    CONST = "CONST"
    VAR = "VAR"
    ADD = "ADD"
    MUL = "MUL"
    SUB = "SUB"
    DIV = "DIV"

class Expr(metaclass=ABCMeta):

    @abstractmethod
    def exprtype(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Div(self, other)

    def match(self, casemap):
        if self.exprtype() in casemap:
            return casemap[self.exprtype()]()
        else:
            raise ValueError("no case found for exprs of exprtype " + self.exprtype())

class Const(Expr):

    def __init__(self, val):
        super()
        self.val = val

    def __repr__(self):
        return str(self.val)

    def exprtype(self):
        return ExprType.CONST

class BinopExpr(Expr, metaclass=ABCMeta):

    def __init__(self, lhs, rhs):
        super()
        self.lhs = lhs
        self.rhs = rhs

    @abstractmethod
    def symbol(self):
        pass

    def __repr__(self):
        return self.lhs.__repr__() + self.symbol() + self.rhs.__repr__()

class Add(BinopExpr):

    def exprtype(self):
        return ExprType.ADD

    def symbol(self):
        return "+"

class Mul(BinopExpr):

    def exprtype(self):
        return ExprType.MUL

    def symbol(self):
        return "*"

class Div(BinopExpr):

    def exprtype(self):
        return ExprType.DIV

    def symbol(self):
        return "/"

class Sub(BinopExpr):

    def exprtype(self):
        return ExprType.Sub

    def symbol(self):
        return "-"

class Var(Expr):

    def __init__(self, var):
        super()
        self.var = var

    def exprtype(self):
        return ExprType.VAR

    def __repr__(self):
        return self.var

def expreval(expr, varmap):
    return expr.match({
        ExprType.CONST: lambda: expr.val,
        ExprType.VAR: lambda: varmap[expr.var],
        ExprType.ADD: lambda: expreval(expr.lhs, varmap) + expreval(expr.rhs, varmap),
        ExprType.MUL: lambda: expreval(expr.lhs, varmap) * expreval(expr.rhs, varmap),
        ExprType.DIV: lambda: expreval(expr.lhs, varmap) / expreval(expr.rhs, varmap),
        ExprType.SUB: lambda: expreval(expr.lhs, varmap) - expreval(expr.rhs, varmap),
    })

c = Const(2) * Const(5) + Const(1) * Var("x")
varmap = {"x": 10}
print(c)
print(expreval(c, varmap))
