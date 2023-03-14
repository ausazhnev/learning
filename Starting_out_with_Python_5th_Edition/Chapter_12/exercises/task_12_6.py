# Задание #6 к главе 12
# Текст задания находится в файле tasks_ru.txt
#
# Task #6 to chapter 12
# The text of the task is in the file tasks_en.txt


# Базовым случаем является момент когда
# число становится равным 1
def sum_of_number(num):
    if num != 1:
        # До тех пор, пока число не равно 1, возвращаем
        # сумму текущего числа и результата функции с
        # числом уменьшенным на 1
        return num + sum_of_number(num-1)
    else:
        # Достигнут базовый случай, заданное
        # число становится равным 1
        return num


def main():
    num = int(input(f'Введите целое число неотрицательное число: '))
    print(sum_of_number(num))


if __name__ == '__main__':
    main()
