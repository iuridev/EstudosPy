import functools


def calculate_decoration(function):
    @functools.wraps(function)
    def result(operation, *args, **kwargs):
        print("usando decorador")
        return function(operation, *args, **kwargs)

    return result


@calculate_decoration
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


print(calculate_decoration(calculate)('+', 50, 10))
