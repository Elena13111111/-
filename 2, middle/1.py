import  time
def calculate_expression():
    num1 = int(input('Введите число 1: '))
    znak = input('Введите знак: ')
    num2 = int(input('Введите число 2: '))
    if znak == '+':
        print(f'{num1} {znak} {num2} = {num1 + num2}')
    elif znak == '-':
        print(f'{num1} {znak} {num2} = {num1 - num2}')
    elif znak == '*':
        print(f'{num1} {znak} {num2} = {num1 * num2}')
    elif znak == '/':
        print(f'{num1} {znak} {num2} = {num1 / num2}')
    else:
        print(f'Знак {znak} не поддерживается текущей версией программы')
calculate_expression()
calculate_expression()
