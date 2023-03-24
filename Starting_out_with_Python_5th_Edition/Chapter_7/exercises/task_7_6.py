# Задание #6 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #6 to chapter 7
# The text of the task is in the file tasks_en.txt

def more_n(test_list, n_num):
    for value in test_list:
        if value > n_num:
            print(f'{value}\t', end='')


# для теста
my_list = [1, 54, 12, 5, 18, 84, 11]
n = 10
more_n(my_list, n)
