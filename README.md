# Price Formatter

## Описание

Скрипт для форматирования строки с ценой. Если цена содержит
дробную часть, то производится ее округление до второго знака после
запятой. Если переданная строка некорректна, то генерируется исключение
ValueError.

## Использование
Скрипт имеет следующие обязательные параметры:

* price - Строка со значением цены в неотформатированном виде

Скрипт имеет следующие опциональные параметры:

* -h, --help - помощь


## Пример

Отображение справки:

```sh
$ python3.5 ./format_price.py -h
usage: format_price.py [-h] price

Script for price formatting

positional arguments:
  price       Price string

optional arguments:
  -h, --help  show this help message and exit
```

Примеры использования:

```sh
$ python3.5 ./format_price.py 3245.000000
[format_price.py#] INFO     [01/05/2017 10:01:28 PM] Formatted price: 3 245
```

```sh
$ python3.5 ./format_price.py 3245.1399
[format_price.py#] INFO     [01/05/2017 10:56:17 PM] Formatted price: 3 245,14
```

## Тесты

Для проверки работоспособности скрипта разработаны тесты
(файл tests.py). Тестовый случай состоит из двух тестов:

* Проверка правильности форматирования набора тестовых цен:
  3245.000000, -3245.000000, 3245.1399, -3245.1399, 123456.999 =>
  3 245,       -3 245,       3 245,14,  -3 245,14,  123 457

* Проверка того, что каждая цена из набора некорректных цен
приводит к исключению ValueError:
  3 245.000000, 3245,000000, abc, - 3245.1399 => ValueError

Пример использования тестов:

```sh
$ python3.5 ./tests.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
