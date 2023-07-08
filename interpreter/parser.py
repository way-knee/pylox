from token import Token
from tokentype import TokenType
from Expr import *
from Stmt import *

class Parser():

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def expression() -> Expr:
        return self.equality()

    def equality() -> Expr:
        expr = self.comparison();
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison() -> Expr:
        expr = self.term()
        while self.match(TokenType.GREATER,
                         TokenType.GREATER_EQUAL,
                         TokenType.LESS,
                         TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term() -> Expr:
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
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

    def is_at_end() -> bool:
        return self.peek().tokentype == TokenType.EOF

    def peek() -> Token:
        return self.tokens[self.current]

    def previous() -> Token:
        return self.tokens[self.current - 1]


