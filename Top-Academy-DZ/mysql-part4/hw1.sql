SELECT book.title, author.name, genre.name, book.price, book.amount
FROM book
JOIN author ON book.author_id = author.id
JOIN genre ON book.genre_id = genre.id
WHERE book.genre_id = (
    SELECT genre_id
    FROM book
    GROUP BY genre_id
    ORDER BY sum(amount) DESC
    LIMIT 1
    )
ORDER BY book.title;
