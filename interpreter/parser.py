from token import Token
from tokentype import TokenType
from Expr import *
from Stmt import *
from scanner import Scanner


#class ParseError(RuntimeError):
#    pass

class Parser():
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison();
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self):
        expr = self.term()
        while self.match(TokenType.GREATER,
                         TokenType.GREATER_EQUAL,
                         TokenType.LESS,
                         TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self):
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
            return expr

    def factor(self):
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE): return Literal(False)
        elif self.match(TokenType.TRUE): return Literal(True)
        elif self.match(TokenType.NIL): return Literal(None)
        elif self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)
        elif self.match(TokenType.SUPER):
            keyword = previous()
            consume(TokenType.DOT, "Expect '.' after 'super'.")
            method = consume(TokenType.IDENTIFIER, 'Expect superclass method name.')
            return Super(keyword, method)
        elif self.match(TokenType.THIS): return This(previous())
        elif self.match(TokenType.IDENTIFIER): return Variable(previous())
        elif self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression")
            return Grouping(expr)
        #raise self.error(self.peek(), 'Expected expression')

    def match(self, *types: TokenType):
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def check(self, _type: TokenType):
        if self.is_at_end():
            return False
        return self.peek().tokentype == _type

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().tokentype == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, _type: TokenType, message: str) -> Token:
        if self.check(_type):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token: Token, message: str):
        token_error(token, message)
        return RuntimeError()

    def synchronize(self) -> None:
        self.advance()
        while not self.is_at_end():
            if self.previous().tokentype == TokenType.SEMICOLON:
                return
            elif self.peek().tokentype in [TokenType.CLASS,
                                           TokenType.FUN,
                                           TokenType.VAR,
                                           TokenType.FOR,
                                           TokenType.IF,
                                           TokenType.WHILE,
                                           TokenType.PRINT,
                                           TokenType.RETURN]:
                return self.advance()

    def parse(self):
        try:
            return self.expression()
        except RuntimeError as e:
            return error(previous(), 'parse error')


s = Scanner('3 * 9 - 7;')
tokens = s.scan_tokens()
parser = Parser(tokens)
expression = parser.parse()
from ast_printer import AstPrinter
printer = AstPrinter()
print(printer.print_expr(expression))
