# Задание (RU)
# 10. Чемпионы мировой серии.
# Файл "dop/10. worldSeries_winners.txt" содержит хронологический список команд-победителей мировой серии по бейсболу
# с 1093 по 2009 г. (Первая строка в файле является название команды которая победила в 1903 году, а последняя строка
# название команды которая победила в 2009 году. Обратите внимание, мировая серия не проводилась в 1904 и 1994 годах)
# Напишите программу которая позволяет пользователю ввести название команды и затем выводит на экран количество лет,
# когда команда побеждала в мировой серии, в течении указанного периода с 1903 по 2009 год.
#
# Task (EN)
# 10. World Series Champions.
# The file "dop/10. worldSeries_winners.txt" contains a chronological list of the World Series of Baseball winning teams
# from 1093 to 2009. (The first line in the file is the name of the team that won in 1903, and the last line is the
# name of the team that won in 2009. Note attention, the world series was not held in 1904 and 1994)
# Write a program that allows the user to enter a team name and then displays the number of years the team won the
# World Series during the specified period from 1903 to 2009.

FILE_NAME = '10. worldSeries_winners.txt'


def get_list(f_name):
    f_list = open(f'dop\\{f_name}', 'r')
    my_list = []
    for value in f_list:
        value = value.strip('\n')
        my_list.append(value)
    f_list.close()
    return my_list


def user_comand():
    return input(f'Введите название команды для поиска: ')


def show_result(my_list, user_comand):
    cout = 0
    for value in my_list:
        if user_comand == value:
            cout += 1
    if cout > 0: print(f'Команда {user_comand} побеждала в турниере {cout} раз')
    else: print(f'Команда {user_comand} не побеждала')

def main():
    my_list = get_list(FILE_NAME)
    user_data = user_comand()
    show_result(my_list, user_data)

if __name__ == '__main__':
    main()

