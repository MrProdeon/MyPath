#Функция для быстрого форматирования айди платежей, которые необходимо перевести в ошибку

def formatting_id_for_cancelling():
    print('''Введите все ваши id выплат, после этого нажмите Enter два раза : ''')
    formated_id = []
    while True:
        line = input()
        if line == '':
            break
        formated_id.append(line)
    return formated_id

print(*formatting_id_for_cancelling(), sep=', ')