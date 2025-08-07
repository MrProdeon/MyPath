import json

target_capital = 1500000
bonds = dict()
stocks = dict()
capital = [100000, 110000]

def add_bonds(name_bond : str, payment_date: str):
    """Добавление данных об облигациях в словарь"""
    bonds[name_bond] = bonds.get(name_bond, payment_date)


def add_stocks(name_stock : str, payment_date: str):
    """Добавление данных об акциях в словарь"""
    bonds[name_stock] = bonds.get(name_stock, payment_date)


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
        percent_increase = increase / capital[-2] * 100
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


def save_changes(collection, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(collection, fp=file ,ensure_ascii=False ,indent=4)


def main():
    global target_capital, bonds, stocks, capital

    target_capital = load_changes('target_capital.txt')
    bonds = load_changes('bonds.txt')
    stocks = load_changes('stocks.txt')
    capital = load_changes('capital.txt')

    what_to_do = input('''
Что вы хотите сделать?
1 - добавить данные об активах
2 - просмотреть нынешние активы
3 - внести изменения в активы 
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

#Остановился на проблеме, что при загрузке файла он вернет список, но у меня метод гет должен работать со словарями
#Написал добавление данных в словарь

