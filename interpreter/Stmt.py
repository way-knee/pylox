from token import Token

import Expr

class Stmt:
    pass

class Block(Stmt):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements

class Expression(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

class Function(Stmt):
    def __init__(self, name: Token, params: list[Token], body: list[Stmt]):
        self.name = name
        self.params = params
        self.body = body

class Class(Stmt):
    def __init__(self, name: Token, superclass: Expr.Variable, methods: list[Function]):
        self.name = name
        self.superclass = superclass
        self.methods = methods

class If(Stmt):
    def __init__(self, condition: Expr, thenBranch: Stmt, elseBranch: Stmt):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

class Print(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression

class Return(Stmt):
    def __init__(self, keyword: Token, value: Expr):
        self.keyword = keyword
        self.value = value

class Var(Stmt):
    def __init__(self, name: Token, initializer: Expr):
        self.name = name
        self.initializer = initializer

class While(Stmt):
    def __init__(self, condition: Expr, body: Stmt):
        self.condition = condition
        self.body = body

