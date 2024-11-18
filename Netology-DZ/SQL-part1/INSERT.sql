-- заполняем таблицу artist
INSERT INTO artist (name)
VALUES ('Zivert'),
        ('Баста'),
        ('Кино'),
        ('NILETTO'),
        ('Король и Шут');

-- заполняем таблицу genre
INSERT INTO genre (title)
VALUES ('Рок'),
        ('Попса'),
        ('Шансон'),
        ('Джаз');

-- заполняем таблицу album
INSERT INTO album (title, year)
VALUES ('Первый удар', 2012),
        ('Свободная Зона', 2008),
        ('Палец на отсечение', 2017);

-- заполняем таблицу tracks
INSERT INTO tracks (name, year, duration, album_id)
VALUES ('Моя игра', 20003, 240, 1),
        ('Любовь без памяти', 2001, 240, 2),
        ('Осень', 2000, 256, 3),
        ('Ты так мне необходим', 2002, 247, 2),
        ('Моя Вселенная', 2003, 231, 3),
        ('Солнца не видно', 2005, 267, 1);

-- заполняем таблицу collections
INSERT INTO collections (name, age)
VALUES ('СБПЧ Здесь и всегда', 2017),
        ('Lapti В тираж', 2018),
        ('Hudson Mohawke Lantern', 2019),
        ('Lana Del Rey Honeymoon', 2020);

-- заполняем таблицу artist_genre
INSERT INTO artist_genre (artist_id, genre_id)
VALUES (1, 3),
        (2, 1),
        (3, 4),
        (4, 2);

-- заполняем таблицу artist_album
INSERT INTO artist_album (artist_id, album_id)
VALUES (1, 3),
        (2, 2),
        (4, 2),
        (3, 1),
        (3, 1),
        (2, 3);

-- заполняем таблицу tracks_collections
INSERT INTO tracks_collections (collection_id, tracks_id)
VALUES (1, 2),
        (2, 3),
        (3, 1),
        (4, 4),
        (3, 5),
        (2, 6),
        (4, 3),
        (1, 2);
