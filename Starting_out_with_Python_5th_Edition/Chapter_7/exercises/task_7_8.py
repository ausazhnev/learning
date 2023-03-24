# Задание #8 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #8 to chapter 7
# The text of the task is in the file tasks_en.txt


def get_list(f_name):
    with open(f'dop\\{f_name}', 'r') as f_data:
        list_data = []
        for value in f_data:
            value = value.strip('\n')
            list_data.append(value)
    return list_data


def check_names_in_lists(boys_name_list, girls_name_list, chldren_names):
    if chldren_names != '':
        for i in range(len(chldren_names)):
            if (chldren_names[i] in boys_name_list) or\
                    (chldren_names[i] in girls_name_list):
                print(f'{chldren_names[i]} есть в списке')
    else:
        print(f'Вы не ввели имена')


def get_user_data():
    children_list = []
    print(f'Вводите имена детей:')
    boy_name = input(f'Введите имя мальчика: ')
    if boy_name != '':
        children_list.append(boy_name)
    girl_name = input(f'Введите имя девочки: ')
    if girl_name != '':
        children_list.append(girl_name)
    return children_list


def main():
    boys_name_list = get_list('8. boy_names.txt')
    girls_name_list = get_list('8. girl_names.txt')
    children_names = get_user_data()
    check_names_in_lists(boys_name_list, girls_name_list, children_names)


if __name__ == '__main__':
    main()
