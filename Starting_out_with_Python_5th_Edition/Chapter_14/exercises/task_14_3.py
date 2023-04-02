# Задание #3 к главе 14
# Текст задания находится в файле tasks_ru.txt
#
# Task #3 to chapter 14
# The text of the task is in the file tasks_en.txt


import os.path
import sqlite3


''' Основное меню '''
DEPARTMENTS_MENU = 1
MAJORS_MENU = 2
STUDENTS_MENU = 3
MAIN_MIN_VALUE = 0
MAIN_MAX_VALUE = 3

''' Меню специальности '''
ADD_NEW_MAJOR = 1
FIND_MAJOR = 2
UPDATE_MAJOR = 3
DELETE_MAJOR = 4
SHOW_ALL_MAJORS = 5
BACK = 0
MAJOR_MIN_VALUE = 0
MAJOR_MAX_VALUE = 5

''' Меню факультеты '''
ADD_NEW_DEPARTMENT = 1
FIND_DEPARTMENT = 2
UPDATE_DEPARTMENT = 3
DELETE_DEPARTMENT = 4
SHOW_ALL_DEPARTMENTS = 5
DEPARTMENT_MIN_VALUE = 0
DEPARTMENT_MAX_VALUE = 5

''' Меню студенты '''
ADD_NEW_STUDENT = 1
FIND_STUDENT = 2
UPDATE_STUDENT = 3
DELETE_STUDENT = 4
SHOW_ALL_STUDENTS = 5
STUDENT_MIN_VALUE = 0
STUDENT_MAX_VALUE = 5


''' Блок для первого запуска программы, создание базы данных и таблиц'''
def start():
    # Проверяем существует ли файл с базой данных, и если его нет то создаем ее.
    if not os.path.exists('../db/student_info.db'):
        # Создаем базу данных и все необходимые таблицы
        create_db()
    else:
        print(f'[#] > Файл базы данных найден. . .')
        print(f'[#] > Загрузка сопутствующих программ. . .')
        print(f'[#] > Приложение готово к работе. . .')
        print(f'[#]')


def decoration():
    print(f'[#] > Обнаружен первый запуск программы. . .')
    print(f'[#] > Инициализируем базу данных. . .')
    print(f'[#] > . . .')
    print(f'[#] > Создаем структуру таблиц. . .')
    print(f'[#] > Таблица Majors . . . ok')
    print(f'[#] > Таблица Departments . . . ok')
    print(f'[#] > Таблица Students . . . ok')
    print(f'[#] > Программа готова к работе!')
    print(f'[#]')


