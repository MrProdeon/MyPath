direction = input('''Хотите шифровать или дешифровать?
Ш - если шифровать
Д - если дешифровать
-> ''').upper()

while 'Ш' not in direction  and "Д" not in direction:
    print('''Ш - если шифровать
Д - если дешифровать
Другие ответы не принимаются!
-> ''')
    direction = input().upper()

language = input('Введите язык алфавита. Р - если русский. А - если английский -> ').upper()
while language != 'Р' and language != 'А':
    print('''Р - русский
А - Английский
Другие ответы не принимаются!
-> ''')
    language = input().upper()

k = input('Введите целое число, которое будет являться шагом сдвига -> ')
while not k.isdigit():
    print('На вход принимается только целое число!')
    k = input('-> ')
k = int(k)

text = input('Введите текст, к которому будет применен Шифр Цезаря ')

rus_alphabet_lowers = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_alphabet_uppers = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
eng_alphabet_lowers = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = '!#$%&*+-=?@"^_,. '


def caesar(direction, language, k, text):
    result = ''
    if direction == 'Ш':
        if language == 'Р':
            for char in text:
                if char.isupper():
                    current_index = rus_alphabet_uppers.index(char)
                    shift_index = (current_index + k) % 32
                    result += rus_alphabet_uppers[shift_index]
                if char.islower():
                    current_index = rus_alphabet_lowers.index(char)
                    shift_index = (current_index + k) % 32
                    result += rus_alphabet_lowers[shift_index]
                if char in symbols:
                    result += symbols[symbols.index(char)]


        if language == 'А':
            for char in text:
                if char.isupper():
                    current_index = eng_alphabet_uppers.index(char)
                    shift_index = (current_index + k) % 26
                    result += eng_alphabet_uppers[shift_index]
                if char.islower():
                    current_index = eng_alphabet_lowers.index(char)
                    shift_index = (current_index + k) % 26
                    result += eng_alphabet_lowers[shift_index]
                if char in symbols:
                    result += symbols[symbols.index(char)]

    if direction == 'Д':
        if language == 'Р':
            for char in text:
                if char.isupper():
                    current_index = rus_alphabet_uppers.index(char)
                    shift_index = (current_index - k) % 32
                    result += rus_alphabet_uppers[shift_index]
                if char.islower():
                    current_index = rus_alphabet_lowers.index(char)
                    shift_index = (current_index - k) % 32
                    result += rus_alphabet_lowers[shift_index]
                if char in symbols:
                    result += symbols[symbols.index(char)]

        if language == 'А':
            for char in text:
                if char.isupper():
                    current_index = eng_alphabet_uppers.index(char)
                    shift_index = (current_index - k) % 26
                    result += eng_alphabet_uppers[shift_index]
                if char.islower():
                    current_index = eng_alphabet_lowers.index(char)
                    shift_index = (current_index - k) % 26
                    result += eng_alphabet_lowers[shift_index]
                if char in symbols:
                    result += symbols[symbols.index(char)]

    return result

rs = caesar(direction, language, k, text)
print(rs)   