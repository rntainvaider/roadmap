class Group:
    members = []


class Student:
    pass


s1 = Student()
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1

s2 = Student()
s2.name = "Лев"
s2.surname = "Сергеев"
s2.semester = 1

group = Group()

group.members.append(s1.name)
group.members.append(s1.surname)
group.members.append(s1.semester)
group.members.append(s2.name)
group.members.append(s2.surname)
group.members.append(s2.semester)

result = group.members
result_0 = isinstance(result[0], Student)
print(result_0)
