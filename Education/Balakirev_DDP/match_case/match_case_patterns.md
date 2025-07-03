# Конспект: Конструкция match/case в Python

## Что такое match/case
`match/case` — это конструкция структурного сопоставления, добавленная в Python 3.10. Она позволяет элегантно проверять и распаковывать значения, аналогично `switch` в других языках, но с расширенными возможностями.

Используется для сопоставления значения с различными шаблонами (`patterns`) и выполнения соответствующего блока кода.

---

## Пример базового синтаксиса:
```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something else"
```

---

## Сопоставление с распаковкой кортежей и списков
```python
cmd = ("Автор", "Название", 2000.78)

match cmd:
    case author, title, price:
        print(f"Книга: {author}, {title}, {price}")
    case _:
        print("Формат не распознан")
```
- Работает только если длина соответствует шаблону
- `*_` — для захвата остатка элементов

```python
match cmd:
    case author, title, price, *_:
        print(f"Книга: {author}, {title}, {price}")
```

---

## Проверка типов и условий (guard)
```python
match cmd:
    case [str() as author, str() as title, float() as price, *_] if len(cmd) < 6:
        print("Всё в порядке")
```
- Можно использовать `str()`, `int()` и `float()` для проверки типа
- В `guard` можно добавить дополнительные условия: `if len(title) < 100`

---

## Объединение шаблонов (`|`)
```python
match cmd:
    case (author, title, price) | (_, author, title, price, _):
        print(f"Книга: {author}, {title}, {price}")
```
- Работает, если переменные совпадают по именам

---

## Словари (`dict`)
```python
request = {'url': 'https://example.com', 'method': 'GET'}

match request:
    case {'url': url, 'method': method}:
        print(f"Запрос: {url}, {method}")
```
- Не важен порядок ключей
- Остаточные данные: `**kwargs`

```python
match request:
    case {'url': url, 'method': method, **kwargs} if len(kwargs) <= 2:
        print("Допускается до двух дополнительных параметров")
```

---

## Множества (`set`)
```python
match s:
    case set() as values if len(values) == 3:
        print("Множество из 3 элементов")
```
- Прямое сопоставление через `set()`

---

## Работа с вложенными структурами
```python
json_data = {
    'access': True,
    'info': ['дата', {'email': 'a@b.com'}, True, 1234]
}

match json_data:
    case {'access': access, 'info': [_, {'email': email}, _, _]}:
        print(f"Email: {email}, доступ: {access}")
```

---

## Переменные-константы в case
```python
CMD = 3
cmd = 3

match cmd:
    case CMD:  # Ошибка: воспринимается как новая переменная
        ...
```
### Способы исправления:
1. Использовать атрибут:
```python
class Const:
    CMD_3 = 3

match cmd:
    case Const.CMD_3:
        print("OK")
```
2. Импортировать из модуля:
```python
import consts

match cmd:
    case consts.CMD_3:
        print("OK")
```

---

## Преимущества `match/case`
- Более читаемый и лаконичный код
- Удобная работа с вложенными структурами
- Меньше `if`/`elif`/`else`

> Конструкция `match/case` — мощный инструмент для разборов и фильтрации структурированных данных в Python 3.10+

