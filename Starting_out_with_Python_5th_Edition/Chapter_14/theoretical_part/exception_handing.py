import sqlite3


def main():
    # Переменная управления циклом
    again = 'д'
    while again.lower() == 'д':
        # Получить ID товара, название и цену.
        item_id = int(input(f'ID товара: '))
        item_name = input(f'Наименование товара: ')
        price = float(input(f'Цена: '))
        # Добавить товар в базу данных
        add_item(item_id, item_name, price)
        # Добавить еще одну позицию ?
        again = input(f'Добавить еще одну позицию? (д/н): ')


# Функция add_item добавляет позицию в базу данных
def add_item(item_id, item_name, price):
    # Инициализировать переменную соединения
    conn = None
    try:
        # Присоединиться к базе данных
        conn = sqlite3.connect('../db/inventory.db')
        # Получить курсор
        cur = conn.cursor()
        # добавить позицию в базу данных
        cur.execute('''INSERT INTO Inventory (ItemId, ItemName, Price)
                       VALUES (?, ?, ?)''',
                    [item_id, item_name, price])
        # Зафиксировать изменения
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        # Закрыть соединение
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
