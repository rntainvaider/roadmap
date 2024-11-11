-- Создаем базу данных
CREATE DATABASE music;

-- Создаем таблицу artist
CREATE TABLE artist
(
    ID SERIAL NOT NULL,
    name VARCHAR (50) NOT NULL,
    PRIMARY KEY (ID)
);

-- Создаем таблицу genre
CREATE TABLE genre
(
    ID SERIAL NOT NULL,
    title VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID)
);

-- Создаем таблицу artist_genre
CREATE TABLE artist_genre
(
    ID SERIAL,
    artist_id INT,
    genre_id INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (artist_id) REFERENCES artist (ID),
    FOREIGN KEY (genre_id) REFERENCES genre (ID)
);

-- Создаем таблицу album
CREATE TABLE album
(
    ID SERIAL NOT NULL,
    title VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (ID)
);

-- Создаем таблицу artist_album
CREATE TABLE artist_album
(
    ID SERIAL NOT NULL,
    artist_id INT,
    album_id INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (artist_id) REFERENCES artist (ID),
    FOREIGN KEY (album_id) REFERENCES album (ID)
);

-- Создаем таблицу collectios
CREATE TABLE collections
(
    ID SERIAL NOT NULL,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (ID)
);

-- Создаем таблицу tracks
CREATE TABLE tracks
(
    ID SERIAL NOT NULL,
    name VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    duration INT NOT NULL,
    album_id INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (album_id) REFERENCES album (ID)
);

-- Создаем таблицу tracks_collections
CREATE TABLE tracks_collections
(
    ID SERIAL NOT NULL,
    collection_id INT,
    tracks_id INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (collection_id) REFERENCES collections (ID),
    FOREIGN KEY (tracks_id) REFERENCES tracks (ID)
);
