# Задание #4 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходный файл для анализа 'dop\text_9_5.txt'
#
# Task #4 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source file for analysis 'dop\text_9_5.txt'

# список спецсимволов которые будут удаляться из текста
MARKS = ':;!@#$%^&*()_-=+<>.,`*?—\\/"\n'


# Получаем все данные из фала одним списком
def get_data_from_file():
    with open('dop\\text_9_5.txt', 'r', encoding='utf8') as file:
        data = file.readlines()
        return data


# получаем данные и добавлям в словарь новую пару ключ: значение если такой нет со значением 1
# если ключ есть в словаре, то увеличиваем его значение на 1
def add_in_dict(value, cout_dict):
    if value not in cout_dict:
        cout_dict[value] = 1
    else:
        cout_dict[value] = cout_dict.get(value) + 1


# разбираем полученный список на строки и плова
# удаляем все знаки препинания которые хранятся в MARKS
# и передаем в функцию add_in_dict что бы добавить данные в словарь
def del_makrs(data, cout_dict):
    for line in data:
        for word in line.split():
            word = word.strip(MARKS)
            add_in_dict(word.lower(), cout_dict)


# пользователь выбирает отобразить на экране или сохранить в файл
def user_change():
    u_change = input(f'[#] ------------------------------- [#]\n'
                     f'[#] > Как вы хотите получить данные:\n'
                     f'[#] > [1] - Вывести на экран\n'
                     f'[#] > [2] - Сохранить в файл\n'
                     f'[#] > [3] - Вывести на экран и сохранить в файл\n'
                     f'[#] > > '
                     )
    if u_change.isdigit() and (int(u_change) > 0 or int(u_change) <= 3):
        return int(u_change)
    else:
        user_change()


# Выводит на экран содержимое словаря cout_dict
def show_result(cout_dict):
    for k, v in cout_dict.items():
        print(f'[#] > {k} \t {v}')


# Вывод словаря cout_dict в файл
def create_file(cout_dict):
    with open('dop\\dict_9_5.txt', 'w', encoding='utf8') as f_dict:
        for k, v in cout_dict.items():
            f_dict.write(f'{k}\t{v}\n')


def main():
    cout_dict = {}
    data = get_data_from_file()
    del_makrs(data, cout_dict)
    change = user_change()
    if change == 1:
        show_result(cout_dict)
    elif change == 2:
        create_file(cout_dict)
    elif change == 3:
        show_result(cout_dict)
        create_file(cout_dict)


if __name__ == '__main__':
    main()
