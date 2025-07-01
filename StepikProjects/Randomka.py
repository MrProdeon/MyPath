import random  # Импорт модуля random

num = random.randint(1, 100)  # Загадываем наше число от 1 до 100 включительно
print("Добро пожаловать в числовую угадайку!")  # Приветствие игрока


# Функция для валидации указанного числа
def is_valid(s):
    if s.isdigit:
        n = int(s)
        if 1 <= n <= 100:
            return True
        else:
            return False


flag = True
while flag:
    n = input("Введите число от 1 до 100 : ")
    x = is_valid(n)
    if x:
        n = int(n)
        if n < num:
            print("Ваше число меньше загаданного, попробуйте ещё раз")
        elif n > num:
            print("Ваше число больше загаданного, попробуйте еще раз")
        else:
            print("Вы угадали, поздравляем!")
            print()
            print("Спасибо за игру, всего хорошего!")
            break
    else:
        print("А может быть всё-таки введем целое число от 1 до 100?")
