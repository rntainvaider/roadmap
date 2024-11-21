- [**ROADMAP FULLSTACK PYTHON DEVELOPER**](#roadmap-fullstack-python-developer)
- [**Python**](#python)
  - [Переменные](#переменные)
  - [Базовые типы данных](#базовые-типы-данных)
    - [Числа int/float](#числа-intfloat)
      - [Числа и операции над ними](#числа-и-операции-над-ними)
    - [Списки](#списки)
      - [Двумерные списки](#двумерные-списки)
      - [Списки и операции над ними](#списки-и-операции-над-ними)
    - [Кортежи и операции над ними](#кортежи-и-операции-над-ними)
    - [Множества и операции над ними](#множества-и-операции-над-ними)
    - [Словари](#словари)
      - [Словари и операции над ниди](#словари-и-операции-над-ниди)
  - [Циклы](#циклы)
    - [Цикл for](#цикл-for)
    - [Цикл while](#цикл-while)
  - [Функции](#функции)
  - [ООП](#ооп)
  - [Регулярные выражения](#регулярные-выражения)
    - [Функции регулярных выражений](#функции-регулярных-выражений)
    - [Метасимволы регулярных выражений](#метасимволы-регулярных-выражений)
    - [Флаги регулярных выражений](#флаги-регулярных-выражений)
  - [Итераторы](#итераторы)
  - [Генераторы](#генераторы)
  - [Паттерны проектирования](#паттерны-проектирования)
    - [Декораторы](#декораторы)
  - [Веб-скрапинг](#веб-скрапинг)
    - [Библиотеки для веб-скрапинга](#библиотеки-для-веб-скрапинга)
  - [Фреймворки](#фреймворки)
    - [Django](#django)
      - [БД, SQL и ORM](#бд-sql-и-orm)
      - [Миграции](#миграции)
    - [Flet](#flet)
    - [Pytest](#pytest)
  - [HTTP запросы](#http-запросы)
  - [Библиотеки](#библиотеки)
    - [loggin](#loggin)
- [GIT](#git)
- [HTML](#html)
- [CSS](#css)
- [Вопросник](#вопросник)
  - [Python](#python-1)
  - [HTML](#html-1)
  - [CSS](#css-1)
  - [JavaScript](#javascript)

# **ROADMAP FULLSTACK PYTHON DEVELOPER**
# **Python**

Python - является высокоуровневым интепретируемым кроссплатформенным динамически строго типизированным языком программирования. Динамическая типизация - это не изменение самой переменной, а перенаправление ссылки, на другой объект.

## Переменные

Переменная - это ссылка на пространство в мамяти, в котором находится некоторый объект. Объекты же - это хранилище данных, имеющие определенный тип данных и имеющие набор свойств и методов. Название переменной может состоять из букв, цифр, нижнего подчеркивания, но не может состоять только из цифр, не может начинаться с цифр и каких либо знаков припенания.

## Базовые типы данных
### Числа int/float
#### Числа и операции над ними
`abs()` - находит модуль числа и принимает на вход одно значение. Модуль числа - это абсолютная величина, то есть, грубо говоря, модуль числа отбрасывает знак.

`min()` - принимает на вход несколько значений через запятую и находит самое наименьшее из них.

`max()` - принимает на вход несколько значений через запятую и находит самое наибольшее из них.

`pow()` - принимает на вход 2 значения и возводит первое число в степень второго.

`round()` - принимает на вход значение и выполняет округление по умолчанию до целого числа. Также, если через запятую указать разряд, то функция будет округлять именно до этого разряда.

### Списки

Список - это упорядоченный набор элементов, каждый их которых имеет свой индекс, позволяющий быстро к нему обратиться. В списке можно хранить различные типы данных.

Индекс - это порядковый номер элемента в списке, начинающийся с 0.

С помощью индексов вохможно менять значение в списке. Пример: `list[3] = 'Pavel'`

Так же возможно получать элементы списка с помощью срезов.

Срез - это извлечение из данного списка одонго или нескольких фрагментов. `list[start, stop, step]`

#### Двумерные списки
`Двумерные списки` - это список, каждый элемент которого является одномерным списком

#### Списки и операции над ними

- `append()` - добавляет элемент в конец списка.
- `extend()` - добавляет в указанный список переданные элементы в список
- `len()` - позволяет узнать количество элементов в списке
- `insert()` - добавляет указанный элемент по указанному индексу. При этом соседние элемента массива сдвигаются вправую сторону
- `remove()` - удаляет элемент по значению и если нет элемента возвращает ValueError
- `pop()` - удаляет элемент по индексу, при этом возвращая значение. Если не передать значение в метод, тогда удаляет последний элемент в списке.
- `clear()` - полностью очищает список, удаляя из него все элементы
- `index()` - возвращает индекс указанного элемента, если элемента нет в списке возвращает ValueError
- `sort()` - позволяет сортировать данный список, без создания нового

### Кортежи и операции над ними

### Множества и операции над ними

### Словари

`Словарь` - это неупорядоченная структура данных, элементамти которой является пары ключ:значение. Значения ключей уникальны и не могут повторяться. Ключом словаря может быть любой неизменяемый тип данных. А в значение словаря можно записывать любой тип данных.

#### Словари и операции над ниди

Чтобы добавить новую пару в словарь и так же можно менять значение по ключу, нужно:

```
translator['tester'] = 'тестировщик'
```

- `del dict[key]` - удаляет элемент словаря по его ключу
- `pop()` - удаляет элемент словаря по его ключу, возвращая его значение
- `keys()` - возвращает список ключей словаря
- `values()` - возвращает список значений словаря
- `items()` - возвращает список кортежей всех пар ключей:значения словаря

## Циклы

Цикл - это конструкция, которая помогает выполнить определенный блок кода несколько раз.

`Итерация` - это одно повторение блока кода в цикле.

`break` -  команда прерывает работу цикла и выходит из цикла.
`continue` - команда пропускает текущую итерацию цикла и переходит к следующей итерации.

### Цикл for

`for` - счетный, повторяет блок кода определенное количество раз

`range(start, stop, step)` - генерирует список чисел от 0 до указанного числа (не включительно) и передает эти значения в переменную цикла. Задает количество итераций в цикле

### Цикл while

`while` - условный, повторяет блок кода до наступления определенного условия

## Функции

`Функция` - это фрагмент кода, который выполняет определенные операции и отдаёт результат. Пишем один раз, а вызываем сколько нам угодно.

Функции помогают избавиться от дублирования кода. А так же повысить читаемость и чистоту кода.

Принцип DRY (Don’t Repeat Yourself — «Избегай самоповтора») — один из основных принципов разработки ПО, который наставляет нас избегать дублирования кода путём применения различных инструментов и навыков.

- Процедурное программирование. Программа без функций, которая выполняется последовательно сверху вниз.
- Функциональное программирование. Программа, которая содержит функции, но всё ещё является процедурным кодом. Однако такой код более компактный, поскольку вся функциональность вынесена за скобки — в функции.

Параметры — это переменные, которые перечислены в определении функции. Они действуют в качестве «заполнителей» для значений, которые будут использоваться в функции.

Аргументы — это конкретные значения, которые передаются в функцию при её вызове.

## ООП

- Объектно-ориентированное программирование. Программа строится на основе классов и объектов. С этим типом программирования мы познакомим вас на заключительных этапах.

## Регулярные выражения
Регулярное выражение - это шаблоны, по которым можно проверять валдиность данных, искать совпадения в тексте или заменять определенные фрагменты.
### Функции регулярных выражений
`re.match()` - поиск вхождения шаблона в начале строки. В качестве аргументов требуется передать сначала шаблон, а потом строку для проверки.

`re.search` - ищет первое вхождение шаблона в любом месте строки, возвращает объект match, если в строке есть другие подходящие фрагменты, то они будут проигнорированы. У функции есть дополнительные функции, упрощающие поиск:
- `.group()` - возвращает тот фрагмент строки, в котором нашлось совпадение;
- `.span()` - возвращает кортеж с начальной и конечной позицией искомого шаблона;
- `.string()` - возвращает строку которую передали в re.search().

`re.findall()` - поиск всех вхождение шаблона в любом месте строки

`re.sub()` - заменяет фрагменты в соответствии с шаблоном

`re.split()` - разделяет строку по шаблону, количество разделений задается числом

### Метасимволы регулярных выражений

| Метасимвол | Зачем он нужен                                                                                                                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .          | Задает один произвольный символ, кромк новой строки                                                                                                               |
| [...]      | Любой символ в скобках, сами символы можно задавать с помощью перечислений или диапазонов                                                                         |
| [^...]     | Любой символ, ислючая указанные в скобках, сами символы можно задавать с помощью перечислений или диапазонов                                                      |
| ^          | Начало строки                                                                                                                                                     |
| $          | Конец строки                                                                                                                                                      |
| \|         | Логический оператор ИЛИ. Поиск одного из нескольких указанных вариантов                                                                                           |
| \          | Экранирование, с помощью которого Python понимает, является ли следующий символ обычным или специальным. Можно обычные символы превращать в метасимволы и обратно |
| *          | Проивольное число повторений одного символа                                                                                                                       |
| ?          | Строго одно повтороение символа                                                                                                                                   |
| +          | Указывает, что предыдущее выражение может повторяться сколько угодно раз, но как минимум один раз                                                                 |
| (...)      | Группировка символов в скобках                                                                                                                                    |
| {...}      | Число повторений предыдущего символа                                                                                                                              |

| Символ | Зачем он нужен                                                                     |
| ------ | ---------------------------------------------------------------------------------- |
| \d     | Любая цифра, заменяет собой запись [0-9]                                           |
| \D     | Исключает все цифры, заменяет собой запись [^0-9]                                  |
| \s     | Любой пробельный символ, включая пробел, табуляцию, новую строку и возврат каретки |
| \S     | Любой символ, исключая пробельный                                                  |
| \w     | Любая буква, цифра и знак нижнего подчеркивания (_)                                |
| \W     | Любой символ, кроме буквы, цифры и нижнего подчеркивания                           |
| \A     | Начало строки, заменяет собой запись ^                                             |
| \Z     | Конец строки, заменяет собой запись $                                              |
| \b     | Начало или конец строки                                                            |
| \B     | Середина слова                                                                     |
| \n     | Новая строки                                                                       |
| \t     | Табуляция                                                                          |
| \r     | Возврат каретки                                                                    |

### Флаги регулярных выражений

| Краткая запись флага | Полная запись флага | Зачем нужен                                                                                                         |
| -------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| re.I                 | re.IGNORECASE       | Игнорирует регистр символов                                                                                         |
| re.A                 | re.ASCII            | Возвращает совпадения только по таблице ASCII-символов                                                              |
| re.X                 | re.VERBOSE          | Позволяет использовать комментарии в регулярных выражениях                                                          |
| re.S                 | re.DOTALL           | Метасимвол точка (.) возвращает совпадения по всем символам, включая новую строку.                                  |
| re.L                 | re.LOCALE           | Добавляет к \w, \W, \b, \B, \s и \S региональные настройки, но работает только с байтовыми строками                 |
| re.M                 | re.MULTILINE        | Возвращает совпадения в начале каждой новой строки, если используется с ^, и в конце каждой новой строки — если с $ |

## Итераторы

`Итероваты` - позволяют создавать и работать с последовательностями объектов. Итератор - это объект, который реализует два метода `__iter__()` и `__next__()`. Если в последовательности нет элементов, метод `__next__()` должен вызвать исключение `StopIteration`

- `__iter__()` - возвращает сам итератор
- `__next__()` - возвращает следующий элемент последовательности

## Генераторы

`Генераторы` - функция, которая возвращает итератор, с помощью которого можно обойти некую последовательность значений. Генератор использует ключевое слово `yield` вместо `return` для возврата значений. Когда функция-генератор вызывается, она не выполняет свое тело сразу, а возвращает объект генератор и возвращает значения по мере их генерации.

- `yield` - используется для создания функции-генераторов, которые возвращают итератор. `return` останавливает выполнение тела функции на всегда, а `yield` выполнение приостанавливает, до её возобновления посредством `next()`

## Паттерны проектирования
(Ссылка на паттерны проектирования)[https://refactoring.guru/ru/design-patterns]
### Декораторы

`Декораторы` -     чтобы дополнять дополнительную логику до выполнения функции и после выполнения функции. Чтобы изменить поведение функции

## Веб-скрапинг

Веб-скрапинг - это процесс извлечения данных из веб-страниц путем скачивания и анализа их содержимого.

### Библиотеки для веб-скрапинга

1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html) - ссылка на документацию
    - `pip install beautifulsoup4`
    - Особенности: превосходный парсер HTML/XML, простой интерфейс веб-скрейпинга, гибкая навигация и поиск.
    - `find_all()` - метод, просматривает и извлекат всех потомков тега, которые соответствуют переданным фильтрующим аргументам
    - `find()` - метод, который ищет первый элемент, удовлетворяющий заданным критериям, в дереве элементов HTML DOM. Если такой элемент не найден, возвращает None.
2. [Scary](https://scrapy.org/) - ссылка на документацию
    - `pip install scrapy`
    - Особенности: быстрая и масштабируемая, middleware, функция распределённого скрейпинга.
3. [Selenium](https://www.selenium.dev/documentation/overview/) - ссылка на документацию
    - `pip install selenium`
    - Особенности: полная автоматизация браузера, работа с сайтами с большим объёмом javascript.
4. [lxml](https://lxml.de/) - ссылка на документацию
    - `pip install lxml`
    - Особенности: очень быстрый парсер XML и HTML
5. [pyquery](https://pythonhosted.org/pyquery/) - ссылка на документацию
    - `pip install pyquery`
    - Особенности: синтаксис в стиле jQuery для доступа к HTML-элементам.

## Фреймворки
### Django
Команда `pip install django` - устанавливает библиотеку
#### БД, SQL и ORM
Джанго построен на MTV (Modelds, Templates, Views)

ORM (Object-Relational Mapping)

#### Миграции
Миграции - создают таблицы в базе данных, а так же меняет существующую.

Команда `python manage.py makemigrations` - создает миграцию

Команда `python manage.py migrate` - применяет миграцию

Команда `python manage.py sqlmigrate [название папки] [номер файла миграциии]` - дает возможность просмотреть запрос на языке sql

### Flet
[Ссылка на документацию](https://flet.dev/docs/)

- Команда `pip install flet` - устанавливает библиотеку
- Команда `flet --version` - узнать какая версия установлена
- Команда `flet create <имя проекта>` - содает новый проект
- Команда `flet run <имя файла>` - запускает программу
- Команда `flet run --web <имя файла>` - запускат приложение как web-приложение

### Pytest

Pytest - это фреймворк для тестирования кода на языке Python.

- Команда `pip install -U pytest` - установка Pytest
- Команда `pytest` - запускает тессты текущего католога
- Команда `pytest <имя файла.py>` - запускает файл с тестами
<!-- - Команда `pytest <имя файла.py>;<имя функции>` - запускает проверку функции -->

Чтобы Pytest воспринимал функции тестовыми, файлы и сами тесты должны быть названы определенным образом:
- **название файла** должно начинаться с `test` или заканчиваться на `test.py`
- **название функции** должно быть аписано в нижнем регистре и начинаться с `test_`

`assert()` - отвечает за результат тестирования. Если заданное после него условие правдиво — тест пройден, если оно ложно оператор assert вызывает исключение AssertionError, что приводит к остановке выполнения программы

`Фикстуры` - это функции, которые создают окружение вокруг тестов. Они удобны, когда нужно передать один и те же входные данные нескольким тестам.

`Финализатор` -

## HTTP запросы
- GET - получение ресурса
- POST - создание ресурса
- PUT - обновление ресурса
- DELETE - удаление ресурса
- OPTIONS - доступные запросы
- HEAD - получение заголовков
- PATCH - обновление части ресурса

## Библиотеки

### loggin
`import login` - это набор функций и классов, которые позволяют регистрировать события, происходящие во время работы кода.

Основная функция, которая пригодится Вам для работы с этим модулем — basicConfig(). В ней Вы будете указывать все основные настройки (по крайней мере, на базовом уровне).

У функции basicConfig() 3 основных параметра:

- level — уровень логирования на Python;
- filename — место, куда мы направляем логи;
- format — вид, в котором мы сохраняем результат.

# GIT

**Слияние веток**
1. Перейдите к ветке master: git checkout master.
2. Обновите локальную ветку с сервера: git pull origin master.
3. Выполните команду: git merge merged-branch. где merged-branch — имя сливаемой ветки. Сливаемой веткой считается та, из которой берутся изменения.

# HTML
HTML (Hyper Text Markup Language) - язык гиппертекстовой разметки. Определяет структуру вашего контента.

Любой документ на языке HTML представляет собой набор элементов, причем начало и конец каждого элемента обозначается специальными пометками - тегами.

Структурные элементы - `<html>, <head>, <body>`

Текстовые элементы - `<h1><h6>, <p>, <span>, <a>`

Строчные элементы - `<strong>, <em>, <br>, <img>`

Блочные элементы - `<div>`

# CSS
CSS (Cascading Style Sheets) - каскадные таблицы стилей. Формальный язык описания внешнего вида документа написанного с использованием языка разметки

```
селектор {
  свойство: значение;
}
```
Селекторы бывают элементов, по ID, класса, по атрибуту, псевдокласса.

Псевдоклассы
- `:hover` -
- `:active` -
- `:focus` -
- `:visited` -****
- `:nth-child(n)` -
- `:first-child` -
- `:last-child` -
- `:nth-of-type(n)` -
- `:not(highlight)` -

Псевдоэлементы
- `::defore` -
- `::after` -
- `::first-line` -
- `::first-letter` -
///

# Вопросник
## Python
## HTML
## CSS
## JavaScript
