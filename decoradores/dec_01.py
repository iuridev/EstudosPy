def calculate(operation, a, b):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '/':
            return a / b
        case '*':
            return a * b
        case '%':
            return a % b
        case _:
            return "operation invalid!"


def calculate_decoration(operation, a, b):
    print("usando decorador")
    result = calculate(operation, a,b)
    return result


print(calculate('+', 5, 7))
print(calculate_decoration('/',20, 5))

