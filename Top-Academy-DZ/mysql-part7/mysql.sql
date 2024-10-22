-- Создаем базу social_network
CREATE DATABASE social_network;

-- Создаем таблицу users
CREATE TABLE social_network.users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender ENUM('man', 'woman'),
    email VARCHAR(100)
);

-- Создаем таблицу users_friends
CREATE TABLE social_network.users_friends (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    user_id INT,
    friend_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

-- Создаем таблицу users_post
CREATE TABLE social_network.users_post (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    user_id INT,
    content TEXT(250),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Заполняем таблицу users
INSERT INTO social_network.users (first_name, last_name, age, gender, email)
VALUES ('Petr', 'Rostovskii', 15, 'men', 'asd@gmail.com'),
        ('Igor', 'Petrovcki', 21, 'men', 'gfhgfhhgf@gmail.com'),
        ('Elena', 'Faghruh', 25, 'woman', 'aqwqwewe123@gmail.com'),
        ('Djek', 'Sharz', 27, 'men', 'asd19999@gmail.com'),
        ('Svetlana', 'Chekasheva', 23, 'woman', 'asd1451asd@gmail.com');

-- Заполняем таблицу users_friends
INSERT INTO social_network.users_friends (user_id, friend_id)
VALUES (1, 2),
		(2, 1),
        (2, 3),
        (3, 2),
        (3, 4),
        (4, 3),
        (4, 5),
        (5, 4);

INSERT INTO social_network.users_post (user_id, content)
VALUES (1, "Risus ultricies. Amet efficitur vulputate accumsan amet est. Ornare risus vitae venenatis risus pell"),
        (2, "Venenatis sit cursus in ipsum ipsum et lorem non cras sed libero, venenatis sed eleifend dolor molli"),
        (3, "Mauris vel cursus leo, id elit. Imperdiet augue dictum. Tortor, ornare nisi molestie aenean lacinia"),
        (4, "In hac dolor amet, sed consectetur risus ultricies. Vestibulum nec eleifend ultricies. Accumsan inte"),
        (5, "Pulvinar faucibus. Dictumst. Dolor sapien quis, ornare adipiscing urna velit et mattis vel consectet");
