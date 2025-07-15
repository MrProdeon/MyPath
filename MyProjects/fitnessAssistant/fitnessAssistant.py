#Проект на стадии разработки

import json
import math

basic_met_list = list()
bodyfat_list = list()


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
    steps -
    train -
    digestion -
    daily_activity -
    """


def get_calories_for_steps(steps, weight):
    """Функция для расчета потраченных калорий за шаги"""
    steps_calories = steps * 0.035 *(weight / 70)
    return round(steps_calories, 2)


def get_calories_for_train(part, tonnage, press_sets, rest_time, sets, walk_speed):
    epoc_input = input('Насколько тяжелая была тренировка? 1 - легкая, 2 - тяжелая ---> ')
    epoc = 100 if epoc_input == '2' else 70
    if part in ('грудьбицепс', 'спинатрицепс'):
        k = 0.031
    if part in 'ноги':
        k = 0.034
    calories = (tonnage * k) + (( rest_time * sets * walk_speed) * 0.045) + (press_sets * 6) + epoc

    return calories




def save_changes(collection, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(collection, fp=file, ensure_ascii=False, indent=4, )
