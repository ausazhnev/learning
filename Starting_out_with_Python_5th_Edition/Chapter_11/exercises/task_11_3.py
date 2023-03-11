# Задание #3 к главе 11
# Текст задания находится в файле tasks_ru.txt
# Описание класса Person и класса Customer находится
# в файле 'modul_11_3.py'
#
# Task #3 to chapter 11
# The text of the task is in the file tasks_en.txt
# The description of the Person class and the Customer
# class is in file 'modul_11_3.py'

import modul_11_3 as my_modul


def main():
    print(f'Добро пожаловать в систему рассылок.\n'
          f'====================================\n'
          f'Введите данные нового пользователя:\n'
          )
    new_user = my_modul.Customer()
    new_user.set_name(input(f'Введите имя пользователя: '))
    new_user.set_address(input(f'Введите адрес пользователя: '))
    new_user.set_phone(input(f'Введите номер телефона пользователя: '))
    new_user.set_id_num(input(f'Введите id для пользователя: '))
    choice = input(f'Добавить пользователя в список рассылки? (д/н) ')
    if choice.lower() == 'д':
        choice = True
    else:
        choice = False
    new_user.set_mailing(choice)
    print(f'Благодарим за предоставленную информацию.\n'
          f'сообщения будут приходить на номер: {new_user.get_phone()}'
          )
    if new_user.get_mailing():
        print(f'мы рады что вы подписались на нашу рассылку.')
    else:
        print(f'Нам жаль, что вы не подписались на рассылку.\n'
              f'В личном кабинете вы всегда сможете это сделать.'
              )


if __name__ == '__main__':
    main()
