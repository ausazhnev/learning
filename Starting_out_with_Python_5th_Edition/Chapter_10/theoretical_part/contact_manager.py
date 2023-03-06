# Эта программа управляет контактами

import pickle
import contact

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа для имени файла.
FILE_NAME = 'contacts.dat'


# Функция загружает создает словарь и если в файле
# присутствуют данные, расконсервирует их в словарь
def load_contacts():
    try:
        # Открыть файл contacts.dat или получить
        # исключение IOError если файл не найден
        with open(f'../dop/{FILE_NAME}', 'rb') as r_file:

            # Расконсервировать словаря
            contact_dct = pickle.load(r_file)

        # Мы не закрываем файл по тому что,
        # использовали пакетный менеджер with
        # r_file.close

    except IOError:
        # Не получилось открыть файл, поэтому
        # создать пустой словарь
        contact_dct = {}

    return contact_dct


# Функция save_contacts консервирует указанный
# объект и сохраняет его в файл контактов
def save_contacts(cont_list):
    # Открыть файл для записи
    with open(f'../dop/{FILE_NAME}', 'wb') as w_file:
        # Законсервировать словарь и сохранить его в файл
        pickle.dump(cont_list, w_file)
    # Мы не закрываем файл по тому что,
    # использовали пакетный менеджер with
    # w_file.close

    # Информируем пользователя о сохранении данных
    print(f'Данные сохранены в файл: {FILE_NAME}')


# Функция look_up отыскивает
# элементы в заданном словаре
def look_up(cont_list):
    # Получить искомое имя
    name = input(f'Введите имя: ')

    # Отыскать его в словаре
    print(f'{cont_list.get(name, "Запись в словаре не найдена.")}')


# Функция add добавляет новую
# запись в указанный словарь
def add(cont_list):
    # Получить контактную информацию
    name = input(f'Введите имя: ')
    phone = input(f'Введите телефон: ')
    email = input(f'Введите электронный адрес: ')

    # Создать именованную запись с объектом Contact
    entery = contact.Contact(name, phone, email)

    # Если имя в словаре не существует, то
    # добавить его в качестве ключа со связанным
    # с ним значением в виде объекта.
    if name not in cont_list:
        cont_list[name] = entery
        print(f'Запись добавлена.')
    else:
        print(f'Запись с таким именем уже существует.')


# Функция change изменяет существующую
# записи в указанном словаре.
def change(cont_list):
    # Получить искомое имя
    name = input(f'Введите имя: ')

    if name in cont_list:
        # Получить новый телефонный номер.
        phone = input(f'Введите новый телефонный номер: ')

        # Получить новый электронный адрес
        email = input(f'Введите новый электронный адрес: ')

        # Создать именованную запись с объектом Contact
        entery = contact.Contact(name, phone, email)

        # Обновить запись
        cont_list[name] = entery
        print(f'Информация обновлена.')
    else:
        print(f'Это имя не найдено.')


# Функция delete удаляет запись
# из указанного словаря
def delete(cont_list):
    # Получить искомое имя.
    name = input(f'Введите имя: ')

    # Если имя найдено, то удаляем запись
    if name in cont_list:
        del cont_list[name]
        print(f'Запись удалена.')
    else:
        print(f'Это имя не найдено.')


# Функция get_menu_choice выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print(f'Меню:')
    print(f'-----------------------------------')
    print(f'1. Найти контактное лицо')
    print(f'2. Добавить новое контактное лицо')
    print(f'3. Изменить существующее контактное лицо')
    print(f'4. Удалить контактное лицо')
    print(f'5. Выйти из программы')

    # Получить выбранный пользователем пункт меню
    choice = int(input(f'Введите выбранный пункт: '))

    # проверить выбранный пункт на допустимость.
    while 0 > choice > 5:
        choice = int(input(f'Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт
    return choice


def main():
    # Загрузить существующий словарь контактов
    # и присвоить его переменно my_contacts.
    my_contacts = load_contacts()
    # Инициализировать переменную для выбора пользователя.
    choice = 0

    # Обработать варианты выбора пунктов меню до тех пор,
    # пока пользователь не пожелает выйти из программы.
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработка выбранного варианта действий.
        if choice == LOOK_UP:
            look_up(my_contacts)
        elif choice == ADD:
            add(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)
        elif choice == DELETE:
            delete(my_contacts)

    # Сохранить словарь my_contacts в файле
    save_contacts(my_contacts)


if __name__ == '__main__':
    main()
