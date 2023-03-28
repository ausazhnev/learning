# у меня нет исходников db employees.db по этому,
# этот сприт создает ее и наполняет тестовыми данными

import sqlite3


def main():
    conn = None
    try:
        conn = sqlite3.connect('../db/employees.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Departments 
                              (DepartmentID INTEGER PRIMARY KEY NOT NULL,
                              DepartmentName TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Locations  
                              (LocationID INTEGER PRIMARY KEY NOT NULL,
                              City TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Employees 
                              (EmployeeID INTEGER PRIMARY KEY NOT NULL,
                              Name TEXT,
                              Position TEXT,
                              DepartmentID INTEGER,
                              LocationID INTEGER,
                              FOREIGN KEY (DepartmentID) REFERENCES 
                                Departments (DepartmentID),
                              FOREIGN KEY (LocationID) REFERENCES
                                Locations (LocationID))''')
        # cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) 
                                   VALUES (1, 'Бухгалтерский учет')''')
        cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) 
                                   VALUES (2, 'Производство')''')
        cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) 
                                   VALUES (3, 'Маркетинг')''')
        cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) 
                                   VALUES (4, 'Исследования и разработки')''')

        cur.execute('''INSERT INTO Locations (LocationID, City) 
                                   VALUES (1, 'Остин')''')
        cur.execute('''INSERT INTO Locations (LocationID, City) 
                                   VALUES (2, 'Бостон')''')
        cur.execute('''INSERT INTO Locations (LocationID, City) 
                                   VALUES (3, 'Нью-Йорк')''')
        cur.execute('''INSERT INTO Locations (LocationID, City) 
                                   VALUES (4, 'Сан-Хосе')''')

        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Арлин Мейерс", "Директор", 4, 4)''')
        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Джанель Грант", "Инженер", 2, 1)''')
        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Джек Смит", "Менеджер", 3, 3)''')
        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Соня Альварадо", "Аудитор", 1, 2)''')
        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Рене Кинкейд", "Дизайнер", 3, 3)''')
        cur.execute('''INSERT INTO Employees (Name, Position, DepartmentID, LocationID)
                                   VALUES ("Курт Грин", "Супервайдер", 2, 1)''')

        conn.commit()

    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
