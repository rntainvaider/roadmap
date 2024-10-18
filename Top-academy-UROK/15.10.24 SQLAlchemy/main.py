from databeses.db import create_new_user, get_all_users, get_user_to_id, rename_user

# create_new_user(name="name1", age=11)

# create_new_user(name="name2", age=22)

# all_users = get_all_users()
# for user in all_users:
#     print(f"{user.name} {user.age}")

# user1 = get_user_to_id(1)
# user2 = get_user_to_id(2)
# print(user1.id, user1.name, user1.age)
# print(user2.id, user2.name, user2.age)

rename_user(1, "Новое имя")
