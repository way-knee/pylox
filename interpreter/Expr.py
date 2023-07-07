from token import Token

class ExprVisitor:
    def visit_assign_expr(expr): raise NotImplementedError
    def visit_binary_expr(expr): raise NotImplementedError
    def visit_call_expr(expr): raise NotImplementedError
    def visit_get_expr(expr): raise NotImplementedError
    def visit_grouping_expr(expr): raise NotImplementedError
    def visit_literal_expr(expr): raise NotImplementedError
    def visit_logical_expr(expr): raise NotImplementedError
    def visit_set_expr(expr): raise NotImplementedError
    def visit_super_expr(expr): raise NotImplementedError
    def visit_this_expr(expr): raise NotImplementedError
    def visit_unary_expr(expr): raise NotImplementedError
    def visit_variable_expr(expr): raise NotImplementedError


class Expr:
    def accept(visitor: ExprVisitor):
        raise NotImplementedError


class Assign(Expr):
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_assign_expr


class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_binary_expr


class Call(Expr):
    def __init__(self, callee: Expr, paren: Token, arguments: list[Expr]):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_call_expr


class Get(Expr):
    def __init__(self, object: Expr, name: Token):
        self.object = object
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_get_expr


class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_grouping_expr


class Literal(Expr):
    def __init__(self, value: object):
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_literal_expr


class Logical(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_logical_expr


class Set(Expr):
    def __init__(self, _object: Expr, name: Token, value: Expr):
        self._object = _object
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_set_expr


class Super(Expr):
    def __init__(self, keyword: Token, method: Token):
        self.keyword = keyword
        self.method = method

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_super_expr


class This(Expr):
    def __init__(self, keyword: Token):
        self.keyword = keyword

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_this_expr


class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_unary_expr


class Variable(Expr):
    def __init__(self, name: Token):
        self.name = name

    def accept(self, visitor: ExprVisitor):
        return visitor.visit_variable_expr


