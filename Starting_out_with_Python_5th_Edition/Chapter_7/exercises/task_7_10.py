# Задание #10 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #10 to chapter 7
# The text of the task is in the file tasks_en.txt

FILE_NAME = '10. worldSeries_winners.txt'


def get_list(f_name):
    with open(f'dop\\{f_name}', 'r') as f_list:
        my_list = []
        for value in f_list:
            value = value.strip('\n')
            my_list.append(value)
    return my_list


def user_comand():
    return input(f'Введите название команды для поиска: ')


def show_result(my_list, user_comand):
    cout = 0
    for value in my_list:
        if user_comand == value:
            cout += 1
    if cout > 0:
        print(f'Команда {user_comand} побеждала в турнире {cout} раз')
    else:
        print(f'Команда {user_comand} не побеждала')


def main():
    my_list = get_list(FILE_NAME)
    user_data = user_comand()
    show_result(my_list, user_data)


if __name__ == '__main__':
    main()
