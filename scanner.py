from token import Token
from tokentype import TokenType
from lox import Lox

class Scanner:

    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens() -> list:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(EOF, '', None, self.line))
        return self.tokens

    def scan_token() -> None:
        c = advance()
        if c == '(': self.add_token(LEFT_PAREN)
        elif c == ')': self.add_token(RIGHT_PAREN)
        elif c == '{': self.add_token(LEFT_BRACE)
        elif c == '}': self.add_token(RIGHT_BRACE)
        elif c == ',': self.add_token(COMMA)
        elif c == '.': self.add_token(DOT)
        elif c == '-': self.add_token(MINUS)
        elif c == '+': self.add_token(PLUS)
        elif c == ';': self.add_token(SEMICOLON)
        elif c == '*': self.add_token(STAR)
        elif c == '!': 
            if self.match('='): self.add_token(BANG_EQUAL)
            else: self.add_token(BANG)
        elif c == '=':
            if self.match('='): self.add_token(EQUAL_EQUAL)
            else: self.add_token(EQUAL)
        elif c == '<':
            if self.match('='): self.add_token(LESS_EQUAL)
            else: self.add_token(LESS)
        elif c == '>':
            if self.match('='): self.add_token(GREATER_EQUAL)
            else: self.add_token(GREATER)
        elif c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(SLASH)
        elif c ==' ' or c == '\r' or c == '\t':
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.string()
        else:
            if self.is_digit(c): self.number()
            elif self.is_alpha(c): self.identifier()
        else: Lox.error(line, 'Unexpected character.')



