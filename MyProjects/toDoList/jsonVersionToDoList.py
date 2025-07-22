import json
import math

basic_met_list = list()
bodyfat_list = list()
calories_per_day = list()
macros_list = list()
target_list = list()


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


def get_calories_for_train(part, tonnage, press_sets, rest_time, sets, walk_speed):
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
    daily_activity = input('Много ли сегодня было бытовой активности ? 1 - мало (Практически весь день сидеть или лежать, редкая ходьба)\n2 - средне (Ходьба по дому, уборка, готовка в обычном темпе)\n3 - много (Большая активность по дому, генеральная уборка, перетаскивание вещей...)')
    while daily_activity not in ('1', '2', '3'):
        daily_activity = input('Много ли сегодня было бытовой активности ? 1 - мало, 2 - средне, 3 - много')
    return level_activity[daily_activity]


def get_eated_calories(eated_calories):
    """Функция для приема информации о количестве съеденных калорий"""
    return eated_calories


def get_macros(weight, func_per_day):
    """Функция для расчета БЖУ. Для всех целей выбрано одинаковое значение:
    2гр белка на 1кг веса тела и 1гр жира на 1кг веса тела"""
    protein = weight * 2
    protein_calories = protein * 4
    fat = 1 * weight
    fat_calories = fat * 9
    carbs_calories = func_per_day() - protein_calories - fat_calories
    carbs = carbs_calories / 4
    macros_list.append(f'Белки - {protein}, Жиры - {fat}, Углеводы - {carbs}')
    return f'Белки - {protein}, Жиры - {fat}, Углеводы - {carbs}'

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


def main():
    global basic_met_list, bodyfat_list, calories_per_day, macros_list, target_list

    basic_met_list = load_changes('basic_met.txt')
    bodyfat_list = load_changes('bodyfat.txt')
    calories_per_day = load_changes('ccals_per_day.txt')
    macros_list = load_changes('macros.txt')
    target_list = load_changes('target.txt')

    what_want = input('Необходимо рассчитать полностью всё сначала или просто рассчитать потраченные калории и цель за день?\n1 - рассчитать всё с самого начала\n2 - рассчитать калории и цель на день\n---> ')
    while what_want not in ('1', '2'):
        what_want = input('Формат входных данных : \n1 - рассчитать всё с самого начала\n2 - рассчитать калории и цель на день\n---> ')
    if what_want == '1':
        #Рассчет базового обмена
        print('Для начала рассчитаем базовый обмен веществ.')
        # Пол
        while (gender := input('Введите ваш пол: м или ж ---> ')) not in ('м', 'ж'):
            print('Неверный ввод. Попробуйте снова. м или ж ---> ')
        # Возраст
        age = input('Введите ваш возраст ---> ')
        try:
            age = int(age)
        except ValueError:
            while True:
                age = input('Введите ваш возраст. Допустимы только целые числа. ---> ')
                try:
                    age = int(age)
                    break
                except ValueError:
                    continue
        # Рост
        height = input('Введите ваш рост ---> ')
        try:
            height = int(height)
        except ValueError:
            while True:
                height = input('Введите ваш рост. Допустимы только целые числа. ---> ')
                try:
                    height = int(height)
                    break
                except ValueError:
                    continue

        # Вес
        weight = input('Введите ваш вес ---> ')
        try:
            weight = int(weight)
        except ValueError:
            while True:
                weight = input('Введите ваш вес. Допустимы только целые числа. ---> ')
                try:
                    weight = int(weight)
                    break
                except ValueError:
                    continue

        get_bmr(gender, age, height, weight)
        save_changes(basic_met_list, 'basic_met.txt')
        print(load_changes('basic_met.txt'))

        #Процент жира
        print('Теперь необходимо рассчитать процент жира.')
        #Шея
        neck = input('Введите обхват шеи в сантиметрах --->')
        try:
            neck = float(neck)
        except ValueError:
            while True:
                neck = input('Введите обхват шеи в сантиметрах. Допускаются только числа и числа с плавающей точкой. --->')
                try:
                    neck = float(neck)
                    break
                except ValueError:
                    continue
        #Талия
        waist = input('Введите обхват талии в сантиметрах --->')
        try:
            waist = float(waist)
        except ValueError:
            while True:
                waist = input('Введите обхват талии в сантиметрах. Допускаются только целые числа и числа с плавающей точкой. --->')
                try:
                    waist = float(waist)
                    break
                except ValueError:
                    continue
        #Обхват бёдер
        hip = input('Введите обхват бёдер в сантиметрах --->')
        try:
            hip = float(hip)
        except ValueError:
            while True:
                hip = input(
                    'Введите обхват бёдер в сантиметрах. Допускаются только целые числа и числа с плавающей точкой. --->')
                try:
                    waist = float(hip)
                    break
                except ValueError:
                    continue

        get_bfp(gender, height, weight, neck, waist, hip)
        save_changes(bodyfat_list, 'bodyfat.txt')




main()
