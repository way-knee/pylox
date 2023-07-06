from token import Token

class ExprVisitor:
    def visitAssignExpr(expr): raise NotImplementedError
    def visitBinaryExpr(expr): raise NotImplementedError
    def visitCallExpr(expr): raise NotImplementedError
    def visitGetExpr(expr): raise NotImplementedError
    def visitGroupingExpr(expr): raise NotImplementedError
    def visitLiteralExpr(expr): raise NotImplementedError
    def visitLogicalExpr(expr): raise NotImplementedError
    def visitSetExpr(expr): raise NotImplementedError
    def visitSuperExpr(expr): raise NotImplementedError
    def visitThisExpr(expr): raise NotImplementedError
    def visitUnaryExpr(expr): raise NotImplementedError
    def visitVariableExpr(expr): raise NotImplementedError


class Expr:
    def accept(visitor: ExprVisitor):
        raise NotImplementedError


class Assign(Expr):
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visitAssignExpr


class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visitBinaryExpr


class Call(Expr):
    def __init__(self, callee: Expr, paren: Token, arguments: list[Expr]):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

    def accept(self, visitor: ExprVisitor):
        return visitor.visitCallExpr


class Get(Expr):
    def __init__(self, object: Expr, name: Token):
        self.object = object
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visitGetExpr


class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: ExprVisitor):
        return visitor.visitGroupingExpr


class Literal(Expr):
    def __init__(self, value: object):
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visitLiteralExpr


class Logical(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visitLogicalExpr


class Set(Expr):
    def __init__(self, _object: Expr, name: Token, value: Expr):
        self._object = _object
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visitSetExpr


class Super(Expr):
    def __init__(self, keyword: Token, method: Token):
        self.keyword = keyword
        self.method = method

    def accept(self, visitor: ExprVisitor):
        return visitor.visitSuperExpr


class This(Expr):
    def __init__(self, keyword: Token):
        self.keyword = keyword

    def accept(self, visitor: ExprVisitor):
        return visitor.visitThisExpr


class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visitUnaryExpr


class Variable(Expr):
    def __init__(self, name: Token):
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visitVariableExpr


