users = [
    {"name":"Олег", "age": 35},
    {"name":"Егор", "age": 33},
    {"name": "Игорь", "age":32}
]
def get_user_by_index(index: int):
    try:
        user = users[index - 1]
        return f"{user['name']} {user['age']}"
    except IndexError:
        return f"Пользователя с индексом {index} не существует"

print(get_user_by_index(2))