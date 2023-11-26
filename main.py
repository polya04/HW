import sqlite3

#створити базу даних з Д/З-1
conn = sqlite3.connect('sto.db')
cursor = conn.cursor()

#створюємо таблицю
cursor.execute('''
    CREATE TABLE IF NOT EXISTS client (
        id INTEGER,
        name TEXT,
        surname TEXT,
        mobile_phone TEXT,
        car TEXT
        )    
''')
conn.commit()

#наповнити базу даними (INSERT ... VALUES ...)
cursor.execute("INSERT INTO client VALUES (1, 'Олександр', 'Зубко', '0980229623', 'Toyota')")
cursor.execute("INSERT INTO client VALUES (2, 'Ігор', 'Фомін', '0986475363', 'Tesla')")
cursor.execute("INSERT INTO client VALUES (3, 'Владислав', 'Новохрещений', '0673406754', 'BMW')")
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS service (
        id INTEGER,
        name TEXT,
        surname TEXT,
        price TEXT
        )    
''')
conn.commit()

#наповнити базу даними (INSERT ... VALUES ...)
cursor.execute("INSERT INTO service VALUES (1, 'Олександр', 'Зубко', '2000UAH')")
cursor.execute("INSERT INTO service VALUES (2, 'Ігор', 'Фомін', '73669UAH')")
cursor.execute("INSERT INTO service VALUES (3, 'Владислав', 'Новохрещений', '52630UAH')")
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER,
        name TEXT,
        surname TEXT,
        order_date TEXT,
        status TEXT
        )    
''')
conn.commit()

#наповнити базу даними (INSERT ... VALUES ...)
cursor.execute("INSERT INTO orders VALUES (1, 'Олександр', 'Зубко', '04.06.2021', 'done')")
cursor.execute("INSERT INTO orders VALUES (2, 'Ігор', 'Фомін', '05.10.2022', 'done')")
cursor.execute("INSERT INTO orders VALUES (3, 'Владислав', 'Новохрещений', '25.12.2022', 'done')")
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS car (
        id INTEGER,
        name TEXT,
        surname TEXT,
        model TEXT,
        model_year INTEGER,
        engine code INTEGER
        )    
''')
conn.commit()

#наповнити базу даними (INSERT ... VALUES ...)
cursor.execute("INSERT INTO car VALUES (1, 'Олександр', 'Зубко', 'Toyota', '2021', '202823')")
cursor.execute("INSERT INTO car VALUES (2, 'Ігор', 'Фомін', 'Tesla', '2020', '9034874')")
cursor.execute("INSERT INTO car VALUES (3, 'Владислав', 'Новохрещений', 'BMW', '2013', '8287263')")
conn.commit()


#виконати SELECT запити
#повертає імена всіх клієнтів
print("Імена всіх клієнтів: ")
cursor.execute ("SELECT name FROM client")
print(cursor.fetchall())
print()

#повертає прізвища всіх клієнтів
print("Прізвища всіх клієнтів: ")
cursor.execute ("SELECT surname FROM client")
print(cursor.fetchall())

print()

#повертає номера всіх клієнтів
print("Номера всіх клієнтів: ")
cursor.execute ("SELECT mobile_phone FROM client")
print(cursor.fetchall())

print()

#повертає марку машини всіх клієнтів
print("Марки машин всіх клієнтів: ")
cursor.execute ("SELECT car FROM client")
print(cursor.fetchall())

#оновити записи - UPDATE ... SET ... WHERE ...
print()
cursor.execute('UPDATE client SET car = "Audi" WHERE name = "Олександр"')
conn.commit()

print('Марки машин після апгрейду всіх клієнтів: ')
cursor.execute("SELECT car FROM client")
print(cursor.fetchall())

conn.close()
