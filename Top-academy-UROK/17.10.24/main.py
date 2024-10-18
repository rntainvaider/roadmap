from databases.db import DB

DB.create_new_user(
    firstname="Вася", lastname="Пупкин", otchevo="Евгеньевич", phone="99991232399", team_id=1
)

DB.create_new_team()
