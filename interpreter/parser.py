from token import Token
from tokentype import TokenType
from Expr import *
from Stmt import *

class Parser():

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def expression():
        return self.equality()

    def equality():
        expr = self.comparison();
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def match(*types: TokenType):
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def check(_type: TokenType):
        if self.is_at_end():
            return False
        return self.peek().tokentype == _type

    def advance() -> Token:
        if not self.is_at_end():
            current += 1
        return self.previous()


