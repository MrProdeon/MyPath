import json
import math

basic_met_list = list()
bodyfat_list = list()
calories_per_day = list()
macros_list = list()
target_list = list()
bmr_list = list()
global_weight = list()

def get_bmr(gender : str, age : int, height : int | float, weight : int | float) -> int | float:
    """Функция для расчета базового обмена веществ"""
    if gender.lower() in 'м':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() in 'ж':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    basic_met_list.append(bmr)
    return round(bmr, 2)


def get_bfp(gender, height, weight, neck, waist, hip):
    """
    Функция для расчета процента жира
    height - рост
    weight - вес
    neck - шея
    waist - талия
    hip - обхват бёдер
    """
    if gender == 'м':
        bodyfat = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    elif gender == 'ж':
        bodyfat = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450
    bodyfat_list.append(bodyfat)
    return int(bodyfat)


def calories_spent_per_day(bmr, steps, train, digestion, daily_activity):
    """
    Функция для расчета потраченных калорий за день
    bmr - базовый обмен
    steps - шаги
    train - тренировка
    digestion - переваривание
    daily_activity - бытовая активность
    """
    total = bmr
    total += sum([steps, train, digestion, daily_activity])
    calories_per_day.append(total)
    return total


def get_calories_for_steps(steps, weight):
    """Функция для расчета потраченных калорий за шаги"""
    steps_calories = steps * 0.035 *(weight / 70)
    return round(steps_calories, 2)


def get_calories_for_train(part, tonnage, press_sets, rest_time, sets, walk_speed=3):
    """Функция для расчета потраченных калорий за тренировку"""
    epoc_input = input('Насколько тяжелая была тренировка? 1 - легкая, 2 - тяжелая ---> ')
    while epoc_input not in ('1', '2'):
        epoc_input = input('Насколько тяжелая была тренировка? 1 - легкая, 2 - тяжелая ---> ')
    epoc = 100 if epoc_input == '2' else 70
    if part in ('грудьбицепс', 'спинатрицепс'):
        k = 0.031
    if part in 'ноги':
        k = 0.034
    calories = (tonnage * k) + (( rest_time * sets * walk_speed) * 0.045) + (press_sets * 6) + epoc

    return calories

def get_digestion(eat_calories):
    """Функция для расчета потраченных калорий на переваривание пищи"""
    return eat_calories * 0.10

def get_daily_activity():
    """Функция для примерного расчета бытовой активности."""
    level_activity = {'1' : 150, '2' : 300, '3' : 550}
    daily_activity = input('🔽\nМного ли сегодня было бытовой активности ? 1 - мало (Практически весь день сидеть или лежать, редкая ходьба)\n2 - средне (Ходьба по дому, уборка, готовка в обычном темпе)\n3 - много (Большая активность по дому, генеральная уборка, перетаскивание вещей...)\n---> ')
    while daily_activity not in ('1', '2', '3'):
        daily_activity = input('Много ли сегодня было бытовой активности ? 1 - мало, 2 - средне, 3 - много')
    return level_activity[daily_activity]


def get_macros(weight, func_per_day):
    """Функция для расчета БЖУ. Для всех целей выбрано одинаковое значение:
    2гр белка на 1кг веса тела и 1гр жира на 1кг веса тела"""
    protein = weight * 2
    protein_calories = protein * 4
    fat = 1 * weight
    fat_calories = fat * 9
    carbs_calories = func_per_day - protein_calories - fat_calories
    carbs = carbs_calories / 4
    macros_str = f'Белки - {protein}, Жиры - {fat}, Углеводы - {carbs}'
    macros_list.append(macros_str)
    return macros_str

def get_tarder_calories(func_calories_per_day):
    """Функция для расчета дефицита и профицита"""
    target_list.append(f'Для дефицита калорий необходимо съесть - {func_calories_per_day - 500}\nДля профицита калорий необходимо съесть - {func_calories_per_day + 300}')
    return f'Для дефицита калорий необходимо съесть - {func_calories_per_day - 500}\nДля профицита калорий необходимо съесть - {func_calories_per_day + 300}'


