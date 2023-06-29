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
        self.keywords = {
                'and': AND,
                'class': CLASS,
                'else': ELSE,
                'false': FALSE,
                'for': FOR,
                'fun': FUN,
                'if': IF,
                'nil': NIL,
                'or': OR,
                'print': PRINT,
                'return': RETURN,
                'super': SUPER,
                'this': THIS,
                'true': TRUE,
                'var': VAR,
                'while': WHILE}

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
            else: Lox.error(self.line, 'Unexpected character.')

    def advance(self) -> str:
        current += 1
        return self.source[self.current - 1]

    def add_token(self, token_type: TokenType, literal = None) -> None:
        text: str = self.source[self.start : self.current]
        self.tokens.append( Token(token_type, text, literal, line))

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def match(self, expected: str) -> bool:
        if self.is_at_end(): return False
        if self.source[current] != expected: return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.is_at_end(): return '\0'
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]

    def is_alpha(self, s: str) -> bool:
        return ((s >= 'a' and s <= 'z') or
                (s >= 'A' and s <= 'Z') or
                (s == '_'))

    def is_digit(self, s: str) -> bool:
        return (s >= '0' and s <= '9')

    def is_alpha_numeric(self, s: str) -> bool:
        return (self.is_alpha(s) or self.is_digit(s))

    def identifier(self) -> None:
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        text: str = self.source[self.start : self.current]
        token_type: TokenType = self.keywords.get(text)
        if token_type == None:
            token_type = IDENTIFIER
        self.add_token(token_type)

    def number(self) -> None:
        while self.is_digit(self.peek()):
            self.advance()
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        self.add_token(NUMBER, float(self.source[self.start : self.current]))

    def string(self) -> None:
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n': self.line += 1
            self.advance()
        if is_at_end:
            Lox.error(self,line, 'Unterminated string.')
            return
        self.advance()
        val: str = self.source[self.start + 1 : self.current - 1]
        self.add_token(STRING, val)
