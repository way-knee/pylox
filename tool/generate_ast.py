import sys

expressions = []
TAB = '    '

args = sys.argv

if __name__ == '__main__':
    if len(args) != 2:
        print('Usage: generate_ast <output directory>')
        sys.exit(64)
    output_dir = args[1]


def define_ast(base_name: str, types: list) -> None:
    path: str = output_dir + '/' + base_name + '.py'

    with open(path, 'w') as output_file:
        lines = []
        lines.append(f'class {base_name}:\n')
        lines.append(f'{TAB}pass\n\n')

        for t in types:
            class_name = t[0]
            fields = t[1]
            define_type(lines, base_name, class_name, fields)
        
        output_file.writelines(lines)


def define_type(lines: list, base_name: str, class_name: str, fields: str) -> None:
    lines.append(f'class {class_name}({base_name}):\n')
    lines.append(f'{TAB}def __init__(self, {fields}):\n')
    fields_list = fields.split(', ')
    for field in fields_list:
        lines.append(f'{TAB}{TAB}self.{field} = {field}\n')
    lines.append('\n')


