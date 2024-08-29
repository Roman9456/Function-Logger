# Function Logger

This project contains a decorator function logger that adds logging functionality to other functions. The logger records the function name, arguments, and return value to a log file.

## Usage

1. Import the logger function from the logger_module.py file.
2. Apply the logger decorator to the functions you want to log.
3. The logged data will be saved to a log file specified by the path argument in the logger function.

Example:

from logger_module import logger

# Define a different path for the log file
path = 'another_log.log'

# Apply the logger decorator to functions
@logger(path)
def multiply(a, b):
    return a * b

@logger(path)
def power(base, exponent):
    return base ** exponent

## Testing

The project includes two test functions, test_1() and test_2(), which test the functionality of the logger decorator. You can run these tests to ensure the correct operation of the decorator.

## Requirements

- Python 3.x
- Standard Python libraries: os, datetime

## License

This project is licensed under the [MIT License](LICENSE).

README.md (Russian)

# Логгер функций

Этот проект содержит функцию-декоратор logger, которая добавляет функциональность ведения журнала (логирования) к другим функциям. Логгер записывает название функции, аргументы и возвращаемое значение в файл журнала.

## Использование

1. Импортируйте функцию logger из файла logger_module.py.
2. Применяйте декоратор logger к функциям, которые вы хотите логировать.
3. Записанные данные будут сохранены в файле журнала, указанном аргументом path в функции logger.

Пример:

from logger_module import logger

# Определяем другой путь для файла журнала
path = 'another_log.log'

# Применяем декоратор logger к функциям
@logger(path)
def multiply(a, b):
    return a * b

@logger(path)
def power(base, exponent):
    return base ** exponent

## Тестирование

Проект включает две тестовые функции, test_1() и test_2(), которые проверяют функциональность декоратора logger. Вы можете запустить эти тесты, чтобы убедиться в правильной работе декоратора.

## Требования

- Python 3.x
- Стандартные библиотеки Python: os, datetime

## Лицензия

Этот проект распространяется под [Лицензией MIT](LICENSE).
