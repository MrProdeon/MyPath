def get_number(promt):
     while True:
          number = input(promt)

          try:
               return float(number)
          except ValueError:
               print('ОШИБКА : Для ввода допускается только целое число и число с плавающей точкой')
               print()


def get_sign(promt):
     while True:
          sign = input(promt)
          if sign in '+-*/':
               return sign

def calculator(num1, sign, num2):
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        result = num1 / num2
    return result


def ask_continue():
     answer = input('Хотите продолжить вычисления ? д если да ---> ').lower()
     return answer == 'д'


def main():
     while True:
          print('Начало работы с калькулятором')
          first_number = get_number('Введите первое число для вычислений (Пример : 25   23.8)---> ')
          sign = get_sign('Введите знак выражения (+ - * /) ---> ')
          second_number = get_number('Введите второе число для вычислений (Пример : 25   23.8)---> ')

          try :
               print(calculator(first_number, sign, second_number))
          except ZeroDivisionError:
               print('На ноль делить нельзя!')

          if not ask_continue():
               print('Конец программы ')
               break


main()