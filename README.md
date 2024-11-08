- [**FULLSTACK PYTHON DEVELOPER**](#fullstack-python-developer)
- [**Python**](#python)
  - [Переменные](#переменные)
  - [Базовые типы данных](#базовые-типы-данных)
    - [Числа и операции над ними int/float](#числа-и-операции-над-ними-intfloat)
  - [Циклы](#циклы)
    - [Цикл for](#цикл-for)
    - [Цикл while](#цикл-while)
  - [Регулярные выражения](#регулярные-выражения)
    - [Функции регулярных выражений](#функции-регулярных-выражений)
    - [Метасимволы регулярных выражений](#метасимволы-регулярных-выражений)
    - [Флаги регулярных выражений](#флаги-регулярных-выражений)
  - [Веб-скрапинг](#веб-скрапинг)
    - [Библиотеки для веб-скрапинга](#библиотеки-для-веб-скрапинга)

# **FULLSTACK PYTHON DEVELOPER**
# **Python**

Python - является высокоуровневым интепретируемым кроссплатформенным динамически строго типизированным языком программирования. Динамическая типизация - это не изменение самой переменной, а перенаправление ссылки, на другой объект.

## Переменные

Переменная - это ссылка на пространство в мамяти, в котором находится некоторый объект. Объекты же - это хранилище данных, имеющие определенный тип данных и имеющие набор свойств и методов. Название переменной может состоять из букв, цифр, нижнего подчеркивания, но не может состоять только из цифр, не может начинаться с цифр и каких либо знаков припенания.

## Базовые типы данных
### Числа и операции над ними int/float
`abs()` - находит модуль числа и принимает на вход одно значение. Модуль числа - это абсолютная величина, то есть, грубо говоря, модуль числа отбрасывает знак.

`min()` - принимает на вход несколько значений через запятую и находит самое наименьшее из них.

`max()` - принимает на вход несколько значений через запятую и находит самое наибольшее из них.

`pow()` - принимает на вход 2 значения и возводит первое число в степень второго.

`round()` - принимает на вход значение и выполняет округление по умолчанию до целого числа. Также, если через запятую указать разряд, то функция будет округлять именно до этого разряда.

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
