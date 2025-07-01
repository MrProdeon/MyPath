def calculator(num1, sign, num2):
    global result
    if sign == '+':
        result = num1 + num2
    if sign == '-':
        result = num1 - num2
    if sign == '*':
        result = num1 * num2
    if sign == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        result = num1 / num2
    return result


while True:
    print('Начальная версия калькулятора с вводом трех значений : ')


    num1 = input('Введите целое и число или число с плавающей точкой в формате : 123 или 12.3 ---> ' )
    try:
        float(num1)
    except ValueError:
        num1 = input('Допускается ввод только целого числа ли числа с плавающей точкой ---> ')
    finally:
        num1 = float(num1)


    sign = input('Введите арифметическое действие\nДоступные действия для ввода + - * /\n ---> ')
    while sign not in '+-*/':
        sign = input('Доступные действия для ввода + - * /\n ---> ')

    num2 = input('Введите целое и число или число с плавающей точкой в формате : 123 или 12.3 ---> ')
    try:
        float(num2)
    except ValueError:
        num2 = input('Допускается ввод только целого числа ли числа с плавающей точкой ---> ')
    finally:
        num2 = float(num2)

    result = calculator(num1, sign, num2)

    print(f'Результат : {result}')
    print()
    print('Хотите ещё произвести вычисления?\nд если да, н если нет')
    more = input().lower()
    if more == 'н':
        break
print()
print('Конец программы')