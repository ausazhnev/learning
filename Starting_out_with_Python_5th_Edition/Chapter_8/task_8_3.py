# RU
# Задание №1 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# EN
# Task №1 to chapter 8
# The text of the task is in the file tasks_en.txt

MONTHS = ('Января', 'Февряля', 'Марта', 'Апреля', 'Мая', 'Июня',
          'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'
          )


def get_user_data():
    user_data = input(f'Введите дату в формате ДД/ММ/ГГГГ: ')
    return user_data


def conversion(data):
    data = data.split('/')
    return f'{data[0]} {MONTHS[int(data[1])-1]} {data[2]} года'


def show_result(data):
    print(data)


def main():
    user_data = get_user_data()
    new_format = conversion(user_data)
    show_result(new_format)


if __name__ == '__main__':
    main()
