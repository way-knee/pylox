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

    def comparison():
        expr = self.term()
        while self.match(TokenType.GREATER,
                         TokenType.GREATER_EQUAL,
                         TokenType.LESS,
                         TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term():
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
            return expr

    def factor():
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary():
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary():
        if self.match(TokenType.FALSE): return Literal(False)
        if self.match(TokenType.TRUE): return Literal(True)
        if self.match(TokenType.NIL): return Literal(None)
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression")
            return Grouping(expr)

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

    def consume(_type: TokenType, message: str) -> Token:
        if check(_type):
            return advance()
        raise self.error(self.peek(), message)





