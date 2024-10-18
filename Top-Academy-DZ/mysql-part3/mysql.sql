-- Вывести все жанры, которые не представлены в книгах на складе.
SELECT genre.name
FROM genre
    LEFT JOIN book
    ON genre.id = book.genre_id
WHERE book.id IS NULL
GROUP BY genre.name;

-- Вывести информацию о книгах (жанр, книга, автор), относящиехся к жанру, включающему слово "приключения" в отсортированном по названиям книг виде.
SELECT genre.name, book.title, author.name
FROM book
    INNER JOIN genre ON genre.id = book.genre_id
    INNER JOIN author ON author.id = book.genre_id
WHERE genre.name LIKE "%приключения%";
