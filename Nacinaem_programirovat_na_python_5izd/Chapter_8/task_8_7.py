# Задание №7 к главе 8
# Текст задания находится в вайле tasks_ru.txt
# Символ переноса строки '\n' не участвует в подстчете пробелов
#
# Task №7 to Chapter 8
# The text of the task is in the file tasks_en.txt
# line break character '\n' does not count whitespace

FILE_NAME = 'text.txt'


def read_file():
    f_data = open(f'dop\\{FILE_NAME}', 'r')
    data_in_file = ''
    for line in f_data:
        line = line.strip()
        data_in_file += line
    f_data.close()
    return data_in_file


def analiyze(data):
    total_upper = 0
    total_lower = 0
    total_num = 0
    total_space = 0
    for ch in data:
        if ch.isupper():
            total_upper += 1
        if ch.islower():
            total_lower += 1
        if ch.isdigit():
            total_num += 1
        if ch.isspace():
            total_space += 1
    show_result('Всего букв в верхнем регистре: ', total_upper)
    show_result('Всего букв в нижнем регистре: ', total_lower)
    show_result('Всего  цифр: ', total_num)
    show_result('Всего пробелов: ', total_space)


def show_result(message, value):
    print(f'[#] > {message} {value}')


def main():
    data_in_file = read_file()
    analiyze(data_in_file)


if __name__ == '__main__':
    main()
