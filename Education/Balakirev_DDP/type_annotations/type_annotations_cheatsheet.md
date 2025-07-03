# Конспект: Аннотация типов в Python

## Что такое аннотация типов

Аннотация типов (type hints) — это синтаксис в Python, который позволяет явно указать ожидаемые типы переменных, аргументов функций и возвращаемых значений. Не влияет на выполнение кода, но улучшает читаемость, автодополнение, анализ статическими средствами (`mypy`, `pyright`, `pylance`).

## Зачем использовать аннотации типов

- Помогают понять, что делает функция.
- Упрощают отладку.
- Позволяют использовать инструменты статической типизации.

## Синтаксис аннотаций

### Переменные:

```python
name: str = "Alice"
age: int = 25
```

### Функции:

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"
```

- `name: str` — аргумент `name` должен быть строкой.
- `-> str` — функция возвращает строку.

### Без возвращаемого значения:

```python
def print_hello() -> None:
    print("Hello")
```

### Списки, словари и другие коллекции:

```python
from typing import List, Dict

def process(numbers: List[int]) -> Dict[str, int]:
    return {"max": max(numbers), "min": min(numbers)}
```

---

## Модули typing: Union, Optional, Any, Final

### Union

Позволяет указать несколько допустимых типов. Значение может принадлежать любому из них.

```python
from typing import Union

def handle(value: Union[int, str]) -> None:
    print(value)
```

**Пример:** аргумент может быть либо `int`, либо `str`.

### Optional

Сокращение для `Union[X, None]`. Тип может быть либо указанным, либо `None`.

```python
from typing import Optional

def get_name(user_id: int) -> Optional[str]:
    if user_id == 0:
        return None
    return "Alice"
```

**Пример:** функция может вернуть строку или `None`.

### Any

Отключает проверку типов. Может быть абсолютно любой тип.

```python
from typing import Any

def log(data: Any) -> None:
    print(data)
```

**Пример:** аргумент может быть чем угодно.

### Final

Указывает, что переменная не должна быть изменена после присвоения. Используется как константа.

```python
from typing import Final

PI: Final = 3.14
```

**Пример:** `PI` будет считаться постоянным значением. Инструменты статического анализа выдадут ошибку при попытке его изменить.

---

## Пример полной функции с аннотациями:

```python
from typing import List

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)
```

---

## Инструменты для проверки типов

- [mypy](https://mypy-lang.org/): статическая проверка типов
- Pyright / Pylance: проверка типов в редакторах (например, VSCode)

> Аннотации делают код самодокументируемым и позволяют находить ошибки ещё до запуска.

