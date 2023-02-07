# Задание (RU)
# Генератор лотырейных билетов.
# Разработайте программу, которая генерирует семизначную комбинацию лотырейных числе. Программа должна сгенерировать
# семь случайных числе, каждое в диапозоне от 0 до 9, и просвоить каждое число элементу списка. Затем напишите
# еще один цикл, который показывает содержимое списка.
#
# Task (EN)
# Lottery ticket generator
# Develop a program that generates a seven-digit combination of lottery numbers. The program must generate
# seven random numbers, each in the range 0 to 9, and assign each number to an element of the list.
# Then write another loop that shows the contents of the list.

import random


def rnd_generator(numbers):
    ticket_number = []
    for i in range(numbers):
        ticket_number.append(random.randint(0, 9))
    return ticket_number


def show_number(t_num):
    print(f'Выйгрешная комбинация: ', end='')
    for i in t_num:
        print(f'{i}\t', end='')


def main():
    ticket_number = rnd_generator(7)
    show_number(ticket_number)


if __name__ == '__main__':
    main()