def create_db():
    conn = None
    decoration()
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY,
                                                          Name TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY,
                                                          Name TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Students 
                                                (StudentID INTEGER PRIMARY KEY NOT NULL,
                                                 Name TEXT,
                                                 MajorID INTEGER,
                                                 DeptID INTEGER,
                                                 FOREIGN KEY (MajorID) REFERENCES
                                                   Majors (MajorID),
                                                 FOREIGN KEY (DeptID) REFERENCES
                                                   Departments (DeptID))''')
        conn.commit()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
''' Конец блока первого запуска'''


''' Общие функции используемые в программе '''
def get_user_menu_choice(min_values, max_values):
    print(f'[#] > Введите выбранное выбранное действие от {min_values} до {max_values}')
    choice = input(f'[#] > > ')
    if choice.isnumeric() is not True:
        print(f'[#] > Вы должны ввести число!')
        choice = get_user_menu_choice(min_values, max_values)
    elif (int(choice) < min_values) or (int(choice) > max_values):
        print(f'[#] > Выбор должен быть от от {min_values} до {max_values}')
        choice = get_user_menu_choice(min_values, max_values)
    return int(choice)


def get_parameter(parameter):
    parameter = input(f'[#] > Введите {parameter}: \n'
                      f'[#] > > '
                      )
    return parameter


def show_results(results):
    print(f'[#] > --------------- Результаты запроса ---------------')
    for row in results:
        print(f'[#] > ', end='')
        for i in range(len(results[0])):
            print(f'{row[i]}\t\t', end='')
        print()


def confirm(action):
    sure = input(f'[#] > Вы уверены, что хотите {action} запись?\n'
                 f'[#] > > (д/н): ')
    if sure.lower() == 'д':
        sure = True
    else:
        sure = False
    return sure
''' Конец блока общих функций '''


''' Блок работы с факультетами, меню и функции обработки '''
def add_new_department():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        dept_name = get_parameter('наименование')
        cur.execute('''INSERT INTO Departments (Name) VALUES (?)''', (dept_name,))
        conn.commit()
        print(f'[#] > Новый факультет добавлен в базу данных.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def find_department():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        dept_name = get_parameter('наименование')
        cur.execute('SELECT Name FROM Departments WHERE Name LIKE ?', (f'%{dept_name}%',))
        # Вариант записи через конкатенацию строк, так же работает
        # cur.execute('SELECT Name FROM Departments WHERE Name LIKE ?',('%'+dept_name+'%',))
        results = cur.fetchall()
        if len(results) > 0:
            show_results(results)
        else:
            print(f'[#] > Факультет не найден.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def update_department():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Departments''')
        results = cur.fetchall()
        # Выводим на экран содержимое таблицы с идентификатором
        show_results(results)
        # Уточнить идентификатор
        id_change_row = 0
        # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
        while (int(id_change_row) < 1) or (int(id_change_row) > len(results)):
            id_change_row = get_parameter('идентификатор')
        # Получить новое значение наименования
        new_name = get_parameter('наименование')
        # Внести изменение в базу
        if confirm('изменить'):
            try:
                cur.execute('''UPDATE Departments SET Name = ? 
                                                  WHERE DeptID == ?''',
                            (new_name, id_change_row))
                conn.commit()
                print(f'Запись {new_name} успешно изменена.')
            except sqlite3.Error as err:
                print(f'Ошибка базы данных: {err}')
        else:
            print(f'Изменение отменено.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def delete_department():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Departments''')
        results = cur.fetchall()
        # Выводим на экран содержимое таблицы с идентификатором
        show_results(results)
        id_change_row = 0
        while (int(id_change_row) < 1) or (int(id_change_row) > len(results)):
            # Уточнить идентификатор
            id_change_row = get_parameter('идентификатор')
        if confirm('удалить'):
            try:
                cur.execute('''DELETE FROM Departments WHERE DeptID == ?''', (id_change_row,))
                conn.commit()
                print(f'[#] > Запись удалена')
            except sqlite3.Error as err:
                print(f'[#] > Ошибка базы данных: {err}')
        else:
            print(f'Изменение отменено.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def show_all_department():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Departments')
        results = cur.fetchall()
        show_results(results)
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
    return results


def dept_menu():
    while True:
        print()
        print(f'[#] > -- Меню Факультеты')
        print(f'[1] > Добавить новый факультет')
        print(f'[2] > Найти факультет')
        print(f'[3] > Обновить информацию о факультете')
        print(f'[4] > Удалить факультет')
        print(f'[5] > Показать все факультеты')
        print(f'[0] > Вернуться в предыдущее меню')
        choice = get_user_menu_choice(DEPARTMENT_MIN_VALUE, DEPARTMENT_MAX_VALUE)
        if choice == ADD_NEW_DEPARTMENT:
            add_new_department()
        elif choice == FIND_DEPARTMENT:
            find_department()
        elif choice == UPDATE_DEPARTMENT:
            update_department()
        elif choice == DELETE_DEPARTMENT:
            delete_department()
        elif choice == SHOW_ALL_DEPARTMENTS:
            show_all_department()
        elif choice == BACK:
            main_menu()

''' Конц блока работы с факультетами '''


