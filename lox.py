import sys

class Lox:
    def __init__(self):
        self.args = sys.argv
        self.interpreter = Interpreter()
        self.had_error = False
        self.had_runtime_error = False

    def main(self):
        return

    def run_file(self, path: str) -> None:
        with open(path, 'r') as file:
           run(file.read())
        if had_error:
            sys.exit(65)
        if had_runtime_error:
            sys.exit(70)

    def run_prompt(self) -> None:
        while true:
            line = input('> ')
            if line == None: # to handle Control-C or Control-D
                break
            run(line)
            self.had_error = False
    
    def run(source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scanTokens()
        for token in tokens:
            print(token)

    def error(line: int, message: str) -> None:
        report(line, "", message)

    def report(line: int, where: str, message: str) -> None:
        print(f'[line {line}] Error{where}: {message}')
        had_error = True






