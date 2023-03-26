import sqlite3


def main():
    # Подключаемся к базе данных
    conn = sqlite3.connect('../db/company.db')
    # Получить курсор
    cur = conn.cursor()
    # Добавить таблицу Customer
    cur.execute('''CREATE TABLE Customer (CustomerID INTEGER PRIMARY KEY NOT NULL,
                                          Name TEXT,
                                          Email TEXT)''')
    # Добавить таблицу Employees
    cur.execute('''CREATE TABLE Employees (EmployeesId INTEGER PRIMARY KEY NOT NULL,
                                           Name TEXT,
                                           Position TEXT)''')
    # Зафиксировать изменения
    conn.commit()
    # Закрыть соединение
    conn.close()


if __name__ == '__main__':
    main()
