import sqlite3


def main():
    conn = None
    try:
        # Присоединяемся к базе данных и получаем курсор
        conn = sqlite3.connect('../db/employees.db')
        cur = conn.cursor()
        # Задействовать поддержку внешнего ключа
        cur.execute('PRAGMA foreign_keys=ON')
        # Вставить новую строку в таблицу Employees
        cur.execute('''INSERT INTO Employees
                       (Name, Position, DepartmentID, LocationID)
                       VALUES ("Анжела Тейлор", "Программист", 4, 4)''')
        conn.commit()
        print(f'Сотрудник успешно добавлен.')
    except sqlite3.Error as err:
        print(f'Ошибка с базой данных: {err}')
    finally:
        # Если соединение открыто, то закрываем его.
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
