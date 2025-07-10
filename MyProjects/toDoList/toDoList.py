# Проект на стадии разработки

toDoList = []
next_id = 0

def get_case(case, time, tag, progress = 'Не выполнено') -> dict:
    """Получение данных от пользователя о его делах"""
    global next_id
    next_id += 1
    return {'id' : next_id,'Дело' : case, 'Время' : time, 'Пометка' : tag, 'Прогресс' : progress}


def add_a_case(case) -> None:
    """Добавление дел в список"""
    toDoList.append(case)


def get_tasks_by_progress(task_list : list, progress : str = None) -> list:
    """Получение всех задач если None
    Получение только невыполненных задач если Progress = 'Не выполнена' """
    if progress is None:
        return task_list

    return [task for task in task_list if task.get('Прогресс') == progress]


def print_tasks(task_list: list) -> None:
    """Выводит задачи в консоль"""
    for task in task_list:
        status = '✅' if task['Прогресс'] == 'Выполнено' else '❌'
        print(f"[{task['id']}] {status} {task['Дело']} (до {task['Время']}) [пометка: {task['Пометка']}]")


def end_or_continue() -> bool:
    """Уточнение у пользователя нужно ли добавить ещё задачи"""
    answer = input('Хотите ещё добавить задачу ? д если да, н если нет ---> ')
    while answer not in ('д', 'н'):
        answer = input('Неверный формат ввода. д если да, н если нет ---> ')
    return answer == 'д'



def mark_done(todolist, task_id):
    for task in todolist:
        if task.get('id') == task_id:
            task['Прогресс'] = 'Выполнено'
            print(f'Задача с id = {task_id} помечена выполненной')
            return
    print(f"Задача с id={task_id} не найдена.")



def main() -> None:
    """Основная функция, которая собирает результаты выполнения остальных и выводит результат"""
    while True:
        case : str = input('Введите ваше дело : ')
        time : str = input('До какого времени выполнить (Синтаксис = 01.01.2001 ) : ')
        tag : str = input('Введите пометку, если требуется : ')
        add_a_case(get_case(case, time, tag))

        if not end_or_continue():

            what_progress = input('Вывести все задачи, только завершенные или только невыполненные в - все, н - невыполненные, з - завершенные ---> ')
            if what_progress == 'в':
                tasks = get_tasks_by_progress(toDoList)
            elif what_progress == 'н':
                tasks = get_tasks_by_progress(toDoList, progress='Не выполнено')
            elif what_progress == 'з':
                tasks = get_tasks_by_progress(toDoList, progress='Выполнено')
            else:
                print('Неверный ввод.')
                tasks = []

            print_tasks(tasks)

            mark = input('Хотите отметить какую-то задачу как выполненную? д если да, н если нет ---> ')
            while mark not in ('д', 'н'):
                mark = input('Хотите отметить какую-то задачу как выполненную? д если да, н если нет ---> ')
            if mark == 'д':
                try:
                    task_id = int(input('Введите id вашей задачи ---> '))
                    mark_done(toDoList, task_id)
                except ValueError as error:
                    print(f'Ошибка {error} - id должен быть числом')

            print('Обновлённый список задач: ')
            print_tasks(tasks)
            break


main()