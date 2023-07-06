from token import Token

class Expr:
    pass

class Assign(Expr):
    def __init__(self, name: Token, value: Expr):
        self.name = name
        self.value = value

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

class Call(Expr):
    def __init__(self, callee: Expr, paren: Token, arguments: list[Expr]):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

class Get(Expr):
    def __init__(self, object: Expr, name: Token):
        self.object = object
        self.name = name

class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

class Literal(Expr):
    def __init__(self, value: object):
        self.value = value

class Logical(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

class Set(Expr):
    def __init__(self, _object: Expr, name: Token, value: Expr):
        self._object = _object
        self.name = name
        self.value = value

class Super(Expr):
    def __init__(self, keyword: Token, method: Token):
        self.keyword = keyword
        self.method = method

class This(Expr):
    def __init__(self, keyword: Token):
        self.keyword = keyword

class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

class Variable(Expr):
    def __init__(self, name: Token):
        self.name = name

