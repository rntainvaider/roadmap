-- КАРТИНКА ТАБЛИЦЫ БАЗЫ ДАННЫХ В ПАПКЕ


-- ЗАДАНИЕ 1
-- Отображение всех овощей с калорийностью меньше, указанной калорийности;
SELECT *
FROM vegetables_and_fruits
WHERE type = 'овощ' AND calories < 123;

-- Отображение всех фруктов с калорийностью в указанном диапазоне;
SELECT *
FROM vegetables_and_fruits
WHERE calories BETWEEN 10 AND 50;

-- Отображение всех овощей в названии, которых есть указанное слово. Например, слово: капуста;
SELECT *
FROM vegetables_and_fruits
WHERE name = 'Помидор' OR name = 'Баклажан';

-- Отображение всех овощей и фруктов в кратком описании, которых есть указанное слово. Например, слово: гемоглобин;
SELECT *
FROM vegetables_and_fruits
WHERE description LIKE '%Зеленый%';

-- Показать все овощи и фрукты, у которых цвет желтый или красный
SELECT *
FROM vegetables_and_fruits
WHERE description LIKE '%Желтый%' OR description LIKE '%Красный%';

-- Задание 2
-- Показать количество овощей;
SELECT COUNT(type) as Количество_овощей
FROM vegetables_and_fruits
WHERE type = 'овощ';

-- Показать количество фруктов;
SELECT COUNT(type) as Количество_фруктов
FROM vegetables_and_fruits
WHERE type = 'фрукт';

-- Показать количество овощей и фруктов заданного цвета;
SELECT COUNT(color) as Количество_овощей_и_фруктов_желтого_цвета
FROM vegetables_and_fruits
WHERE color = 'желтый';

-- Показать количество овощей и фруктов каждого цвета;
SELECT color, count(color) as Количество_овощей_и_фруктов_каждого_цвета
FROM vegetables_and_fruits
GROUP BY color;

-- Показать цвет с минимальным количеством овощей и фруктов;
SELECT color, COUNT(*) AS количество
FROM vegetables_and_fruits
GROUP BY color
ORDER BY количество LIMIT 1;

-- Показать цвет с максимальным количеством овощей и фруктов;
SELECT color, COUNT(*)AS количество
FROM vegetables_and_fruits
GROUP BY color
ORDER BY количество DESC LIMIT 1;

-- Показать минимальную калорийность овощей и фруктов;
SELECT *
FROM vegetables_and_fruits
WHERE calories =
(SELECT MIN(calories)
    FROM vegetables_and_fruits
    WHERE type = 'фрукт')
    OR calories =
(SELECT MIN(calories)
    FROM vegetables_and_fruits
    WHERE type = 'овощ');

-- Показать максимальную калорийность овощей и фруктов;
SELECT *
FROM vegetables_and_fruits
WHERE calories = (SELECT MAX(calories)
    FROM vegetables_and_fruits
    WHERE type = 'фрукт') OR calories = (SELECT MAX(calories)
    FROM vegetables_and_fruits
    WHERE type = 'овощ');

-- Показать среднюю калорийность овощей и фруктов;
SELECT ROUND(AVG(calories), 2) as средняя_калорийность_овощей_и_фруктов
FROM vegetables_and_fruits;

-- Показать фрукт с минимальной калорийностью;
SELECT *
FROM vegetables_and_fruits
WHERE calories = (SELECT MIN(calories)
FROM vegetables_and_fruits
WHERE type = 'фрукт');

-- Показать фрукт с максимальной калорийностью
SELECT *
FROM vegetables_and_fruits
WHERE calories = (SELECT MAX(calories)
FROM vegetables_and_fruits
WHERE type = 'фрукт');
