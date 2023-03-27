import sqlite3


def main():
    # Переменная управления циклом
    again = 'д'
    # Присоединение к базе данных
    conn = sqlite3.connect('../db/inventory.db')
    # Получаем курсор
    cur = conn.cursor()
    while again.lower() == 'д':
        # Получить название и цену позиции.
        item_name = input(f'Введите название товарной позиции: ')
        price = float(input(f'Введите стоимость позиции: '))
        # Добавляем позицию в таблицу Inventory
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                                              VALUES (?, ?)''',
                                              (item_name, price))
        # добавить еще?
        again = input(f'добавить еще одну позицию? (д/н) ')
    # Зафиксировать изменения
    conn.commit()
    # Закрываем соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
