# Задание #2 к главе 7
# Текст задания находится в файле tasks_ru.txt
# - Доработка
# Добавлена возможность в ручную ввести количество номеров для генерации в лотерейном билете
#
# Task #2 to chapter 7
# The text of the task is in the file tasks_en.txt
# - Modification
# Added the ability to manually enter the number of numbers to generate in the lottery ticket

import random


def rnd_generator(numbers):
    ticket_number = []
    for i in range(numbers):
        ticket_number.append(random.randint(0, 9))
    return ticket_number


def show_number(t_num):
    print(f'Вый грешная комбинация: ', end='')
    for i in t_num:
        print(f'{i}\t', end='')


def main():
    how_many_numbers = int(input(f'Введите количество цифр в лотерейном билете: '))
    ticket_number = rnd_generator(how_many_numbers)
    show_number(ticket_number)


if __name__ == '__main__':
    main()
