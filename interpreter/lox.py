import sys
from token import Token
from tokentype import TokenType

args = sys.argv
had_error = False
had_runtime_error = False

def run_file(path: str) -> None:
    with open(path, 'r') as file:
        run(file.read())
    if had_error:
        sys.exit(65)
    if had_runtime_error:
        sys.exit(70)

def run_prompt() -> None:
    while True:
        line = input('> ')
        if line == None: # to handle Control-C or Control-D, do I need this line?
            break
        run(line)
        had_error = False

def run(source: str) -> None:
    from scanner import Scanner
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)

def error(line: int, message: str) -> None:
    report(line, '', message)

def report(line: int, where: str, message: str) -> None:
    print(f'[line {line}] Error{where}: {message}')
    had_error = True

def token_error(token: Token, message: str) -> None:
    if token.tokentype == TokenType.EOF:
        self.report(token.line, ' at end', message)
    else:
        self.report(token.line, f' at "{token.lexeme}"', message)


