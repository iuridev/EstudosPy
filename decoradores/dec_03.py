import functools




def calculate_decoration(function):
    @functools.wraps(function)
    def result(*args, **kwargs):
        print("usando decorador")
        return function(*args, **kwargs)


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




print(calculate('+', 50, 10))
