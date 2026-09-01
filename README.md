# Python Basic Course

Курс по основам программирования и анализа данных на Python (ИТМО)

## Информация о курсе

| | |
|---|---|
| Лекции | 32 ч |
| Практика | 32 ч |
| Самостоятельная работа | 145.6 ч |

## Структура курса

| Модуль | Тема | Директория |
|--------|------|------------|
| 1 | Введение в Python, настройка окружения | `01_python_basics/` |
| 2 | Неизменяемые и изменяемые типы данных | `02_python_structures/` |
| 3 | Управляющие конструкции, работа с файлами | `03_control_flow/` |
| 4 | Парадигмы программирования (функции, ООП, итераторы) | `04_paradigms/` |
| 5 | Работа с API | `05_api/` |
| 6 | Итоговая лабораторная работа | `06_test assignment/` |
| 7 | Анализ данных (NumPy, Pandas, Geopandas) | `07_data_analysis/` |
| 8 | Геоанализ (osmnx) | `08_geoanalysis/` |
| 9 | Визуализация (Matplotlib, Seaborn) | `09_visualization/` |
| 10 | Итоговый проект | `10_final_project/` |

## Как работать с курсом

**1. Клонируйте репозиторий**
```bash
git clone https://github.com/DKPokidov/python_basic_course.git
cd python_basic_course
```

**2. Создайте ветку для своих заданий**
```bash
git checkout -b student/ваше_имя
```

**3. Выполняйте задания**
- Откройте задание в VS Code или Jupyter Notebook
- Напишите решение в месте `# НАПИШИТЕ ВАШ КОД ЗДЕСЬ`
- Сохраните файл

**4. Отправьте работу**
```bash
git add .
git commit -m "Выполнены задания: модуль N"
git push origin student/ваше_имя
```

**5. Создайте Pull Request** на GitHub из вашей ветки в `master`

## Автоматические тесты

При каждом Pull Request запускаются тесты:
- Проверка корректности решений (`pytest`)
- Проверка стиля кода (`flake8`)

Запуск локально:
```bash
python -m pytest tests/ -v
python -m flake8 0*/practice/ tests/
python utils/validator.py
```
