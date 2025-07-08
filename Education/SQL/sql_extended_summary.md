
# 📘 SQL: Основы и Типы Данных

## 📌 Что такое SQL?

**SQL (Structured Query Language)** — язык для работы с базами данных:

- Ищет нужные данные.
- Сортирует, фильтрует и структурирует их.
- Представляет данные в удобном виде (например, для отчётов).

**SQL — не язык для создания сайтов/приложений**, он работает *с данными*.

## 🧩 Реляционные базы данных

**Реляционная БД** — это набор таблиц, связанных между собой.

- Таблица = объект (например, Клиенты, Поставщики, Товары)
- Таблицы связаны через **первичные** и **внешние ключи**

**Пример связи:**

```
Таблица Товары:
- Идентификатор (Primary Key)
- Поставщик (Foreign Key -> Поставщики.Идентификатор)
```

**Столбцы (columns)**: поля, атрибуты, fields

**Строки (rows)**: записи, кортежи, records

## 🛠 Что такое СУБД

**СУБД (система управления базами данных)** — программа, которая управляет БД и обрабатывает SQL-запросы.

📍 Примеры: MySQL, PostgreSQL, SQLite, Oracle

## 📦 Типы данных в SQL

### 🔤 Строковые типы

#### `CHAR(n)`

- Строка **фиксированной длины**
- Дополняется пробелами до `n`
- До 255 символов

#### `VARCHAR(n)`

- Строка **переменной длины**
- До 65 535 байт

🔸 Пример хранения: "Привет" (6 байт) → занимает 7 байт (1 байт длины + 6 байт данных)

#### Когда использовать:

- `CHAR` — фиксированная длина
- `VARCHAR` — переменная длина

#### `BINARY(n)` / `VARBINARY(n)`

- Для хранения двоичных данных

#### `BLOB` / `TEXT`

- Для больших данных

#### `ENUM`, `SET`

- `ENUM` — одно значение из списка
- `SET` — несколько

### 🔢 Числовые типы

- `DECIMAL(p, s)`, `FLOAT(M,D)`, `DOUBLE(M,D)` — дробные
- `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT` — целые

### 📅 Типы даты и времени

- `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR`

## 🧱 Создание таблиц

```sql
CREATE TABLE имя_таблицы (
  имя_столбца1 тип_данных1 атрибуты,
  имя_столбца2 тип_данных2
);
```

- Названия в нижнем регистре, операторы — ВЕРХНИМ

## 🔐 Ограничения

- `NOT NULL`
- `UNIQUE`
- `PRIMARY KEY`
- `FOREIGN KEY`

## 💾 Вставка данных

```sql
INSERT INTO таблица (столбцы)
VALUES (...);
```

## 🔄 Обновление

```sql
UPDATE таблица
SET столбец = значение
WHERE условие;
```

## 🗑 Удаление

```sql
DELETE FROM таблица WHERE ...;
TRUNCATE TABLE таблица;
```

## 🔍 SELECT — извлечение данных

```sql
SELECT [DISTINCT] выражения
FROM таблица
[WHERE условие]
[GROUP BY поля]
[HAVING условие]
[ORDER BY поля [ASC|DESC]]
[LIMIT число];
```

### DISTINCT

```sql
SELECT DISTINCT visit_time FROM talons;
```

### WHERE

```sql
SELECT * FROM doctors WHERE cabinet_num = 21;
```

### Операторы сравнения

- `=`, `!=`, `>`, `<`, `>=`, `<=`, `IN`, `BETWEEN`, `LIKE`, `IS NULL`, `IS NOT NULL`

### NULL

```sql
WHERE cabinet_num IS NULL
```

## 📋 SELECT: выражения

Выражения могут быть:

- столбец: `SELECT doctor_num FROM doctors;`
- константа: `SELECT 'Привет' FROM doctors;`
- операция: `SELECT cabinet_num + 1 FROM doctors;`
- функция: `SELECT CONCAT('г.', area_address) FROM med_area;`
- без таблицы: `SELECT 1 + 1;` или `SELECT 1 + 1 FROM dual;`

## 🏷 ALIAS (псевдонимы)

```sql
SELECT 1 + 1 AS summa;
```

## 🔧 Встроенные функции

| Функция | Пример |
|--------|--------|
| `CONCAT()` | `SELECT CONCAT('П','р','и','в','е','т') AS ex_concat;` |
| `LOWER()` | `SELECT LOWER('ПриВет') AS ex_lower;` |
| `UPPER()` | `SELECT UPPER('ПриВет') AS ex_upper;` |
| `ABS()` | `SELECT ABS(-12.36) AS ex_abs;` |
| `GREATEST()` | `SELECT GREATEST(1,5,3) AS ex_greatest;` |
| `LEAST()` | `SELECT LEAST(1,5,3) AS ex_least;` |
| `ROUND()` | `SELECT ROUND(8.589, 2) AS ex_round;` |
| `CURDATE()` | `SELECT CURDATE() AS ex_curdate;` |
| `DAY()` | `SELECT DAY('2024-01-14') AS ex_day;` |
| `MONTH()` | `SELECT MONTH('2024-01-14') AS ex_month;` |
| `YEAR()` | `SELECT YEAR('2024-01-14') AS ex_year;` |
| `DATEDIFF()` | `SELECT DATEDIFF('2024-01-14', '2023-11-12') AS ex_diff;` |
| `ISNULL()` | `SELECT ISNULL(NULL) AS ex_null;` |
| `IF()` | `SELECT IF(1<2, 'да', 'нет') AS ex_if;` |
| `COALESCE()` | `SELECT COALESCE(NULL, NULL, 'значение') AS ex_coalesce;` |

## 🔽 ORDER BY

```sql
SELECT * FROM patients ORDER BY sex ASC;
SELECT full_name, sex, birth_date FROM patients ORDER BY 2, 3 DESC;
```

NULL при ASC — в начале, при DESC — в конце

## 🔢 LIMIT

```sql
SELECT * FROM talons ORDER BY visit_time LIMIT 3;
```
# 📊 Агрегатные функции и группировка в SQL

## 🔹 Скалярные и агрегатные функции

**Скалярные функции** — работают с одной строкой (например, `ROUND()`, `CONCAT()` и др.)  
**Агрегатные функции** — работают с несколькими строками и возвращают одно значение.

| Название функции | Описание |
|------------------|----------|
| `AVG(expr)`      | Среднее значение |
| `SUM(expr)`      | Сумма значений |
| `MIN(expr)`      | Минимум |
| `MAX(expr)`      | Максимум |
| `COUNT(expr)`    | Количество непустых значений |
| `COUNT(*)`       | Количество всех строк |

❗ Все функции (кроме `COUNT(*)`) игнорируют `NULL`.

Пример:

```sql
SELECT AVG(visit_amount) AS avg_amount 
FROM talons;
```

С фильтрацией:

```sql
SELECT AVG(visit_amount) AS avg_amount
FROM talons
WHERE doctor_num IN (2,3);
```

---

## 🔹 `GROUP BY`

**`GROUP BY`** группирует строки по указанному столбцу. Используется совместно с агрегатными функциями.

```sql
SELECT doctor_num, SUM(visit_amount) AS sum_amount
FROM talons
GROUP BY doctor_num;
```

---

## 🔹 `HAVING`

**`HAVING`** фильтрует группы после `GROUP BY`:

```sql
SELECT doctor_num, SUM(visit_amount) AS sum_amount
FROM talons
GROUP BY doctor_num
HAVING SUM(visit_amount) > 2000;
```

---
