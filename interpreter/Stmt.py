from token import Token

import Expr

class StmtVisitor:
    def visit_block_stmt(stmt): raise NotImplementedError
    def visit_expression_stmt(stmt): raise NotImplementedError
    def visit_function_stmt(stmt): raise NotImplementedError
    def visit_class_stmt(stmt): raise NotImplementedError
    def visit_if_stmt(stmt): raise NotImplementedError
    def visit_print_stmt(stmt): raise NotImplementedError
    def visit_return_stmt(stmt): raise NotImplementedError
    def visit_var_stmt(stmt): raise NotImplementedError
    def visit_while_stmt(stmt): raise NotImplementedError


class Stmt:
    def accept(visitor: StmtVisitor):
        raise NotImplementedError


class Block(Stmt):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_block_stmt


class Expression(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_expression_stmt


class Function(Stmt):
    def __init__(self, name: Token, params: list[Token], body: list[Stmt]):
        self.name = name
        self.params = params
        self.body = body

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_function_stmt


class Class(Stmt):
    def __init__(self, name: Token, superclass: Expr.Variable, methods: list[Function]):
        self.name = name
        self.superclass = superclass
        self.methods = methods

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_class_stmt


class If(Stmt):
    def __init__(self, condition: Expr, thenBranch: Stmt, elseBranch: Stmt):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_if_stmt


class Print(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_print_stmt


class Return(Stmt):
    def __init__(self, keyword: Token, value: Expr):
        self.keyword = keyword
        self.value = value

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_return_stmt


class Var(Stmt):
    def __init__(self, name: Token, initializer: Expr):
        self.name = name
        self.initializer = initializer

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_var_stmt


class While(Stmt):
    def __init__(self, condition: Expr, body: Stmt):
        self.condition = condition
        self.body = body

    def accept(self, visitor: StmtVisitor):
        return visitor.visit_while_stmt


