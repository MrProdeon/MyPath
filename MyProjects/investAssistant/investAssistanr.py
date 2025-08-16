import json
from sys import base_prefix
from time import perf_counter

target_capital = 1500000
bonds = dict()
stocks = dict()
capital = list()

def add_bonds(name_bond : str, payment_date: str):
    """Добавление данных об облигациях в словарь"""
    bonds[name_bond] = bonds.get(name_bond, payment_date)


def add_stocks(name_stock : str, payment_date: str):
    """Добавление данных об акциях в словарь"""
    stocks[name_stock] = bonds.get(name_stock, payment_date)


def delete_asset(var_name : dict, asset_name : str):
    """Удаление актива"""
    del var_name[asset_name]


def add_new_capital(total_capital):
    """Функция для добавления нового значения капитала"""
    capital.append(total_capital)


def capital_increase():
    """Подсчет увеличения капитала. Вернет сумму увеличения и процентное соотношение увеличения"""
    global capital
    if len(capital) >= 2:
        increase = capital[-1] - capital[-2]
        percent_increase = round(increase / capital[-2] * 100, 2)
        return increase, percent_increase
    return 'Пока что посчитать увеличение нельзя, так как всего одно значение в списке.'


def set_change(var_name, asset_name):
    if var_name.get(asset_name):
        var_name[asset_name] = input('Введите необходимое изменение даты и величины купона. ---> ')


def change_currency(currency, capital):
    if currency == 'евро':
        return capital[-1] * 93
    return capital[-1] * 80


def load_changes(filename):
    try:
        with open(filename,'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def load_dict_changes(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return dict()
    except json.JSONDecodeError:
        return dict()


def save_changes(collection, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(collection, fp=file ,ensure_ascii=False ,indent=4)


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
    global target_capital, bonds, stocks, capital


while True:
    target_capital = load_changes('target_capital.txt')
    bonds = load_dict_changes('bonds.txt')
    stocks = load_dict_changes('stocks.txt')
    capital = load_changes('capital.txt')
    what_to_do = input('''
Что вы хотите сделать?
1 - добавить данные об активах
2 - просмотреть нынешние активы
3 - внести изменения в активы
4 - добавить нынешний капитал
5 - просмотреть текущий капитал
6 - просмотр увеличеняи капитала
7 - просмотр капитала в разных валютах
''')
    while what_to_do not in ('1', '2', '3', '4', '5', '6', '7'):
        what_to_do = input('''
Что вы хотите сделать?
1 - добавить данные об активах
2 - просмотреть нынешние активы
3 - внести изменения в активы
4 - добавить нынешний капитал
5 - просмотреть текущий капитал
6 - просмотр увеличеняи капитала
7 - просмотр капитала в разных валютах
''')
    if what_to_do == '1':
        while True:
            bonds_or_stocks = input('Вы хотите добавить акции или облигации? а - акции, о - облигации ---> ').lower()
            while bonds_or_stocks not in ('а', 'о'):
                bonds_or_stocks = input('Вы хотите добавить акции или облигации? а - акции, о - облигации ---> ').lower()

            while True:
                if bonds_or_stocks == 'о':
                    name_bond = input('Введите название облигации ---> ')
                    payment_date = input('Введите дату получения купона ---> ')
                    add_bonds(name_bond, payment_date)
                    save_changes(bonds, 'bonds.txt')
                    more = input('Хотите добавить ещё облигацию? д - да, н - нет ---> ')
                    while more not in ('д', 'н'):
                        more = input('Хотите добавить ещё облигацию? д - да, н - нет ---> ')
                    if more == 'д':
                        continue
                    break

                elif bonds_or_stocks == 'а':
                    name_stock = input('Введите название акции ---> ')
                    payment_date = input('Введите дату получения дивиденда---> ')
                    add_stocks(name_stock, payment_date)
                    save_changes(stocks, 'stocks.txt')
                    more = input('Хотите добавить ещё акцию? д - да, н - нет ---> ')
                    while more not in ('д', 'н'):
                        more = input('Хотите добавить ещё акцию? д - да, н - нет ---> ')
                    if more == 'д':
                        continue
                    break
            add_more_assets = input('Хотите добавить ещё какой-то инструмент? д - да , н - нет ---> ')
            while add_more_assets not in ('д', 'н'):
                add_more_assets = input('Хотите добавить ещё акцию? д - да, н - нет ---> ')
            if add_more_assets == 'д':
                continue
            break

    if what_to_do == '2':
        print('Облигации : ')
        for key, value in bonds.items():
            print(f'{key}, дата купона - {value}')
        print('Акции : ')
        for key_value in stocks.items():
            print(f'{key}, дата дивидендов - {value}')

    if what_to_do == '3':
        what_change = input('Что хотите сделать? 1 - внести изменения 2 - удалить актив ---> ')
        while what_change not in ('1', '2'):
            what_change = input('Что хотите сделать? 1 - внести изменения 2 - удалить актив ---> ')
        if what_change == '1':
            asset = input('В какой актив внести изменения? а - акции, о - облигации ---> ')
            while asset not in ('а', 'о'):
                asset = input('В какой актив внести изменения? а - акции, о - облигации ---> ')
            if asset == 'а':
                asset_name = input('Введите название акции для изменения ---> ')
                set_change(stocks, asset_name)
                save_changes(stocks, 'stocks.txt')
            if asset == 'о':
                asset_name = input('Введите название облигации для изменения ---> ')
                set_change(bonds, asset_name)
                save_changes(bonds, 'bonds.txt')
        if what_change == '2':
            asset = input('В какой актив внести изменения? а - акции, о - облигации ---> ')
            while asset not in ('а', 'о'):
                asset = input('В какой актив внести изменения? а - акции, о - облигации ---> ')
            if asset == 'а':
                asset_name = input('Введите название акции для изменения ---> ')
                if asset_name not in stocks.keys():
                    print('Такой акции у вас нет.')
                else:
                    delete_asset(stocks, asset_name)
                    save_changes(stocks, 'stocks.txt')
            if asset == 'о':
                asset_name = input('Введите название облигации для изменения ---> ')
                if asset_name not in bonds.keys():
                    print('Такой облигации у вас нет.')
                else:
                    delete_asset(bonds, asset_name)
                    save_changes(bonds, 'bonds.txt')
    if what_to_do == '4':
        now_capital = input('Введите ваш текущий капитал ---> ')
        now_capital = check_number_or_string(now_capital)
        add_new_capital(now_capital)
        save_changes(capital, 'capital.txt')

    if what_to_do == '5':
        print(capital[-1])

    if what_to_do == '6':
        now_sum, percent = capital_increase()
        print(f'Нынешняя сумма - {capital[-1]}')
        print(f'Увеличение суммы - {now_sum}')
        print(f'Процент увеличения - {percent}')

    elif what_to_do == '7':
        print(f'Сумма в рублях - {capital[-1]}')
        print(f'Сумма в долларах - {change_currency('доллар', capital)}')
        print(f'Сумма в евро - {change_currency('евро', capital)}')

    what_more = input('Хотите ли вы ещё что-то сделать? д - да, н - нет ---> ').lower()
    if what_more == 'д':
        continue
    break


main()

def change_currency(currency, capital):
    if currency == 'евро':
        return capital[-1] * 93
    return capital[-1] * 80