# работа со словорями создание и редактирования списка дней рождений

# working with dictionaries creating and editing a list of birthdays

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def add(birthdays):
    name = input(f'[#] > Введите имя друга\n'
                 f'[#] > > ')
    bday = input(f'[#] > Введите день рождения друга\n'
                 f'[#] > > ')
    if name in birthdays:
        print(f'[#] > Друг {name} уже в списке')
    else:
        birthdays[name] = bday


def look_up(birthdays):
    name = input(f'[#] > Введите имя друга\n'
                 f'[#] > > ')
    print(f'[#] > {birthdays.get(name, "Друг с таким именем не найден")}')


def change(birthdays):
    name = input(f'[#] > Введите имя друга\n'
                 f'[#] > > ')
    if name in birthdays:
        bday = input(f'[#] > Введите день рождения друга\n'
                     f'[#] > > ')
        birthdays[name] = bday
    else:
        print(f'[#] > Друг {name} не найден в списке')


def delete(birthdays):
    name = input(f'[#] > Введите имя друга\n'
                 f'[#] > > ')
    if name in birthdays:
        del birthdays[name]
    else:
        print(f'[#] > Друг {name} не найден в списке')


def get_user_choice():
    print(f'[#] ---------------------------- [#]\n'
          f'[#] > Друзья и их дни рождения\n'
          f'[#] > [1] - Найти день рожджения\n'
          f'[#] > [2] - Добавить день пождения\n'
          f'[#] > [3] - Изменить день рождения\n'
          f'[#] > [4] - Удалить день рождения\n'
          f'[#] > [5] - Выход'
          )
    user_change = input(f'[#] > > ')
    while (not user_change.isdigit()) or \
            (int(user_change) < LOOK_UP or int(user_change) > QUIT):
        print(f'[#] > Некорректный ввод!')
        user_change = input(f'[#] > > ')
    return int(user_change)


def main():
    birthdays = {}
    user_choice = 0
    while user_choice != QUIT:
        user_choice = get_user_choice()
        if user_choice == LOOK_UP:
            look_up(birthdays)
        elif user_choice == ADD:
            add(birthdays)
        elif user_choice == CHANGE:
            change(birthdays)
        elif user_choice == DELETE:
            delete(birthdays)
        elif user_choice == QUIT:
            print(f'[#] > Закрываем протокол комуникации. . .')


if __name__ == '__main__':
    main()
