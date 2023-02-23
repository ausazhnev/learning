# Задание #6 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходные файл для анализа 'dop\text_9_6_1.txt' и 'dop\text_9_6_2.txt'
#
# Task #6 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source files for analysis 'dop\text_9_6_1.txt' and 'dop\text_9_6_2.txt'

F_NAME_1 = 'text_9_6_1.txt'
F_NAME_2 = 'text_9_6_2.txt'
MARKS = ':;!@#$%^&*()_-=+<>.,`*?—\\/"\n'


# получаем данные из файла, удаляем спец символы и собираем во множество
def get_set(f_name):
    f_set = set()
    with open(f'dop\\{f_name}', 'r', encoding='utf8') as file:
        data = file.readlines()
        for line in data:
            for word in line.split():
                word = word.strip(MARKS)
                f_set.add(word.lower())
    return f_set


# меню пользователя, выбор какие данные получить
def menu():
    u_change = input(f'[#] --------------------------------------------------------------- [#]\n'
                     f'[#] > Какие данные вы хотите получить:\n'
                     f'[#] > [1] - Показать список всех уникальных слов, содержащихся обоими '
                     f'файлами\n'
                     f'[#] > [2] - Показать список слов, входящих в оба файла\n'
                     f'[#] > [3] - Показать список слов из первого файла, не входящих во '
                     f'второй\n'
                     f'[#] > [4] - Показать список слов из второго файла, не входящих в первый '
                     f'файл\n'
                     f'[#] > [5] - Показать список слов, входящих либо в первый либо во второй '
                     f'файл, но не входящих в оба файла одновременно\n'
                     f'[#] > > '
                     )
    if u_change.isdigit() and (1 <= int(u_change) <= 5):
        return int(u_change)
    else:
        u_change = menu()
        return u_change


def show_result(set_1, set_2, operation):
    print(f'[#] > Ответ на запрос. . .\n'
          f'[#] ---------------------------------------------------------------- [#]')
    if operation == 1: result_set = set_1 | set_2    # альтернативная запись set_1.union(set_2)
    elif operation == 2: result_set = set_1 & set_2  # альтернативная запись set_1.intersection(set_2)
    elif operation == 3: result_set = set_1 - set_2  # альтернативная запись set_1.difference(set_2)
    elif operation == 4: result_set = set_2 - set_1  # альтернативная запись set_2.difference(set_1)
    elif operation == 5: result_set = set_1 ^ set_2  # set_1.symmetric_difference(set_2)
    for word in result_set:
        print(f'[#] > {word}')


def main():
    set_f_1 = get_set(F_NAME_1)
    set_f_2 = get_set(F_NAME_2)
    u_change = menu()
    show_result(set_f_1, set_f_2, u_change)


if __name__ == '__main__':
    main()
