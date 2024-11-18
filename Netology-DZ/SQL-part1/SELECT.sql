-- Название и продолжительность самого длительного трека.
SELECT name, duration
FROM tracks
ORDER BY duration DESC
LIMIT 1;

-- Название треков, продолжительность которых не менее 3,5 минут.
SELECT name, duration FROM tracks WHERE duration >= 210;

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name
FROM collections
WHERE age BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова.
SELECT name
FROM artist
WHERE position(' ' IN name) = 0;

-- Название треков, которые содержат слово «моя» или «my».
SELECT name
FROM tracks
WHERE name LIKE '%моя%'
OR name LIKE '%my%';

-- Количество исполнителей в каждом жанре.
SELECT genre.title, COUNT(artist_genre.genre_id) as Количество_исполнителей
FROM genre
JOIN artist_genre
ON genre.id = artist_genre.genre_id
GROUP BY genre.title;

-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(collections.age) as Кол_во_треков
FROM tracks_collections
JOIN collections
ON tracks_collections.collection_id = collections.id
WHERE collections.age BETWEEN 2019 AND 2020;

-- Средняя продолжительность треков по каждому альбому.
SELECT album.title, ROUND(AVG(tracks.duration), 2) as Средняя_продолжительность
FROM album
JOIN tracks
ON album.id = tracks.album_id
GROUP BY album.title;

-- Все исполнители, которые не выпустили альбомы в 2017 году.
SELECT artist.name
FROM artist
WHERE artist.id NOT IN (
    SELECT album.id
    FROM album
    JOIN artist_album ON artist_album.artist_id = album.id
    WHERE album.year = 2017
);

-- SELECT artist.name as "Все_исполнители"
-- FROM artist_album
-- JOIN artist
-- ON artist.id = artist_album.artist_id
-- JOIN album
-- ON album.id = artist_album.album_id
-- WHERE album.year != 2017
-- GROUP BY artist.name;

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).SELECT DISTINCT album.title
FROM album
JOIN tracks ON tracks.id = album_id
JOIN artist ON artist.id = album.id
WHERE artist.name = 'Zivert';

-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
-- Наименования треков, которые не входят в сборники.
-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.


-- Названия альбомов, содержащих наименьшее количество треков.
