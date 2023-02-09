# Задание (RU)
# Поиск имени.
# "8. girl_names.txt" - имена девочек, "8. boy_names.txt" - имена мальчиков. находятся в директории "dop\"
# Напишите программу, которая считает содержимое из этих двух файлов в два отдельных списка. Пользователь должен
# иметь возможность ввести имя мальчика или девочки или оба имени, приложение должно вывести на экран сообщение о том,
# что введенные имена находятся среди самых популярных.
#
# Task (EN)
# Name search.
# "8. girl_names.txt " - girls' names, "8. boy_names.txt " - the names of the boys. located in the "dop\" directory
# Write a program that counts the contents of these two files into two separate lists. The user should be able to
# enter the name of a boy or a girl or both names, the application should display a message that the names entered
# are among the most popular.


def get_list(f_name):
    f_data = open(f'dop\\{f_name}', 'r')
    list_data = []
    for value in f_data:
        value = value.strip('\n')
        list_data.append(value)
    f_data.close()
    return list_data

def check_names(boys_name_list, girls_name_list, chldren_names):
    if chldren_names != '':
        for i in range(len(chldren_names)):
            if (chldren_names[i] in boys_name_list) or\
                    (chldren_names[i] in girls_name_list): print(f'{chldren_names[i]} есть в списке')
    else: print(f'Вы не ввели имена')


def get_user_data():
    children_list = []
    print(f'Вводите имена детей:')
    boy_name = input(f'Введите имя мальчика: ')
    if boy_name != '': children_list.append(boy_name)
    girl_name = input(f'Введите имя девочки: ')
    if girl_name != '': children_list.append(girl_name)
    return children_list


def main():
    boys_name_list = get_list('8. boy_names.txt')
    girls_name_list = get_list('8. girl_names.txt')
    children_names = get_user_data()
    check_names(boys_name_list, girls_name_list, children_names)


if __name__ == '__main__':
    main()
