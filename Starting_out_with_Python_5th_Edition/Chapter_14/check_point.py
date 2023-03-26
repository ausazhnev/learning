# 14.21 Напишите инструкцию SQL для создания таблицы с именем Book. В таблице Book должны быть
# столбцы, содержащие название изделия, имя автора, число страниц и 10-символьный код ISBN
cur.execute('''CREATE TABLE IF NOT EXISTS Book (BookName TEXT, 
                                  Autor TEXT, 
                                  NumberOfPages INTEGER, 
                                  ISBN TEXT)''')

# 14.22 Напишите инструкцию удаления таблицы Book, созданной в контрольном упражнении 14.21
cur.execute('''DROP TABLE IF EXISTS Book''')

# 14.23 Напишите инструкцию SQL для вставки следующих данных в таблицу Inventory базы данных
# inventory.db
import sqlite3
conn = sqlite3.connect('inventory.db')
cur = conn.cursor()
cur.execute('''INSERT INTO Inventory (ItemId, ItemName, Price)
                                     VALUES (10, 'Циркулярная пила', 199.99)''')
conn.commit()
conn.close()

# 14.24 Напишите инструкцию SQL для вставки следующих данных в таблицу Inventory базы данных
# inventory.db
cur.execute('''INSERT INTO Inventory (ItemName, Price)
                                      VALUES ('Зубило', 8.99)''')

# 14.25 Предположим, что cur является объектом Cursor, переменная name_input ссылается на
# строковое значение, а переменная price_input ссылается на значение с плавающей точкой. Напишите
# инструкцию, в которой используется параметризованный запрос SQL для добавления строки в таблицу
# Inventory базы inventory.db. В этм запросе значение переменной name_input вставляется в столбец
# ItemName, а значение переменной price_input - в столбец Price.
cur.execute('''INSERT INTO Inventory (ItemName, Price)
                                     VALUES (?, ?)''',
                                     (input_name, price_input))

# 14.25 Предположим, что в базе данных есть таблица Inventory со следующими столбцами:
# Имя столбца       Тип
# ProductName       TEXT
# QtyOnHand         INTEGER
# Cost              REAL
# а) Напишите инструкцию SELECT, которая вернет все столбцы из каждой строки таблицы Inventory
cur.execute('SELECT * FROM Inventory')
# б) Напишите инструкцию SELECT, которая вернет столбец ProductName из каждой строки
# таблицы Inventory
cur.execute('SELECT ProductName FROM Inventory')
# в) Напишите инструкцию SELECT, которая вернет столбец ProductName и столбец QtyOnHand из
# каждой сроки таблицы Inventory
cur.execute('SELECT ProductName, QtyOnHand FROM Inventory')
# г) Напишите инструкцию SELECT, которая вернет столбец ProductName только из строк, где
# стоимость меньше 17.00
cur.execute('SELECT ProductName FROM Inventory WHERE Cost < 17')
# д) Напишите инструкцию SELECT, которая вернет все столбцы из строк, где ProductName
# заканчивается на 'ZZ'
cur.execute('SELECT * FROM Inventory WHERE ProductName LIKE "%ZZ"')

# 14.32 Напишите инструкцию SQL которая поменяет цену все изделий с шоколадной стружкой в таблице
# Products базы chocolate.db на 4.99
cur.execute('''UPDATE Products 
               SET RetailPrice = 4.99 
               WHERE Description LIKE "%с шоколадной стружкой%"''')

# 14.33 Напишите инструкцию SQL которая удалит все строки в таблице Products базы данных
# chocolate.db, стоимость единиц которых превышает 4,00
cur.execute('''DELETE FROM Products
               WHERE RetailPrice > 4.00''')