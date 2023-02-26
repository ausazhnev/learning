# Задание (RU)
# 12. Генерация простого числа.
# Натуральное (целое положительное) число является простым, если оно имеет деление кроме 1 и самого себя. Натуральное
# (целое положительное) число является составным, если оно не является простым. Напишите программу, которая просит
# пользователя ввести целое число больше 1 и затем выводит все простые числа, которые меньше или равны введенному числу.
# Программа должна работать следующим образом:
#  - После того как пользователь ввел число, программа должна заполнить список всеми целыми числами начиная с 2 и до
#  введенного значения
#  - Затем программа должна применить цикл, что бы пройти по списку. Каждый элемент должен быть в цикле передан в
#  функцию, которая определяет и сообщает, что элемент является простым числом или составным.
#
# Task (EN)
# 12. Generation of a prime number.
# A natural (positive integer) number is prime if it has a division other than 1 and itself. A natural
# (positive integer) number is composite if it is not prime. Write a program that asks the user to enter an integer
# greater than 1 and then outputs all prime numbers that are less than or equal to the entered number.
# The program should work like this:
#   - After the user has entered a number, the program should fill the list with all integers starting from 2 and
#   up to the entered value
#   - The program should then apply a loop to iterate through the list. Each element must be looped through to a
#   function that determines and reports whether the element is prime or composite.


def check(num, user_num):
    if num == 2 or num == 3 or num == 5:
        print(f' {num}', end='')
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        print(f' {num}', end='')


def get_num():
    num = int(input(f'Введите целое не отрицательное число больше 1: '))
    while num <= 1:
        print(f'Введено некорректное число')
        num = int(input(f'Введите целое не отрицательное число больше 1: '))
    return num


def main():
    user_num = get_num()
    num_list = [i for i  in range(2, user_num+1)]
    print(f'Список простых числел в последовательности от 2 до {user_num}:')
    for num in num_list:
        check(num, user_num)

if __name__ == '__main__':
    main()
