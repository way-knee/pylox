import sys

class Lox:
    def __init__(self):
        self.args = sys.argv
        self.interpreter = Interpreter()

    def main(self):
