
# Конспект: Python Advanced Cheatsheet

## 3. Тип данных bool и NoneType

### 3.1 Тип данных bool
- Логические значения: `True`, `False` — подклассы `int`.
- Операции сравнения возвращают `bool`.
- Используется в условиях (`if`, `while`).
- Приведение к `bool`: `bool(0)` → `False`, `bool(1)` → `True`, `bool('')` → `False`, `bool('abc')` → `True`.

```python
x = 5 > 2      # True
flag = bool('')  # False
```

### 3.2 Тип данных NoneType
- Только одно значение: `None`.
- Обозначает «ничего», отсутствие значения.
- Возвращается функциями без оператора `return`.

```python
def f():
    pass

result = f()  # None
```

---

## 4. Вложенные списки и матрицы

### 4.1 Повторение списков
- Методы списков: `.append()`, `.remove()`, `.pop()`, `.insert()`, `.index()`, `.count()`, `.sort()`, `.reverse()`
- Перебор списка, срезы, генераторы списков.

```python
fruits = ["apple", "banana"]
fruits.append("orange")
```

### 4.2 Вложенные списки. Часть 1
- Список внутри списка: `[[1, 2], [3, 4]]`
- Доступ по индексу: `a[1][0]`
- Перебор вложенных списков:

```python
for row in matrix:
    for item in row:
        print(item)
```

### 4.3 Вложенные списки. Часть 2
- Создание таблиц с `list comprehension`

```python
n = 3
matrix = [[0 for _ in range(n)] for _ in range(n)]
```

### 4.4 Матрицы. Часть 1
- Матрицы = вложенные списки
- Работа с диагоналями, строками, столбцами

```python
main_diag = [matrix[i][i] for i in range(n)]
```

### 4.5 Матрицы. Часть 2
- Преобразование строк в матрицу

```python
matrix = [list(map(int, input().split())) for _ in range(n)]
```

### 4.6 Матрицы. Часть 3
- Зеркальное отражение, поворот, транспонирование

```python
transposed = list(zip(*matrix))
```

### 4.7 Операции над матрицами в математике
- Сложение, умножение, вычитание поэлементно

```python
result = [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
```

---

## 6. Кортежи

### 6.1 Введение в кортежи
- Кортежи — неизменяемые списки: `t = (1, 2, 3)`
- Можно: индексировать (`t[0]`), срезать (`t[1:]`), перебирать (`for x in t:`), распаковывать (`a, b = t[:2]`), объединять (`t1 + t2`)
- Методы кортежей: `.count(x)`, `.index(x)`
- Нельзя: изменять элементы, использовать `.append()`, `.remove()` и другие методы изменения

```python
t = (1, 2, 3)
a, b, c = t
print(t[1])  # 2
print(t[1:]) # (2, 3)
for item in t:
    print(item)
```

### 6.2 Основы работы с кортежами. Часть 1
- Методы кортежей: `.count(x)`, `.index(x)`
- Преобразование списков и кортежей: `tuple(list)` и `list(tuple)`

```python
t = (1, 2, 2, 3)
print(t.count(2))  # 2
print(t.index(3))  # 3
```

### 6.3 Основы работы с кортежами. Часть 2
- Можно использовать в качестве ключей словаря (если элементы кортежа тоже хешируемы)
- Можно создавать кортежи с элементами разных типов

```python
d = {(1, 2): "point"}
print(d[(1, 2)])

mixed = (1, "two", 3.0, [4, 5])
print(mixed)
```

---

## 8. Множества

### 8.1 Множества в математике
- Уникальные, неупорядоченные элементы
- Операции: объединение (`|`), пересечение (`&`), разность (`-`), симм. разность (`^`)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}
```

### 8.2 Диаграммы Эйлера–Венна
- Теоретические пояснения: объединение, пересечение, подмножества

### 8.3 Введение в множества в Python
- Создание: `set()`, `{1, 2}`
- Автоматически убирают дубликаты

```python
s = set([1, 2, 2, 3])  # {1, 2, 3}
```

### 8.4 Основы работы с множествами
- Проверка принадлежности: `in`
- Перебор: `for x in s:`

```python
if 3 in s:
    print("Есть 3")
