import re


def separate_symbols_and_numbers(input_string):
    pattern = r'(\d+|[+\-*/()])'
    matches = re.findall(pattern, input_string)
    return matches


def solver(formula: list[str], dep: int) -> int:
    stack = []
    current_num = 0
    current_op = '+'
    is_jump = False

    for index, token in enumerate(formula):
        if token == ')':
            is_jump = False

        if is_jump:
            continue

        if token.isdigit():
            current_num = int(token)
        elif token in '+-*/':
            current_op = token
            continue
        elif token == '(':
            is_jump = True
            current_num = solver(formula[index + 1:-1], dep=dep+1)
        elif token == ')':
            if dep > formula.count(')') - 1:
                break
            else:
                continue

        if current_op == '+':
            stack.append(current_num)
        elif current_op == '-':
            stack.append(-current_num)
        elif current_op == '*':
            stack[-1] *= current_num
        elif current_op == '/':
            stack[-1] /= current_num

    return sum(stack)


def main():
    input_str = "34 + 5 * (2 - 7 *(6-4)) - 5" #"34 + 5 - 5" #
    input_num = separate_symbols_and_numbers(input_str)
    print(input_num)
    print(solver(input_num, 0))



if __name__ == "__main__":
    main()
