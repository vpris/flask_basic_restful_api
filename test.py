import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'vpris', 'qwerty123')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'santa', 'qwe'),
    (3, 'stefano', 'rty')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print("Create user: " + row[1])

connection.commit()

connection.close()
