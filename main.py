def sort_users_by_activity(dicty):
    return sorted(
        user_activity.keys(), key=lambda user: user_activity[user], reverse=True
    )


user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
print(sort_users_by_activity(user_activity))
# ['user3', 'user4', 'user1', 'user5', 'user2']
