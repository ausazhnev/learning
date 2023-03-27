# Для понимания того что есть в базе добавил возможность показать все строки из базы
# функция show_all() выводит на экран полный список товаров в базе
import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 6
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
SHOW_ALL = 5
EXIT = 6


def main():
    choice = None
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()
        elif choice == SHOW_ALL:
            show_all()


# Функция display_menu выводит на экран главное меню
def display_menu():
    print(f'\n----- Меню ведения учета инструментов -----')
    print(f'1. Создать новую позицию')
    print(f'2. Прочитать позицию')
    print(f'3. Обновить позицию')
    print(f'4. Удалить позицию')
    print(f'5. Показа все строки')
    print(f'6. Выйти из программы')


# Функция get_menu_choice получает от пользователя пункт меню.
def get_menu_choice():
    # Получить от пользователя вариант действия
    choice = int(input(f'Введите ваш вариант: '))
    # Проверяем введенные данные
    while MIN_CHOICE > choice > MAX_CHOICE:
        print(f'Допустимые значения таковы: {MIN_CHOICE} - {MAX_CHOICE}')
        choice = int(input(f'Введите ваш вариант: '))
    return choice


# Функция create создает новую позицию
def create():
    print(f'Создать новую позицию')
    name = input(f'Название позиции: ')
    price = float(input(f'Цена: '))
    insert_row(name, price)


# Функция insert_row вставляет строку в таблицу Inventory
def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect('../db/inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                       VALUES (?, ?)''',
                       (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


# функция read читает существующую позицию
def read():
    name = input(f'Введите название искомой позиции: ')
    num_found = display_item(name)
    print(f'{num_found} строк(а) найдено.')


# Функция display_item выводит на экран все позиции
# с совпадающими названиями позиций.
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('../db/inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                       WHERE ItemName == ?''',
                       (name,))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Наименование: {row[1]:<35} Цена:{row[2]:<6}')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        # Вернуть число совпадений
        return len(results)


# Функция обновляет данные существующей позиции
def update():
    # Сначала показать пользователю найденные строки
    read()
    # Получить ID выбранной позиции
    selected_id = int(input(f'Введите ID обновляемой позиции: '))
    # Получить новые значения наименования и цены
    name = input(f'Введите новое название позиции: ')
    price = float(input(f'Введите новую цену: '))
    # Обновить строку
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} строк(а) обновлено')


def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect('../db/inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                       SET ItemName = ?, Price = ?
                       WHERE ItemId == ?''',
                       (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


# Функция delete удаляет позицию
def delete():
    # Сначала показать пользователю найденные строки
    read()
    # Получить ID выбранной позиции
    selected_id = int(input(f'Введите ID удаляемой позиции: '))
    # Подтвердить удаление
    sure = input(f'Вы уверены, что хотите удалить эту позицию? (д/н): ')
    if sure.lower() == 'д':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} строк(а) удалено')


def show_all():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('../db/inventory.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Inventory')
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Наименование: {row[1]:<35} Цена: {row[2]:<6}')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        # Вернуть число совпадений
        return len(results)


# Функция delete_row удаляет существующую позицию.
# Возвращает число удаленных строк
def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('../db/inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory 
                       WHERE ItemId == ?''',
                       (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        return num_deleted


if __name__ == '__main__':
    main()
