import sqlite3


def main():
    conn = None
    try:
        # Подсоединиться к базе данных и получить курсор.
        conn = sqlite3.connect('../db/employees.db')
        cur = conn.cursor()
        # Задействовать поддержку внешнего ключа
        cur.execute('PRAGMA foreign_keys=ON')
        # Вставить новую строку в таблицу Employees
        cur.execute('''INSERT INTO Employees
                                   (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Билл Свифт", "Стажер", 99, 1)''')
        conn.commit()
        print(f'Сотрудник успешно добавлен.')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
