# Задание #7 к главе 10
# Текст задания находится в файле tasks_ru.txt
#
# Task #7 to chapter 10
# The text of the task is in the file tasks_en.txt

import m_employee_10_4 as employee
import pickle

FILE_NAME = 'office_dict.dat'


# Получаем данные из бинарного файла и собираем словарь
def load_dict():
    work_dict = {}
    end_of_file = False
    with open(f'../dop/{FILE_NAME}', 'rb') as file:
        while not end_of_file:
            try:
                data = pickle.load(file)
                work_dict.update(data)
            except EOFError:
                end_of_file = True
            except FileNotFoundError:
                print(f'[#] > Обнаружен первый запуск программы. . .\n'
                      f'[#] > Файлы окружения созданы.'
                      )
    return work_dict


# При завершении работы программы (> 0 в меню)
# консервируем данные в файл F_NAME
def save_dict(office_dict):
    with open(f'../dop/{FILE_NAME}', 'wb') as file:
        pickle.dump(office_dict, file)


# Поиск записи в словаре и вывод объекта если запись найдена
def find(office_dict):
    # Проверяем есть ли имя уже в словаре
    ident = input(f'[#] > Введите идентификационный номер:\n'
                  f'[#] > > '
                  )
    if ident in office_dict:
        data = office_dict.get(ident)
        print(data)
    else:
        print(f'[#] > Идентификационный номер не найден в справочнике.')


# Добавление новую запись в словарь
def add(office_dict):
    # Проверяем есть ли имя уже в словаре
    ident = input(f'[#] > Введите идентификационный номер:\n'
                  f'[#] > > '
                  )
    if ident not in office_dict:
        name = input(f'[#] > Введите имя:\n'
                     f'[#] > > '
                     )
        department = input(f'[#] > Введите отдел в котором работает сотрудник:\n'
                           f'[#] > > '
                           )
        office = input(f'[#] > Введите должность сотрудника:\n'
                       f'[#] > > '
                       )
        # Создаем объект класса
        new_contact = employee.Employee(name, ident, department, office)
        office_dict[ident] = new_contact
        print(f'[#] > Запись с идентификационным номером {ident} добавлена в справочник.')
    else:
        print(f'[#] > Идентификационный номер уже зарегистрировано в словаре.')


# Изменяем объект в словаре
def change(office_dict):
    # Проверяем есть ли имя уже в словаре
    ident = input(f'[#] > Введите идентификационный номер:\n'
                  f'[#] > > '
                  )
    if ident not in office_dict:
        name = input(f'[#] > Введите имя:\n'
                     f'[#] > > '
                     )
        department = input(f'[#] > Введите отдел в котором работает сотрудник:\n'
                           f'[#] > > '
                           )
        office = input(f'[#] > Введите должность сотрудника:\n'
                       f'[#] > > '
                       )
        # Создаем объект класса
        new_contact = employee.Employee(name, ident, department, office)
        office_dict[ident] = new_contact
        print(f'[#] > Запись с идентификационным номером {ident} изменена.')
    else:
        print(f'[#] > Идентификационный номер не найден в словаре.')


# удалить объект в словаре
def delete(office_dict):
    # Проверяем есть ли имя уже в словаре
    ident = input(f'[#] > Введите идентификационный номер:\n'
                  f'[#] > > '
                  )
    if ident in office_dict:
        del office_dict[ident]
        print(f'[#] > Запись с идентификационным номером {ident} удалена.')
    else:
        print(f'[#] > Идентификационный номер не найден в словаре.')


# Интерфейс меню пользователя. Проверка корректности
# выбора интегрирована в функцию через рекурсию
def menu():
    u_data = input(f'[#] ------------------------------------------------ [#]\n'
                   f'[#] > Выберете действие:\n'
                   f'[#] > [1] Найти данные сотрудника\n'
                   f'[#] > [2] Добавить нового сотрудника\n'
                   f'[#] > [3] Изменить данные существующий сотрудника\n'
                   f'[#] > [4] Удалить сотрудника из справочника\n'
                   f'[#] > [0] Выход\n'
                   f'[#] > > '
                   )
    if u_data.isdigit() and (0 <= int(u_data) <= 4):
        print(f'[#] > Выбор принят . . . ')
        return int(u_data)
    else:
        u_data = menu()
        return u_data


def main():
    office_dict = load_dict()
    u_change = menu()
    while u_change != 5:
        u_change = menu()
        if u_change == 1: find(office_dict)
        elif u_change == 2: add(office_dict)
        elif u_change == 3: change(office_dict)
        elif u_change == 4: delete(office_dict)
    save_dict(office_dict)


if __name__ == '__main__':
    main()
