family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

for item in family_member.get("children"):
    if item.get("name") == "Bob":
        print(f"С таким именем {item.get('name')} ребенок есть")
    elif item.get("name") == "Rob":
        print(f"С таким именем {item.get('name')} ребенок есть")
    else:
        print("Noname")
