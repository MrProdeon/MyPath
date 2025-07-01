import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

quantity = int(input("Количество паролей для генерации "))
lenght = int(input("Длина одного пароля "))
digit_in = input("Включать ли цифры 0123456789 ? ")
uppercase_in = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ")
lowercase_in = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? ")
punctuation_in = input("Включать ли символы !#$%&*+-=?@^_ ? ")
different_in = input("Исключать ли неоднозначные символы il1Lo0O ? ")


if digit_in.lower() == "да":
    chars += digits
if uppercase_in.lower() == "да":
    chars += uppercase_letters
if lowercase_in.lower() == "да":
    chars += lowercase_letters
if punctuation_in.lower() == "да":
    chars += punctuation
if different_in == "да":
    chars = (
        chars.replace("i", "")
        .replace("l", "")
        .replace("1", "")
        .replace("L", "")
        .replace("o", "")
        .replace("0", "")
        .replace("O", "")
    )


def generate_password(chars, lenght):
   return ''.join(random.sample(chars, lenght))


for _ in range(quantity):
    print(generate_password(chars, lenght))