''' Блок работы со специальностями, меню и функции обработки '''
def add_new_major():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        major_name = get_parameter('наименование')
        cur.execute('INSERT INTO Majors (Name) VALUES (?)', (major_name,))
        conn.commit()
        print(f'[#] > Новая специальность добавлена в базу данных.')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def find_major():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        major_name = get_parameter('наименование')
        cur.execute('SELECT Name FROM Majors WHERE Name LIKE ?', (f"%{major_name}%",))
        results = cur.fetchall()
        if len(results) > 0:
            show_results(results)
        else:
            print(f'[#] > Факультет не найден.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def update_major():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors''')
        results = cur.fetchall()
        # Выводим на экран содержимое таблицы с идентификатором
        show_results(results)
        # Уточнить идентификатор
        id_change_row = 0
        # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
        while (int(id_change_row) < 1) or (int(id_change_row) > len(results)):
            id_change_row = get_parameter('идентификатор')
        # Получить новое значение наименования
        new_name = get_parameter('наименование')
        # Внести изменение в базу
        if confirm('изменить'):
            try:
                cur.execute('''UPDATE Majors SET Name = ? 
                                                  WHERE MajorID == ?''',
                            (new_name, id_change_row))
                conn.commit()
                print(f'Запись {new_name} успешно изменена.')
            except sqlite3.Error as err:
                print(f'Ошибка базы данных: {err}')
        else:
            print(f'Изменение отменено.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def delete_major():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Majors''')
        results = cur.fetchall()
        # Выводим на экран содержимое таблицы с идентификатором
        show_results(results)
        id_change_row = 0
        while (int(id_change_row) < 1) or (int(id_change_row) > len(results)):
            # Уточнить идентификатор
            id_change_row = get_parameter('идентификатор')
        if confirm('удалить'):
            try:
                cur.execute('''DELETE FROM Majors WHERE MajorID == ?''', (id_change_row,))
                conn.commit()
                print(f'[#] > Запись удалена')
            except sqlite3.Error as err:
                print(f'[#] > Ошибка базы данных: {err}')
        else:
            print(f'Изменение отменено.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def show_all_majors():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Majors')
        results = cur.fetchall()
        show_results(results)
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
    return results


def majors_menu():
    while True:
        print()
        print(f'[#] > -- Меню Специальности')
        print(f'[1] > Добавить новую специальность')
        print(f'[2] > Найти специальность')
        print(f'[3] > Обновить информацию о специальности')
        print(f'[4] > Удалить специальность')
        print(f'[5] > Показать все специальности')
        print(f'[0] > Вернуться в предыдущее меню')
        choice = get_user_menu_choice(MAJOR_MIN_VALUE, MAJOR_MAX_VALUE)
        if choice == ADD_NEW_MAJOR:
            add_new_major()
        elif choice == FIND_MAJOR:
            find_major()
        elif choice == UPDATE_MAJOR:
            update_major()
        elif choice == DELETE_MAJOR:
            delete_major()
        elif choice == SHOW_ALL_MAJORS:
            show_all_majors()
        elif choice == BACK:
            main_menu()
''' Конц блока работы со специальностями '''


