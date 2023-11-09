import math

result = 0


def calc_min(x, y):
    result = x - y
    return result


def calc_plus(x, y):
    result = x + y
    return result


def calc_multi(x, y):
    result = x * y
    return result


def calc_multi2(x, y):
    result = x ** y
    return result


def calc_sqrt(x):
    result = math.sqrt(x)
    return result


def calc_cbrt(x):
    result = x ** (1 / 3)
    return result


def calc_division(x, y):
    if y != 0:
        result = x / y
    else:
        result = 'We can\'t divide by zero'
    return result


while 1:
    math_operation = input(
        "\nYou can choose the math operation "
        "\n(available operations): "
        "\n-, +, /, *, **, sqrt, cbrt!"
        "\nFor exit input \"end\""
        "\nInput your choice: ")


    match math_operation:
        case '-':
            first_number = int(input('Input the first number: '))
            second_number = int(input('Input the second number: '))
            print(f'The result = {calc_min(first_number, second_number)}')
        case '+':
            first_number = int(input('Input the first number: '))
            second_number = int(input('Input the second number: '))
            print(f'The result = {calc_plus(first_number, second_number)}')
        case '/':
            first_number = int(input('Input the first number: '))
            second_number = int(input('Input the second number: '))
            result = calc_division(first_number, second_number)
            if isinstance(result, str):
                print(result)
            else:
                print(f'The result = {result}')
        case '*':
            first_number = int(input('Input the first number: '))
            second_number = int(input('Input the second number: '))
            print(f'The result = {calc_multi(first_number, second_number)}')
        case '**':
            first_number = int(input('Input the first number: '))
            second_number = int(input('Input the second number: '))
            print(f'The result = {calc_multi2(first_number, second_number)}')
        case 'sqrt':
            first_number = int(input('Input the first number: '))
            print(f'The result = {calc_sqrt(first_number)}')
        case 'cbrt':
            first_number = int(input('Input the first number: '))
            print(f'The result = {calc_cbrt(first_number)}')
        case _:
            print('Thanks for use our program!')
            break

