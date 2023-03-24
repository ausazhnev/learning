# Задание #12 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #12 to chapter 7
# The text of the task is in the file tasks_en.txt


def check(num):
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
    num_list = [i for i in range(2, user_num+1)]
    print(f'Список простых чисел в последовательности от 2 до {user_num}:')
    for num in num_list:
        check(num)


if __name__ == '__main__':
    main()
