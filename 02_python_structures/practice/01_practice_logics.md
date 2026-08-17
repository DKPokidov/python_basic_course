### Логический тип данных

#### Конъюнкция (Логическое умножение)

| A | B | A and B |
|---|---|---------|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

```python
print(f'False and False = {False and False}')
print(f'False and True = {False and True}')
print(f'True and False = {True and False}')
print(f'True and True = {True and True}')
```

#### Дизъюнкция (логическое сложение)

| A | B | A or B |
|---|---|--------|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

```python
print(f'False and False = {False or False}')
print(f'False and True = {False or True}')
print(f'True and False = {True or  False}')
print(f'True and True = {True or  True}')
```

#### Инверсия (логическое отрицание)

| A | not A |
|---|-------|
| False | True |
| True | False |

```python
print(f'False != False = {False != False}')
print(f'True != True = {True != True}')
print(f'False != True = {False != True}')
```

#### Преоритет выполнения логических операций

Сначала выполняется:
1. Действие в скобках;
2. Логическое отрицание,
3. Конюнкция (and - логическое умножение);
4. Дизъюнкция (or - логическое сложение)

```python
# Что будет?
True and False or True
```

```python
# Что будет?
True or False or True and False
```

```python
# Что будет?
(True or False or True) and True
```

```python
# Что будет?
True != False and True
```

```python
# Что будет?
(True != True and False) != True and True or False
```
