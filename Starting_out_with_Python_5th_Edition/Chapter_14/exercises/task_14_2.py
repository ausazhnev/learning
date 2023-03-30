# Задание #2 к главе 14
# Текст задания находится в файле tasks_ru.txt
#
# Task #2 to chapter 14
# The text of the task is in the file tasks_en.txt

import sqlite3

SHOW_ALL = 1
ADD_ENTRIES = 2
FIND_ENTRIES = 3
UPDATE_ENTRY = 4
DELETE_ENTRY = 5
DELETE_ALL = 6
MIN_VALUES = 0
MAX_VALUES = 6


# При первом запуске программы создаем пустую таблицу.
# Если таблица уже создана то создания новой таблицы не произойдет
def create_db():
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Entries 
                                        (EntriesID INTEGER PRIMARY KEY NOT NULL,
                                         Name TEXT,
                                         PhoneNumber TEXT)''')
        conn.commit()
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def show_menu():
    print()
    print(f'------------- Основное меню -------------')
    print(f'[1] > Показать всю телефонную базу')
    print(f'[2] > Добавить новую запись')
    print(f'[3] > Найти запись')
    print(f'[4] > Обновить существующую запись')
    print(f'[5] > Удалить существующую запись')
    print(f'[6] > Очистить базу (стереть все записи)')
    print(f'[0] > Выход')


def get_user_menu_choice():
    print(f'[#] > Введите выбранное выбранное действие от {MIN_VALUES} до {MAX_VALUES}')
    choice = input(f'[#] > > ')
    if choice.isnumeric() is not True:
        print(f'[#] > Вы должны ввести число!')
        choice = get_user_menu_choice()
    elif (int(choice) < MIN_VALUES) or (int(choice) > MAX_VALUES):
        print(f'[#] > Выбор должен быть от от {MIN_VALUES} до {MAX_VALUES}')
        choice = get_user_menu_choice()
    return int(choice)


def show_all_data():
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('SELECT Name, PhoneNumber FROM Entries')
        results = cur.fetchall()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()

    print(f'|---------- Имя ----------|--- Телефон ---|')
    for row in results:
        print(f'| {row[0]:<23} | {row[1]:>13} |')


def add_entries():
    name = input(f'[#] > Введите имя для контакта:\n'
                 f'[#] > > ')
    phone_number = input(f'[#] > Введите номер телефона контакта:\n'
                         f'[#] > > ')
    add_row(name, phone_number)


def add_row(name, phone_number):
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Entries (Name, PhoneNumber) 
                                    VALUES (?, ?)''',
                                    (name, phone_number))
        conn.commit()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def get_user_data():
    find_data = input(f'[#] > Введите Имя или номер телефона контакта\n'
                      f'[#] > > ')
    return find_data


def show_entries():
    find_data = get_user_data()
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT Name, PhoneNumber FROM Entries
                                                WHERE 
                                                    Name == ? OR
                                                    PhoneNumber == ?''',
                                                (find_data, find_data))
        results = cur.fetchall()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
    if len(results) > 0:
        print(f'|---------- Имя ----------|--- Телефон ---|')
        for row in results:
            print(f'| {row[0]:<23} | {row[1]:>13} |')
        print(f'|-------------------------|---------------|')
    else:
        print(f'[#] > Нет данных удовлетворяющих Вашему запросу.')


def set_update():
    change_id = int(input(f'[#] > Введите id записи, которую хотите изменить\n'
                          f'[#] > > '
                          ))
    new_name = input(f'[#] > Введите новое имя записи\n'
                     f'[#] > > '
                     )
    new_phone_num = input(f'[#] > Введите новый номер телефона для записи\n'
                          f'[#] > > '
                          )
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Entries 
                                 SET 
                                     Name = ?, PhoneNumber = ?
                                 WHERE
                                     EntriesID = ?''',
                    (new_name, new_phone_num, change_id))
        conn.commit()
        print(f'Изменения успешно внесены {new_name} в справочнике.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def update_entry():
    find_data = get_user_data()
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT EntriesID, Name, PhoneNumber FROM Entries
                                                WHERE 
                                                    Name == ? OR
                                                    PhoneNumber == ?''',
                                                (find_data, find_data))
        results = cur.fetchall()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        if len(results) > 0:
            print(f'|-id-|---------- Имя ----------|--- Телефон ---|')
            for row in results:
                print(f'| {row[0]:^2} | {row[1]:<23} | {row[2]:>13} |')
            print(f'|----|-------------------------|---------------|')
            set_update()
        else:
            print(f'[#] > Нет данных удовлетворяющих Вашему запросу.')


def set_delete():
    delete_id = int(input(f'[#] > Введите id записи, которую хотите изменить\n'
                          f'[#] > > '
                          ))
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM  Entries
                                     WHERE
                                         EntriesID = ?''',
                                    (delete_id,))
        conn.commit()
        print(f'Строка удалена из справочника.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def delete_entry():
    find_data = get_user_data()
    conn = None
    try:
        conn = sqlite3.connect('../db/phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT EntriesID, Name, PhoneNumber FROM Entries
                                                WHERE 
                                                    Name == ? OR
                                                    PhoneNumber == ?''',
                                                (find_data, find_data))
        results = cur.fetchall()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        if len(results) > 0:
            print(f'|-id-|---------- Имя ----------|--- Телефон ---|')
            for row in results:
                print(f'| {row[0]:^2} | {row[1]:<23} | {row[2]:>13} |')
            print(f'|----|-------------------------|---------------|')
            set_delete()
        else:
            print(f'[#] > Нет данных удовлетворяющих Вашему запросу.')


def delete_all():
    sure = input(f'[#] > Вы уверены, что хотите очистить содержимое справочника?\n'
                 f'[#] > (д/н)'
                 f'[#] > > '
                 )
    if sure.lower() == 'д':
        conn = sqlite3.connect('../db/phonebook.db')
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM Entries')
            conn.commit()
            print(f'Содержимое справочника успешно очищено.')
        except sqlite3.Error as err:
            print(f'[#] > Ошибка базы данных: {err}')
        finally:
            if conn is not None:
                conn.close()


def main():
    # Подключение к базе данных и создание таблицы если она еще не создана
    create_db()
    choice = None
    while choice != 0:
        show_menu()
        choice = get_user_menu_choice()
        if choice == SHOW_ALL:
            show_all_data()
        elif choice == ADD_ENTRIES:
            add_entries()
        elif choice == FIND_ENTRIES:
            show_entries()
        elif choice == UPDATE_ENTRY:
            update_entry()
        elif choice == DELETE_ENTRY:
            delete_entry()
        elif choice == DELETE_ALL:
            delete_all()


if __name__ == '__main__':
    main()
