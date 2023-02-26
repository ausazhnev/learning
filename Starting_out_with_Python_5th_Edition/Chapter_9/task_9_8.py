# Задание #8 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Консервирование производится в файл 'dop/mail.dat'
#
# Task #8 to chapter 9
# The text of the task is in the file tasks_en.txt
# Preservation is done in the file 'dop/mail.dat'

# модуль pickle требуется для работы с байт кодом
import pickle

F_NAME = 'mail.dat'
# словарь объявляется вне функций, это позволяет
# обращаться к нему из любой части программы
dict_email = {}


# получаем данные из бинарного файла и собираем словарь
def decoding_file():
    # флаг окончания файла
    end_of_file = False
    with open(f'dop\\{F_NAME}', 'rb') as file:
        while not end_of_file:
            try:
                mail = pickle.load(file)
                # добавляем рабочий словарь dict_email новую порцию данных
                dict_email.update(mail)
            except EOFError:
                end_of_file = True
            except FileNotFoundError:
                print(f'[#] > Обнаружен первый запуск программы. . .\n'
                      f'[#] > Файлы окружения созданы.')


# поиск электронного адреса в словаре по введенному пользователем ключу
def find_email():
    search_name = input(f'[#] > Введите имя контака который хотите найти\n'
                        f'[#] > > '
                        )
    print(f'[#] > Поиск . . . ')
    if dict_email.get(search_name):
        print(f'[#] > Адрес электронной почты {search_name} - {dict_email.get(search_name)}')
    else:
        print(f'[#] > Контакт {search_name} в вашей запискной книге не найден')


# добавление в словарь новой пары значений
def add_email():
    name = input(f'[#] > Введите имя контакта:\n'
                 f'[#] > > '
                 )
    # проверяем есть ли такой ключ в словаре
    if not dict_email.get(name):
        user_mail = input(f'[#] > Введите адрес электронной почты:\n'
                          f'[#] > > '
                          )
        dict_email[name] = user_mail
    else:
        print(f'[#] > {name} уже есть в списке')


# изменение электронного адреса для записи в словаре
def change_email():
    name = input(f'[#] > Введите имя контакта:\n'
                 f'[#] > > '
                 )
    print(f'[#] > Обработка. . .')
    if dict_email.get(name):
        user_mail = input(f'[#] > Введите адрес электронной почты:\n'
                          f'[#] > > '
                          )
        dict_email[name] = user_mail
        print(f'[#] > Электронная почта для контакта{name} изменена')
    else:
        print(f'[#] > {name} не найден в списке')


# удаление пары ключ - значение из словаря
def del_email():
    name = input(f'[#] > Введите имя контакта:\n'
                 f'[#] > > '
                 )
    print(f'[#] > Обработка. . .')
    del dict_email[name]
    print(f'Запись {name} удалена.')


# при завершении работы программы (> 0 в меню) консервируем данные в файл F_NAME
def end_prog():
    with open(f'dop\\{F_NAME}', 'wb') as file:
        pickle.dump(dict_email, file)
        print(f'[#] > Завершен протокол коммуникации. . .')

# интерфейс меню пользователя
# проверка корректности выбора интегрирована в функцию через рекурсию
def menu():
    u_data = input(f'[#] ------------------------------------------------ [#]\n'
                   f'[#] > Выберете действие:\n'
                   f'[#] > [1] Найти адрес электронной почты по получателю\n'
                   f'[#] > [2] Добавить новый адрес электронной почты\n'
                   f'[#] > [3] Изменить существующий адрес электронной почты\n'
                   f'[#] > [4] Удалить существующий адрес электронной почты\n'
                   f'[#] > [0] Выход\n'
                   f'[#] > > '
                   )
    if u_data.isdigit() and (0 <= int(u_data) <= 4):
        print(f'[#] > Выбор принят . . . ')
        return int(u_data)
    else:
        u_data = menu()
        return u_data

# основная функция программы
def main():
    user_choice = None
    decoding_file()
    while user_choice != 0:
        user_choice = menu()
        if user_choice == 1: find_email()
        elif user_choice == 2: add_email()
        elif user_choice == 3: change_email()
        elif user_choice == 4: del_email()
        elif user_choice == 0: end_prog()


if __name__ == '__main__':
    main()
