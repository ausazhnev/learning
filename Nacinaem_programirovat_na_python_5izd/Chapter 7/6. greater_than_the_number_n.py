# Задание (RU)
# Больше числа n
# В программе напишите функцию, которая принимает два аргумента: список и число 'n'.
# Допустим, что список содержит числа. Функция должна показать все числа в списке, которые больше чем 'n'
#
#
# Task (EN)
# Greater than the number n
# In the program, write a function that takes two arguments: a list and a number 'n'.
# Let's assume that the list contains numbers. The function should show all the numbers in the list that are
# greater than 'n'

def more_n(test_list, n_num):
    for value in test_list:
        if value > n_num:
            print(f'{value}\t', end='')


# для теста
my_list = [1, 54, 12, 5, 18, 84, 11]
n = 10
