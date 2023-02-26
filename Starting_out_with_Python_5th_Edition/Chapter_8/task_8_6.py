# Задание №6 к главе 8
# Текст задания находится в вайле tasks_ru.txt
#
# Task №6 to Chapter 8
# The text of the task is in the file tasks_en.txt

FILE_NAME = 'text.txt'


def read_file():
    cout_line = 0
    coet_word = 0
    f_data = open(f'dop\\{FILE_NAME}', 'r')
    for line in f_data:
        cout_line += 1
        word_in_line = len(line.split())
        coet_word += word_in_line
    f_data.close()
    return cout_line, coet_word


def calculation(lines, words):
    return words / lines


def show_result(data):
    print(f'Среднее количество слов в предложении: {data:.0f}')


def main():
    line_in_file, word_in_file = read_file()
    result = calculation(line_in_file, word_in_file)
    show_result(result)


if __name__ == '__main__':
    main()
