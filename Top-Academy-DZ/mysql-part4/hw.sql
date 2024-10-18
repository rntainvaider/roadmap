-- 1. Подсчитать количество групп, в которые вступил каждый пользователь.
-- И вывести данные пользователя(firstname, lastname, email, phone)
SELECT users.firstname, users.lastname, users.email, users.phone, COUNT(users_communities.community_id)
FROM users
JOIN users_communities ON users_communities.user_id = users.id
GROUP BY users.firstname, users.lastname, users.email, users.phone;

-- 2. Подсчитать количество пользователей в каждом сообществе.
-- И вывести id сообщества и его название
SELECT communities.id, communities.name AS Название_сообщества, COUNT(users_communities.user_id) AS Количество_пользователей_в_сообществе
FROM communities
JOIN users_communities ON communities.id = users_communities.community_id
GROUP BY communities.id;

-- 4. Подсчитать общее количество лайков, которые получили пользователи младше 18 лет..
SELECT COUNT(likes.id) AS total_likes
FROM users
JOIN likes ON users.id = likes.id
JOIN profiles ON users.id = profiles.user_id
WHERE TIMESTAMPDIFF(YEAR, profiles.birthday, CURDATE()) < 18;

-- 5. Определить кто больше поставил лайков (всего): мужчины или женщины
SELECT profiles.gender, COUNT(likes.id) AS total_likes
FROM users
JOIN likes ON users.id = likes.id
JOIN profiles ON users.id = profiles.user_id
GROUP BY profiles.gender
ORDER BY total_likes DESC;
