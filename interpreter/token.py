from tokentype import TokenType

class Token:

    def __init__(self, 
                 tokentype: TokenType, 
                 lexeme: str, 
                 literal, 
                 line: int):
        self.tokentype = tokentype
        self.lexeme = lexeme
        self.literal = literal
        self.line = line


    def to_string(self) -> str:
        return tokentype + ' ' + lexeme + ' ' + literal

        