def save_changes(collection, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(collection, fp=file, ensure_ascii=False, indent=4, )


def load_changes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def check_number_or_string(value):
    try:
        value = float(value)
    except ValueError:
        while True:
            value = input('Для ввода допускаются только числа. ---> ')
            try:
                value = float(value)
                break
            except ValueError:
                continue
    return value


def main():
    global basic_met_list, bodyfat_list, calories_per_day, macros_list, target_list, bmr_list, global_weight

    basic_met_list = load_changes('basic_met.txt')
    bodyfat_list = load_changes('bodyfat.txt')
    calories_per_day = load_changes('calories_per_day.txt')
    macros_list = load_changes('macros.txt')
    target_list = load_changes('target.txt')
    bmr_list = load_changes('bmr.txt')
    global_weight = load_changes('weight.txt')


    what_want = input('Необходимо рассчитать полностью всё сначала или просто рассчитать потраченные калории и цель за день?\n1 - рассчитать всё с самого начала\n2 - рассчитать калории и цель на день\n---> ')
    while what_want not in ('1', '2'):
        what_want = input('Формат входных данных : \n1 - рассчитать всё с самого начала\n2 - рассчитать калории и цель на день\n---> ')
    if what_want == '2' and len(global_weight) == 0:
        what_want = '1'
        print('Первый раз нужно обязательно рассчитать всё сначала.')
    if what_want == '1':
        #Рассчет базового обмена
        print('Для начала рассчитаем базовый обмен веществ.')
        # Пол
        while (gender := input('Введите ваш пол: м или ж ---> ')) not in ('м', 'ж'):
            print('Неверный ввод. Попробуйте снова. м или ж ---> ')
        # Возраст
        age = check_number_or_string(input('Введите ваш возраст ---> '))

        # Рост
        height = check_number_or_string(input('Введите ваш рост ---> '))

        # Вес
        weight = check_number_or_string(input('Введите ваш вес ---> '))
        global_weight.append(weight)
        save_changes(global_weight, 'weight.txt')



        bmr = get_bmr(gender, age, height, weight)
        bmr_list.append(bmr)
        save_changes(bmr_list, 'bmr.txt')
        save_changes(basic_met_list, 'basic_met.txt')
        print(f'🔽\nВаш базовый обмен веществ - {load_changes('basic_met.txt')[-1]} калорий.')

        #Расчет процента жира
        print('🔽\nТеперь необходимо рассчитать процент жира.')
        #Шея
        neck = check_number_or_string(input('Введите обхват шеи в сантиметрах ---> '))


        #Талия
        waist = check_number_or_string(input('Введите обхват талии в сантиметрах ---> '))


        #Обхват бёдер
        hip = check_number_or_string(input('Введите обхват бёдер в сантиметрах ---> '))


        get_bfp(gender, height, weight, neck, waist, hip)
        save_changes(bodyfat_list, 'bodyfat.txt')
        print(f'🔽\nВаш процент жира : {bodyfat_list[-1]}')

    print('🔽\nРассчитаем потреченные калории за день :')
    steps = check_number_or_string(input('Сколько сегодня было пройдено шагов? ---> '))
    train_or_not = input('🔽\nБыла ли сегодня тренировка? 1 - если да, 2 - если нет ---> ')
    while train_or_not not in ('1', '2'):
        train_or_not = input('Была ли сегодня тренировка? 1 - если да, 2 - если нет ---> ')
    if train_or_not == '1':
        print('Рассчиатем потраченные калории за тренировку : ')
        part = input('Какие группы мышц сегодня тренировались?\nДопускается ввод: грудьбицепс , спинатрицепс, ноги ---> ')
        while part not in ('грудьбицепс', 'спинатрицепс', 'ноги'):
            part = input('Допускается ввод: грудьбицепс , спинатрицепс, ноги')
        tonnage = check_number_or_string(input('Какой сегодня тоннаж на тренировке? ---> '))
        press_sets = check_number_or_string(input('Сколько было подходов на пресс? ---> '))
        rest_time = check_number_or_string(input('Сколько времени отдыха между подходами ---> '))
        sets = check_number_or_string(input('Сколько подходов ---> '))
        train = get_calories_for_train(part, tonnage, press_sets, rest_time, sets)
        print(f'\nЗа тренировку было потрачено {train} калорий\n')
    if train_or_not == '2':
        train = 0

    print('🔽\nРассчитаем количество калорий, потраченных на переваривание пищи')
    digestion = get_digestion(check_number_or_string(input('Сколько калорий сегодня будет съедено? ---> ')))
    daily_activity = get_daily_activity()
    step_ccals = get_calories_for_steps(steps, global_weight[-1])
    ccals_per_day = calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity)
    save_changes(calories_per_day, 'calories_per_day.txt')
    print(f'За день было потрачено {calories_per_day[-1]} калорий 🔥\n🔽 ')

    # need_macros_or_not = input('Хотите рассчитать БЖУ? 1 - да, 2 - нет ---> ')
    # while need_macros_or_not not in ('1', '2'):
    #     need_macros_or_not = input('Хотите рассчитать БЖУ? 1 - да, 2 - нет ---> ')
    # if need_macros_or_not == '1' and len(global_weight) > 0:
    #     result_macros = get_macros(global_weight[-1], calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity))
    #     save_changes(macros_list, 'macros.txt')
    #     print(f'🔽\n{result_macros}\n')

    print(f'''
✅✅✅
Итог:
Для поддержания необходимо съесть : {calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity)}
БЖУ для поддержания : {get_macros(global_weight[-1], calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity))}
✅✅✅
Для профицита необходимо съесть {calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity) + 300}
БЖУ для профицита : {get_macros(global_weight[-1], calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity) + 300)}
✅✅✅
Для дефицита необходимо съесть {calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity) - 500}
БЖУ для дефицита : {get_macros(global_weight[-1], calories_spent_per_day(bmr_list[-1], step_ccals, train, digestion, daily_activity) - 500)}
✅✅✅
''')







main()
