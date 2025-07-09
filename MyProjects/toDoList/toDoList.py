# Проект на стадии разработки

toDoList = []

def get_case(case, time, tag, progress = 'Не выполнено') -> dict:
    """Получение данных от пользователя о его делах"""
    return {'Дело' : case, 'Время' : time, 'Пометка' : tag, 'Прогресс' : progress}


def add_a_case(case) -> None:
    """Добавление дел в список"""
    toDoList.append(case)


def end_or_continue():
    """Уточнение у пользователя нужно ли добавить ещё задачи"""
    answer = input('Хотите ещё добавить задачу ? д если да, н если нет ---> ')
    while answer not in ('д', 'н'):
        answer = input('Неверный формат ввода. д если да, н если нет ---> ')
    return answer == 'д'


#Хочу сделать чтобы можно было выводить определенные значения словаря, пока что вывод всех словарей
def get_dict(lst, progress = None):
    for line in lst:
        if progress is None or line.get('Прогресс') == progress:
            print(line)




def main() -> None:
    while True:
        case : str = input('Введите ваше дело : ')
        time : str = input('До какого времени выполнить (Синтаксис = 01.01.2001 ) : ')
        tag : str = input('Введите пометку, если требуется : ')
        add_a_case(get_case(case, time, tag))




        if not end_or_continue():
            what_progress = input('Вывести все задачи или только невыполненные? в - все, н - невыполненные ---> ')
            if what_progress == 'в':
                get_dict(toDoList)
            else:
                get_dict(toDoList, progress='Не выполнено')
            break




main()