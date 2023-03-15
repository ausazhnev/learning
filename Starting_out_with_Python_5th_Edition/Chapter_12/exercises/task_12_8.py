# Задание #8 к главе 12
# Текст задания находится в файле tasks_ru.txt
#
# Task #8 to chapter 12
# The text of the task is in the file tasks_en.txt

# Комментировать особо не чего, просто написал
# функцию в соответствии с описанием в задании
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def main():
    m = int(input(f'Введите значение для параметра \'m\': '))
    n = int(input(f'Введите значение для параметра \'n\': '))
    print(ackermann(m, n))


if __name__ == '__main__':
    main()
