from Expr import *
from Stmt import *
from token import Token
from tokentype import TokenType

class AstPrinter(ExprVisitor):
    def print_expr(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: Grouping):
        return self.parenthesize('group', expr.expression)

    def visit_literal_expr(self, expr: Literal):
        if expr.value == None:
            return 'nil';
        return str(expr.value)

    def visit_unary_expr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        ret_string = f'({name}'
        for expr in exprs:
            ret_string += f' {expr.accept(self)}'
        ret_string += ')'
        return ret_string

if __name__ == '__main__':
    expression = Binary(
            Unary(
                Token(TokenType.MINUS, '-', None, 1),
                Literal(123)),
            Token(TokenType.STAR, '*', None, 1),
            Grouping(
                Literal(45.67)))
    printer = AstPrinter()
    print(printer.print_expr(expression))