```

### 8.5 Методы множеств. Часть 1
- `add()`: добавляет элемент в множество
- `remove()`: удаляет элемент, вызывает ошибку, если элемента нет
- `discard()`: удаляет элемент, не вызывает ошибку, если элемента нет
- `clear()`: очищает множество
- `copy()`: создает поверхностную копию множества

```python
s = {1, 2, 3}
s.add(10)         # Добавляет 10
s.remove(2)       # Удаляет 2
s.discard(5)      # Пытается удалить 5, ошибки нет
s.clear()         # Очищает множество
s2 = s.copy()     # Копия множества
```

### 8.6 Методы множеств. Часть 2
- `union()`: возвращает объединение множеств (`|`)
- `intersection()`: пересечение (`&`)
- `difference()`: разность (`-`)
- `symmetric_difference()`: симметрическая разность (`^`)

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))                # {1, 2, 3, 4}
print(a.intersection(b))         # {2, 3}
print(a.difference(b))           # {1}
print(a.symmetric_difference(b))# {1, 4}
```

### 8.7 Методы множеств. Часть 3
- `issubset()`: проверяет, является ли множество подмножеством другого
- `issuperset()`: проверяет, является ли множество надмножеством другого
- `isdisjoint()`: проверяет, есть ли пересечения множеств

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))     # True
print(b.issuperset(a))   # True
print(a.isdisjoint({4})) # True
```

### 8.8 Генераторы и frozenset
- Генераторы множеств: `{x for x in range(5)}`
- `frozenset` — неизменяемое множество

```python
fs = frozenset([1, 2, 3])
```

---

## 10. Словари

### 10.1 Введение в словари в Python
- Хранят пары ключ-значение
- Ключи должны быть хешируемыми (строки, числа, кортежи)
- Значения могут быть любыми

```python
d = {"key": "value", 10: [1, 2, 3]}
```

### 10.2 Основы работы со словарями
- Обращение по ключу: `d[key]`
- Добавление и изменение: `d[new_key] = value`
- Удаление: `del d[key]`
- Перебор ключей, значений, пар

```python
for key in d:
    print(key, d[key])
for key, value in d.items():
    print(key, value)
```

### 10.3 Методы словарей
- `.get(key, default)`: получить значение или `default`, если ключа нет
- `.keys()`: возвращает ключи
- `.values()`: возвращает значения
- `.items()`: возвращает пары ключ-значение
- `.pop(key)`: удаляет ключ и возвращает значение
- `.update(other_dict)`: добавляет пары из другого словаря

```python
print(d.get("key", "нет"))  
keys = d.keys()
values = d.values()
items = d.items()
val = d.pop("key")
d.update({"new": 123})
```

### 10.4 Задачи на словари
- Решение задач с использованием словарей, подсчет частот, группировка

### 10.5 Вложенные словари и генераторы словарей
- Словари в словарях
- Генераторы словарей

```python
nested = {"outer": {"inner": 1}}
gen = {k: v*2 for k, v in d.items()}
```

---

## 12. Модули random и string

### 12.1 Модуль random. Часть 1
- Генерация случайных чисел: `random.random()`, `random.randint(a, b)`
- Перемешивание списка: `random.shuffle(list)`

```python
import random
print(random.random())      # 0.0 - 1.0
print(random.randint(1, 10))# 1 - 10
lst = [1,2,3]
random.shuffle(lst)
```

### 12.2 Модуль random. Часть 2
- Выбор случайного элемента: `random.choice(seq)`
- Генерация выборки без повторений: `random.sample(seq, k)`

```python
print(random.choice(lst))
print(random.sample(lst, 2))
```

### 12.3 Метод Монте-Карло и Bogosort
- Монте-Карло: метод статистического моделирования (теоретически)
- Bogosort: шуточный метод сортировки (перемешивание пока отсортирован)

---

## 13. Модули decimal, fraction и complex

### 13.1 Модуль decimal
- Работа с десятичными числами с фиксированной точностью

```python
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)  # 0.3
```

### 13.2 Модуль fractions
- Работа с рациональными числами (дробями)

```python
from fractions import Fraction
f = Fraction(1, 3)
print(f + Fraction(1, 6))  # 1/2
```

### 13.3 Тип данных complex
- Комплексные числа: `3 + 4j`

```python
z = 3 + 4j
print(abs(z))  # 5.0
```

---

## 14. Модуль turtle

### 14.1 Модуль черепашки. Часть 1
- Рисование с помощью черепашки

```python
import turtle
t = turtle.Turtle()
t.forward(100)
```

### 14.2 Модуль черепашки. Часть 2
- Продвинутые команды, циклы

### 14.3 Модуль черепашки. Часть 3

---

## 15. Функции

### 15.1 Необязательные и именованные аргументы
- Можно задавать значения по умолчанию
- Именованные аргументы при вызове

```python
def f(a, b=2):
    return a + b

