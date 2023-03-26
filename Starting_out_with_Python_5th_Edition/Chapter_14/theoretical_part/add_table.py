import sqlite3


def main():
    # Присоединяемся к базе данных
    conn = sqlite3.connect('../db/Inventory.db')
    # Получаем курсор
    cur = conn.cursor()
    # Добавляем таблицу Inventory
    cur.execute('''CREATE TABLE Inventory (ItemId INTEGER PRIMARY KEY NOT NULL,
                                           ItemName TEXT,
                                           Price REAL)''')
    # Зафиксировать изменения
    conn.commit()
    # Закрыть соединение
    conn.close()


if __name__ == '__main__':
    main()
