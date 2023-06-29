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
        if self.had_error:
            sys.exit(65)
        if self.had_runtime_error:
            sys.exit(70)

    def run_prompt(self) -> None:
        while true:
            line = input('> ')
            if line == None: # to handle Control-C or Control-D
                break
            self.run(line)
            self.had_error = False
    
    def run(self, source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

    def error(line: int, message: str) -> None:
        self.report(line, '', message)

    def report(self, line: int, where: str, message: str) -> None:
        print(f'[line {line}] Error{where}: {message}')
        self.had_error = True






