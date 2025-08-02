field = [[None for _ in range (3)]for _ in range(3)] # Игровое поле 3 на 3

def get_elem(elem='X'):
    """Функция для запроса крестика и попытки вставки в игровое поле"""
    print('Допустимые значения для вставки - от 1 до 3 включительно')
    while True:
        string = int(input('Ведите строку для вставки ---> '))
        while string not in (1, 2 ,3):
            string = int(input('Ведите строку для вставки ---> '))

        column = int(input('Введите столбец для вставки ---> '))
        while column not in (1, 2, 3):
            column = int(input('Введите столбец для вставки ---> '))


        if field[string - 1][column - 1] is None:
            field[string - 1][column - 1] = elem
            break
        else:
            print('В этом месте уже есть элемент. Выберите другое пустое место.')
            continue


def check_winner():
    string1 = [field[0][0], field[0][1], field[0][2]]
    string2 = [field[1][0], field[1][1], field[1][2]]
    string3 = [field[2][0], field[2][1], field[2][2]]
    column1 = [field[0][0], field[1][0], field[2][0]]
    column2 = [field[0][1], field[1][1], field[2][1]]
    column3 = [field[0][2], field[1][2], field[2][2]]
    diag1 = [field[0][0], field[1][1], field[2][2]]
    diag2 = [field[0][2], field[1][1], field[2][0]]

    lines = [string1, string2, string3, column1, column2, column3, diag1, diag2]

    for line in lines:
        if line.count('X') == 3:
            return 'X'
        elif line.count(0) == 3:
            return 0
    return None


def main():
    for i in range(3):
        for j in range(3):
            print(str(field[i][j]).ljust(8), end=' ')
        print()
    total = 0
    while total < 9:
        get_elem('X')
        total += 1
        for i in range(3):
            for j in range(3):
                print(str(field[i][j]).ljust(8), end=' ')
            print()
        winner = check_winner()
        if winner is not None:
            print(f'Победитель - {winner}')
            break
        if total == 9:
            print('Ничья')
            break


        get_elem(0)
        total += 1
        for i in range(3):
            for j in range(3):
                print(str(field[i][j]).ljust(8), end=' ')
            print()
        winner =  check_winner()
        if winner is not None:
            print(f'Победитель - {winner}')
            break
        if total == 9:
            print('Ничья')
            break


main()