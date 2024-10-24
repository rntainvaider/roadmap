from datadase_settings import get_mysql_connect


def get_all_users() -> None:
    connect = get_mysql_connect()
    cur = connect.cursor()
    cur.execute(f"select * from users")

    result = cur.fetchall()
    for item in result:
        print(item)


get_all_users()


def del_user_by_id(id_user: int) -> None:
    connect = get_mysql_connect()
    cur = connect.cursor()

    cur.execute("DELETE FROM likes WHERE user_id = %s", (id_user,))
    cur.execute("DELETE FROM users_communities WHERE users_communities.user_id = %s", (id_user,))
    cur.execute("DELETE FROM messages WHERE messages.to_user_id = %s1 OR messages.from_user_id = %s2", (id_user, id_user))
    cur.execute("DELETE FROM friend_requests WHERE friend_requests.initiator_user_id = %s1 OR friend_requests.target_user_id = %s2", (id_user, id_user))
    cur.execute("DELETE likes FROM media JOIN likes ON likes.media_id = media.id WHERE media.user_id = %s", (id_user,))
    cur.execute("UPDATE profiles JOIN media ON profiles.photo_id = media.id SET profiles.photo_id = NULL WHERE media.user_id = %s", (id_user,))
    cur.execute("DELETE FROM media WHERE media.user_id = %s", (id_user,))
    cur.execute("DELETE FROM profiles WHERE profiles.user_id = %s", (id_user,))
    cur.execute("DELETE FROM users WHERE users.id = %s", (id_user,))

    connect.commit()

del_user_by_id(1)
