# RU
# Задание №1 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# EN
# Task №1 to chapter 8
# The text of the task is in the file tasks_en.txt

def converter(user_data):
    initials = ''
    user_data = user_data.split()
    for value in user_data:
        initials += value[0] + '.'
    return initials


def show_initials(initials):
    print(initials.upper())


def get_full_name():
    full_name = input(f'Введите свои Фамилию Имя Отчество: ')
    full_name = full_name
    return full_name


def main():
    full_name = get_full_name()
    initials = converter(full_name)
    show_initials(initials)


if __name__ == '__main__':
    main()
