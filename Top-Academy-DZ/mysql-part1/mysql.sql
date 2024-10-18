-- task 1
CREATE DATABASE Birds;

-- task 3
DROP DATABASE Cats;

-- task 4
CREATE DATABASE products;

CREATE TABLE products.vegetables_and_fruits
(
    id INT
    AUTO_INCREMENT NOT NULL,
    name VARCHAR
    (100) NOT NULL,
    type ENUM
    ('овощ', 'фрукт') NOT NULL,
    color VARCHAR
    (50) NOT NULL,
    calories INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY
    (id)
);

    -- task 5
    INSERT products.vegetables_and_fruits
        (name, type, color, calories, description)
    VALUES
        ('Огурец', 'овощ', 'зеленый', 120, 'Зеленый вкусный овощ'),
        ('Помидор', 'овощ', 'красный', 12, 'Красный вкусный овощ'),
        ('Апельсин', 'фрукт', 'оранжевый', 234, 'Оранжевый вкусный фрукт'),
        ('Банан', 'фрукт', 'желтый', 34, 'Желтый вкусный фрукт'),
        ('Баклажан', 'овощ', 'зеленый', 123, 'Зеленый вкусный овощ'),
        ('Лимон', 'фрукт', 'желтый', 341, 'Желтый вкусный фрукт'),
        ('Слива', 'фрукт', 'черный', 123, 'Черный вкусный фрукт');

    -- Отображение всей информации из таблицы с овощами и фруктами;
    SELECT *
    FROM products.vegetables_and_fruits;

    -- Отображение всех овощей;
    SELECT *
    FROM products.vegetables_and_fruits
    WHERE type = 'овощ';

    -- Отображение всех фруктов;
    SELECT *
    FROM products.vegetables_and_fruits
    WHERE type = 'фрукт';

    -- Отображение всех названий овощей и фруктов;
    SELECT name
    FROM products.vegetables_and_fruits;

    -- Отображение всех цветов. Цвета должны быть уникальными;
    SELECT DISTINCT color
    FROM products.vegetables_and_fruits;

    -- Отображение фруктов конкретного цвета;
    SELECT *
    FROM products.vegetables_and_fruits
    WHERE type = 'фрукт' AND color = 'желтый';

    -- Отображение овощей конкретного цвета.
    SELECT *
    FROM products.vegetables_and_fruits
    WHERE type = 'овощ' AND color = 'зеленый';
