# Задание #2 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #2 to chapter 7
# The text of the task is in the file tasks_en.txt

import random


def rnd_generator(numbers):
    ticket_number = []
    for i in range(numbers):
        ticket_number.append(random.randint(0, 9))
    return ticket_number


def show_number(t_num):
    print(f'Выигрышная комбинация: ', end='')
    for i in t_num:
        print(f'{i}\t', end='')


def main():
    ticket_number = rnd_generator(7)
    show_number(ticket_number)


if __name__ == '__main__':
    main()
