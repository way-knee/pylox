from token import Token

import Expr

class StmtVisitor:
    def visitBlockStmt(stmt): raise NotImplementedError
    def visitExpressionStmt(stmt): raise NotImplementedError
    def visitFunctionStmt(stmt): raise NotImplementedError
    def visitClassStmt(stmt): raise NotImplementedError
    def visitIfStmt(stmt): raise NotImplementedError
    def visitPrintStmt(stmt): raise NotImplementedError
    def visitReturnStmt(stmt): raise NotImplementedError
    def visitVarStmt(stmt): raise NotImplementedError
    def visitWhileStmt(stmt): raise NotImplementedError


class Stmt:
    def accept(visitor: StmtVisitor):
        raise NotImplementedError


class Block(Stmt):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements

    def accept(self, visitor: StmtVisitor):
        return visitor.visitBlockStmt


class Expression(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visitExpressionStmt


class Function(Stmt):
    def __init__(self, name: Token, params: list[Token], body: list[Stmt]):
        self.name = name
        self.params = params
        self.body = body

    def accept(self, visitor: StmtVisitor):
        return visitor.visitFunctionStmt


class Class(Stmt):
    def __init__(self, name: Token, superclass: Expr.Variable, methods: list[Function]):
        self.name = name
        self.superclass = superclass
        self.methods = methods

    def accept(self, visitor: StmtVisitor):
        return visitor.visitClassStmt


class If(Stmt):
    def __init__(self, condition: Expr, thenBranch: Stmt, elseBranch: Stmt):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

    def accept(self, visitor: StmtVisitor):
        return visitor.visitIfStmt


class Print(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: StmtVisitor):
        return visitor.visitPrintStmt


class Return(Stmt):
    def __init__(self, keyword: Token, value: Expr):
        self.keyword = keyword
        self.value = value

    def accept(self, visitor: StmtVisitor):
        return visitor.visitReturnStmt


class Var(Stmt):
    def __init__(self, name: Token, initializer: Expr):
        self.name = name
        self.initializer = initializer

    def accept(self, visitor: StmtVisitor):
        return visitor.visitVarStmt


class While(Stmt):
    def __init__(self, condition: Expr, body: Stmt):
        self.condition = condition
        self.body = body

    def accept(self, visitor: StmtVisitor):
        return visitor.visitWhileStmt


