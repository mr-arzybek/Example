# Что такое База Данных ?
# База данных (БД) — это упорядоченная совокупность данных, которая предназначена для их хранения,
# управления и быстрого доступа. Данные в базе обычно структурированы таким образом,
# чтобы ими было удобно пользоваться. База данных может использоваться для хранения информации
# различного типа: текст, числа, изображения, видео, и другие форматы.


# Что такое  SQL ?
# SQL (Structured Query Language) — это стандартный язык для взаимодействия с базами данных.
# Он используется для выполнения различных операций над данными,
# хранящимися в реляционных базах данных (таких как MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server и другие).


# Что такое СУБД ?
# СУБД (система управления базами данных) — это программное обеспечение,
# которое используется для создания, управления, хранения и извлечения данных в базах данных.
# Она предоставляет инструменты и интерфейсы для работы с данными, обеспечивая их упорядоченное хранение и доступ.

import sqlite3


# Подключаемся к базе данных
def connect_db():
    return sqlite3.connect('users_with_grades.db')


# Функция для создания таблиц
def create_tables():
    connect = connect_db()
    cursor = connect.cursor()

    # Создание таблицы 'users'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            userid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор пользователя
            fio VARCHAR(100) NOT NULL,                -- ФИО пользователя
            age INTEGER NOT NULL                      -- Возраст пользователя
        )
    ''')

    # Создание таблицы 'grades'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор записи о оценке
            userid INTEGER,                            -- Внешний ключ, который ссылается на userid из таблицы 'users'
            subject VARCHAR(100) NOT NULL,             -- Название предмета
            grade INTEGER NOT NULL,                    -- Оценка
            FOREIGN KEY (userid) REFERENCES users(userid) -- Определяем связь с таблицей 'users'
        )
    ''')

    # Закрываем соединение
    connect.commit()
    connect.close()


# Функция для добавления пользователя
def add_user(fio, age):
    connect = connect_db()
    cursor = connect.cursor()

    # Вставка пользователя в таблицу 'users'
    cursor.execute("INSERT INTO users (fio, age) VALUES (?, ?)", (fio, age))

    # Подтверждение изменений
    connect.commit()
    connect.close()


# Функция для добавления оценки
def add_grade(userid, subject, grade):
    connect = connect_db()
    cursor = connect.cursor()

    # Вставка оценки в таблицу 'grades'
    cursor.execute("INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)", (userid, subject, grade))

    # Подтверждение изменений
    connect.commit()
    connect.close()


# Функция для вывода всех пользователей с их оценками
def get_users_with_grades():
    connect = connect_db()
    cursor = connect.cursor()

    # Выполнение запроса на соединение таблиц и получение данных
    cursor.execute('''
        SELECT users.fio, users.age, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.userid = grades.userid
    ''')



    # Печать результатов
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Закрытие соединения
    connect.close()


# Пример использования функций

# Создание таблиц (если они еще не созданы)
create_tables()

# Добавление пользователей
add_user('Иванов Иван Иванович', 20)
add_user('Петрова Мария Ивановна', 22)

# Добавление оценок
add_grade(1, 'Математика', 5)
add_grade(1, 'Физика', 4)
add_grade(2, 'Химия', 5)

# Вывод всех пользователей с их оценками
get_users_with_grades()




# # Пример функции для получения всех пользователей
# def get_all_users():
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#
#     if users:
#         print("Список всех пользователей:")
#         for user in users:
#             print(f"ФИО: {user[0]}, возраст: {user[1]}, хобби: {user[2]}")
#     else:
#         print("Список пользователей пуст.")
#
# # Вызов функции
# get_all_users()