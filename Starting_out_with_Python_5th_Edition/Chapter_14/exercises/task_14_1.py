# Задание #1 к главе 14
# Текст задания находится в файле tasks_ru.txt
# Скрипт для создания базы данных можно (../dop/create_cities.ry)
#
# Task #1 to chapter 14
# The text of the task is in the file tasks_en.txt
# Script to create a database can be (../dop/create_cities.ry)

import sqlite3

CITIES_LIST_UP = 1
CITIES_LIST_DN = 2
CITIES_LIST_NAME = 3
TOTAL_POPULATION = 4
AVERAGE_POPULATION = 5
CITY_MAX_POPULATION = 6
CITY_MIN_POPULATION = 7
EXIT = 0
MIN_VALUES = 0
MAX_VALUES = 7


def show_menu():
    print()
    print(f'----------------------------- Основное меню -----------------------------')
    print(f'[1] > Список городов отсортированных по возрастанию численности населения')
    print(f'[2] > Список городов отсортированных по убыванию численности населения')
    print(f'[3] > Список городов отсортированных по названиям')
    print(f'[4] > Общая численность населения всех городов')
    print(f'[5] > Средняя численность населения всех городов')
    print(f'[6] > Город с наибольшей численностью населения')
    print(f'[7] > Город с наименьшей численностью населения')
    print(f'[0] > Выход')


def get_user_menu_choice():
    print(f'[#] > Введите выбранное значение от {MIN_VALUES} до {MAX_VALUES}: ')
    choice = int(input('[#] > > '))
    while choice < MIN_VALUES or choice > MAX_VALUES:
        print(f'[#] > Введено некорректное значение')
        print(f'[#] > Введите выбранное значение от {MIN_VALUES} до {MAX_VALUES}: ')
        choice = int(input('[#] > > '))
    return int(choice)


def show_sql_result(results):
    for row in results:
        print(f'[#] > ', end='')
        for i in range(len(results[0])):
            print(f'{row[i]:<20}', end='')
        print()


def get_data_from_table(sql_request):
    conn = None
    try:
        conn = sqlite3.connect('../db/cities.db')
        cur = conn.cursor()
        cur.execute(sql_request)
        results = cur.fetchall()
    except sqlite3.Error as err:
        print(f'[#] > Ошибка базы данных: {err}')
    finally:
        if conn is not None:
            conn.close()
        show_sql_result(results)


def main():
    choice = None
    while choice != 0:
        show_menu()
        choice = get_user_menu_choice()
        # Используем вызов одной функции передавая в нее текст sql запроса
        # меняющийся в зависимости от выбора пользователя
        if choice == CITIES_LIST_UP:
            get_data_from_table('''SELECT CityName, Population FROM Cities 
                                        ORDER BY Population DESC''')
        elif choice == CITIES_LIST_DN:
            get_data_from_table('''SELECT CityName, Population FROM Cities 
                                        ORDER BY Population''')
        elif choice == CITIES_LIST_NAME:
            get_data_from_table('''SELECT CityName FROM Cities ORDER BY CityName''')
        elif choice == TOTAL_POPULATION:
            get_data_from_table('''SELECT SUM(Population) FROM Cities''')
        elif choice == AVERAGE_POPULATION:
            get_data_from_table('''SELECT AVG(Population) FROM Cities''')
        elif choice == CITY_MAX_POPULATION:
            get_data_from_table('''SELECT CityName, Population FROM Cities
                                        ORDER BY Population DESC 
                                        LIMIT 1''')
        elif choice == CITY_MIN_POPULATION:
            get_data_from_table('''SELECT CityName, Population FROM Cities
                                        ORDER BY Population 
                                        LIMIT 1''')


if __name__ == '__main__':
    main()
