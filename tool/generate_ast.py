import sys

expressions = [
    ['Assign', 'name: Token, value: Expr'],
    ['Binary', 'left: Expr, operator: Token, right: Expr'],
    ['Call', 'callee: Expr, paren: Token, arguments: list[Expr]'],
    ['Get', 'object: Expr, name: Token'],
    ['Grouping', 'expression: Expr'],
    ['Literal', 'value: object'],
    ['Logical', 'left: Expr, operator: Token, right: Expr'],
    ['Set', '_object: Expr, name: Token, value: Expr'],
    ['Super', 'keyword: Token, method: Token'],
    ['This', 'keyword: Token'],
    ['Unary', 'operator: Token, right: Expr'],
    ['Variable', 'name: Token']
]

statements = [
    ['Block', 'statements: list[Stmt]'],
    ['Expression', 'expression: Expr'],
    ['Function', 'name: Token, params: list[Token], body: list[Stmt]'],
    ['Class', 'name: Token, superclass: Expr.Variable, methods: list[Function]'],
    ['If', 'condition: Expr, thenBranch: Stmt, elseBranch: Stmt'],
    ['Print', 'expression: Expr'],
    ['Return', 'keyword: Token, value: Expr'],
    ['Var', 'name: Token, initializer: Expr'],
    ['While', 'condition: Expr, body: Stmt']
]

TAB = '    '
args = sys.argv

def main():
    define_ast('Expr', expressions)
    define_ast('Stmt', statements)


if __name__ == '__main__':
    if len(args) != 2:
        print('Usage: generate_ast <output directory>')
        sys.exit(64)
    output_dir = args[1]


def define_ast(base_name: str, types: list[list]) -> None:
    path: str = output_dir + '/' + base_name + '.py'

    with open(path, 'w') as output_file:
        lines = []
        lines.append('from token import Token\n\n')
        if base_name == 'Stmt':
            lines.append('import Expr\n\n')
        define_visitor(lines, base_name, types)

        lines.append(f'class {base_name}:\n')
        lines.append(f'{TAB}def accept(visitor: {base_name}Visitor):\n')
        lines.append(f'{TAB}{TAB}raise NotImplementedError\n\n\n')

        for t in types:
            class_name = t[0]
            fields = t[1]
            define_type(lines, base_name, class_name, fields)
            lines.append(f'{TAB}def accept(self, visitor: {base_name}Visitor):\n')
            lines.append(f'{TAB}{TAB}return visitor.visit_{t[0].lower()}_{base_name.lower()}(self)\n\n\n')
        
        output_file.writelines(lines)


def define_type(lines: list, base_name: str, class_name: str, fields: str) -> None:
    lines.append(f'class {class_name}({base_name}):\n')
    lines.append(f'{TAB}def __init__(self, {fields}):\n')
    fields_list = fields.split(', ')
    for field in fields_list:
        lines.append(f'{TAB}{TAB}self.{field[:field.index(":")]} = {field[:field.index(":")]}\n')
    lines.append('\n')


def define_visitor(lines: list, base_name: str, types: list[list]):
    lines.append(f'class {base_name}Visitor:\n')
    for t in types:
        lines.append(f'{TAB}def visit_{t[0].lower()}_{base_name.lower()}({base_name.lower()}): raise NotImplementedError\n')
    lines.append('\n\n')