print(f(1))      # 3
print(f(1, b=3)) # 4
```

### 15.2 Функции с переменным количеством аргументов
- `*args`, `**kwargs`

```python
def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, x=3)
```
# 15.3 Парадигмы программирования
- Императивное программирование: пошаговое выполнение инструкций
- Объектно-ориентированное программирование (ООП): объекты, классы, наследование
- Функциональное программирование: функции как объекты, отсутствие побочных эффектов

## 15.4 Функции как объекты
- Функции можно присваивать переменным
- Можно передавать функции как аргументы другим функциям
- Функции могут возвращать другие функции

```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # присваивание функции переменной
print(say_hello("Alice"))

def apply_func(func, value):
    return func(value)

print(apply_func(greet, "Bob"))
```

## 15.5 Функции высшего порядка
- Функции, принимающие функции в аргументы или возвращающие функции

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))  # 15
```

## 15.6 Встроенные функции map(), filter(), reduce()
- `map(func, iterable)` — применяет func к каждому элементу iterable и возвращает итератор с результатами
- `filter(func, iterable)` — возвращает итератор из элементов iterable, для которых func возвращает True
- `reduce(func, iterable)` — применяет функцию func последовательно к элементам iterable, сводя их к одному значению (нужно импортировать из functools)

```python
from functools import reduce

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda a, b: a + b, nums)

print(squared)  # [1, 4, 9, 16]
print(evens)    # [2, 4]
print(sum_all)  # 10
```

## 15.7 Анонимные функции. Часть 1
- `lambda` — создание анонимных (безымянных) функций

```python
add = lambda x, y: x + y
print(add(3, 4))  # 7
```

## 15.8 Анонимные функции. Часть 2
- Использование lambda с функциями высшего порядка, сортировкой, фильтрацией

```python
nums = [1, 2, 3, 4]
print(sorted(nums, key=lambda x: -x))  # [4, 3, 2, 1]
```

## 15.9 Встроенные функции any(), all(), zip(), enumerate()
- `any(iterable)` — True, если хотя бы один элемент истинен
- `all(iterable)` — True, если все элементы истинны
- `zip(*iterables)` — объединяет несколько итерируемых в кортежи по элементам
- `enumerate(iterable, start=0)` — возвращает пары (индекс, элемент)

```python
print(any([False, True, False]))  # True
print(all([True, True, False]))   # False

a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))            # [(1, 'a'), (2, 'b'), (3, 'c')]

for i, val in enumerate(['x', 'y', 'z'], start=1):
    print(i, val)
```

## 17. Работа с файлами

### 17.1 Файловый ввод и вывод
- Открытие файла: `open(filename, mode)`
- Режимы: `'r'` — чтение, `'w'` — запись (перезапись), `'a'` — добавление, `'b'` — бинарный режим
- Обязательно закрывать файл (`file.close()`) или использовать `with`

```python
with open("file.txt", "w") as f:
    f.write("Hello, file!
")
```

### 17.2 Работа с текстовыми файлами. Часть 1
- Чтение строк: `read()`, `readline()`, `readlines()`
- Запись строк: `write()`, `writelines()`

```python
with open("file.txt", "r") as f:
    content = f.read()
print(content)
```

### 17.3 Работа с текстовыми файлами. Часть 2
- Чтение файла построчно через цикл

```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### 17.4 Работа с текстовыми файлами. Часть 3
- Работа с кодировками: параметр `encoding` в `open()`

```python
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()
```