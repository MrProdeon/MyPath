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

def get_tasks_by_progress(task_list : list, progress : str = None) -> list:
    if progress is None:
        return task_list
    return [task for task in task_list if task.get('Прогресс') == progress]

def print_tasks(task_list: list) -> None:
    """Выводит задачи в консоль"""
    for i, task in enumerate(task_list, 1):
        status = '✅' if task['Прогресс'] == 'Выполнено' else '❌'
        print(f"[{i}] {status} {task['Дело']} (до {task['Время']}) [пометка: {task['Пометка']}]")




def main() -> None:
    while True:
        case : str = input('Введите ваше дело : ')
        time : str = input('До какого времени выполнить (Синтаксис = 01.01.2001 ) : ')
        tag : str = input('Введите пометку, если требуется : ')
        add_a_case(get_case(case, time, tag))




        if not end_or_continue():
            what_progress = input('Вывести все задачи или только невыполненные? в - все, н - невыполненные ---> ')
            if what_progress == 'в':
                tasks = get_tasks_by_progress(toDoList)
            elif what_progress == 'н':
                tasks = get_tasks_by_progress(toDoList, progress='Не выполнено')
            else:
                print('Неверный ввод.')
                tasks = []

            print_tasks(tasks)
            break




main()