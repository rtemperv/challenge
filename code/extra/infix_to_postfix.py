from code.structures import Stack


def infix_to_postfix(expression):
    operator_stack = Stack()

    precedence_rules = {
        '/': 3,
        '*': 3,
        '+': 2,
        '-': 2,
        '%': 1,
        '(': 1
    }

    output_list = []

    for char in expression:

        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            output_list.append(char)

        elif char == '(':
            operator_stack.push('(')

        elif char == ')':
            current_char = operator_stack.pop()
            while current_char != '(':
                output_list.append(current_char)
                current_char = operator_stack.pop()

        elif char == ' ':
            pass

        elif char in precedence_rules.keys():
            while len(operator_stack) > 0 and precedence_rules[operator_stack.peek()] >= precedence_rules[char]:
                output_list.append(operator_stack.pop())

            operator_stack.push(char)

    while len(operator_stack):
        output_list.append(operator_stack.pop())

    return ' '.join(output_list)


if __name__ == '__main__':
    print(infix_to_postfix('(A + 5) - 3 / 4'))