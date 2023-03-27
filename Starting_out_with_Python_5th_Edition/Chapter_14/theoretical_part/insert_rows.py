import sqlite3


def main():
    # Присоединиться к базе данных
    conn = sqlite3.connect('../db/inventory.db')
    # Получить курсор
    cur = conn.cursor()
    # Добавить строку в таблицу Inventory
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ('Отвертка', 4.99)''')
    # Добавить еще одну строку в таблицу Inventory
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ('Молоток', 12.99)''')
    # Добавить еще одну строку в таблицу Inventory
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ('Плоскогубцы', 14.99)''')
    # Зафиксировать изменения
    conn.commit()
    # Закрыть соединение
    conn.close()


if __name__ == '__main__':
    main()
