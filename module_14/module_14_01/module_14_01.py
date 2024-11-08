import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

for i in range(1, 11):
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

cursor.execute("UPDATE Users SET balance=1000")
cursor.execute("UPDATE Users SET balance=500 WHERE id % 2 = 1")

cursor.execute("SELECT COUNT(id) FROM Users")
count_row = cursor.fetchone()[0]

for i in range(1, count_row + 1, 3):
    cursor.execute(f"DELETE FROM Users WHERE id = {i}")

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# users = cursor.fetchall()
# for el in users:
#     print(f'Имя: {el[0]} | Почта: {el[1]} | Возраст: {el[2]} | Баланс: {el[3]}')

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_row = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
balance_avg = cursor.fetchone()[0]

print(balance_avg)

connection.commit()
connection.close()