''' Блок работы со студентами, меню и функции обработки '''
def add_new_student():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        new_student_name = get_parameter('Имя студента')

        results_majors = show_all_majors()
        major_id = 0
        # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
        while (int(major_id) < 1) or (int(major_id) > len(results_majors)):
            major_id = get_parameter('идентификатор специальности')

        results_department = show_all_department()
        department_id = 0
        # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
        while (int(department_id) < 1) or (int(department_id) > len(results_department)):
            department_id = get_parameter('идентификатор факультета')

        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Students (Name, MajorID, DeptID) 
                                            VALUES (?, ?, ?)''',
                                            (new_student_name, major_id, department_id))
        conn.commit()
        print(f'[#] > Новый студент {new_student_name} успешно внесен в базу данных.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def show_all_students():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT 
                        Students.Name,
                        Departments.Name,
                        Majors.Name
                       FROM 
                        Students, Departments, Majors
                       WHERE
                        Students.DeptID == Departments.DeptID AND
                        Students.MajorID == Majors.MajorID''')
        results = cur.fetchall()
        if len(results) >= 1:
            show_results(results)
        else:
            print(f'[#] > Не одного студента нет в базе')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def find_student():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        student_name = get_parameter('имя студента')
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT 
                        Students.Name,
                        Departments.Name,
                        Majors.Name
                       FROM 
                        Students, Departments, Majors
                       WHERE
                        Students.DeptID == Departments.DeptID AND
                        Students.MajorID == Majors.MajorID AND
                        Students.Name LIKE ?''',
                        (f'%{student_name}%',))
        results = cur.fetchall()
        if len(results) >= 1:
            show_results(results)
        else:
            print(f'[#] > Совпадений не найдено.')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def update_student():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        update_student_name = get_parameter('имя студента')
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT Students.StudentID,
                              Students.Name,
                              Departments.Name,
                              Majors.Name
                            FROM
                              Students, Departments, Majors
                            WHERE
                              Students.DeptID == Departments.DeptID AND
                              Students.MajorID == Majors.MajorID AND
                              Students.Name LIKE ?''', (f'%{update_student_name}%',))
        results = cur.fetchall()
        if len(results) >= 1:
            show_results(results)
            id_update_student = get_parameter('идентификатор студента')
            new_name_student = get_parameter('имя студента')

            results_majors = show_all_majors()
            major_id = 0
            # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
            while (int(major_id) < 1) or (int(major_id) > len(results_majors)):
                major_id = get_parameter('идентификатор специальности')

            results_department = show_all_department()
            department_id = 0
            # Если вводится идентификатор которого нет в таблице, то запрашиваем id снова
            while (int(department_id) < 1) or (int(department_id) > len(results_department)):
                department_id = get_parameter('идентификатор факультета')
            if confirm('изменить'):
                cur.execute('''UPDATE Students 
                                SET 
                                    Name = ?,
                                    DeptID = ?,
                                    MajorID = ?
                                WHERE
                                    StudentID = ?''',
                                (new_name_student, department_id, major_id, id_update_student))
                conn.commit()
                print(f'Данные студента обновлены')
        else:
            print(f'Совпадений не найдено!')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def delete_student():
    conn = None
    try:
        conn = sqlite3.connect('../db/student_info.db')
        cur = conn.cursor()
        name_delete_student = get_parameter('имя студента')
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT Students.StudentID,
                        Students.Name,
                        Departments.Name,
                        Majors.Name
                       FROM
                        Students, Departments, Majors
                       WHERE
                        Students.DeptID == Departments.DeptID AND
                        Students.MajorID == Majors.MajorID AND
                        Students.Name LIKE ?''', (f'%{name_delete_student}%',))
        results = cur.fetchall()
        if len(results) >= 1:
            show_results(results)
            id_delete_student = 0
            while (int(id_delete_student) < 1) or (int(id_delete_student) > len(results)):
                id_delete_student = get_parameter('идентификатор студента')
            if confirm('удалить'):
                try:
                    cur.execute('DELETE FROM Students WHERE StudentID = ?', (id_delete_student,))
                    conn.commit()
                    print(f'Студент удален из базы данных!')
                except sqlite3.Error as err:
                    print(f'[#] > Ошибка базы данных: {err}')
                finally:
                    if conn is not None:
                        conn.close()
            else:
                print(f'[#] > Удаление отменено.')
        else:
            print(f'Студент не найден')
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()


def students_menu():
    while True:
        print()
        print(f'[#] > -- Меню студенты ')
        print(f'[1] > Добавить нового студента')
        print(f'[2] > Найти студента')
        print(f'[3] > Обновить информацию о студенте')
        print(f'[4] > Удалить студента')
        print(f'[5] > Показать всех студентов')
        print(f'[0] > Вернуться в предыдущее меню')
        choice = get_user_menu_choice(STUDENT_MIN_VALUE, STUDENT_MAX_VALUE)
        if choice == ADD_NEW_STUDENT:
            add_new_student()
        elif choice == FIND_STUDENT:
            find_student()
        elif choice == UPDATE_STUDENT:
            update_student()
        elif choice == DELETE_STUDENT:
            delete_student()
        elif choice == SHOW_ALL_STUDENTS:
            show_all_students()
        elif choice == BACK:
            main_menu()
''' Конeц блока работы со студентами '''


def main_menu():
    print()
    print(f'[#] > -- Основное меню')
    print(f'[1] > Работа с факультетами')
    print(f'[2] > Работа со специальностями')
    print(f'[3] > Работа со студентами')
    print(f'[0] > Выход')
    choice = get_user_menu_choice(MAIN_MIN_VALUE, MAIN_MAX_VALUE)
    if choice == DEPARTMENTS_MENU:
        dept_menu()
    elif choice == MAJORS_MENU:
        majors_menu()
    elif choice == STUDENTS_MENU:
        students_menu()


def main():
    start()
    main_menu()


if __name__ == '__main__':
    main()
