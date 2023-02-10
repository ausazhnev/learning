# Задание (RU)
# 11. Магический квадрат Ло Шу.
# Магический квадрат Ло Шу представляет собой таблицу с 3 строками и 3 столбцами.
# Магический квадрат Ло Шу имеет свойства:
#  - таблица содержит числа от 1 до 9
#  - Сумма каждой строки,  каждого столбца и каждой диагонали в итоге составляют одно и то же число.
# Магический квадрат можно сымитировать в программе при помощи двумерного списка. Напишите функция, которая
# принимает двумерный список в качестве аргумента и определяет, является ли список магическим квадратом Ло Шу.
# Протестируйте функцию в программе.
# Ло Шу последовательность
# 4   9   2
# 3   5   7
# 8   1   6
#
# Task (EN)
# 11. Lo Shu Magic Square.
# Lo Shu's magic square is a table with 3 rows and 3 columns. The Lo Shu magic square has the following properties:
#   - the table contains numbers from 1 to 9
#   - The sum of each row, each column, and each diagonal adds up to the same number.
# The magic square can be simulated in the program using a two-dimensional list. Write a function that takes a 2D
# list as an argument and determines if the list is a Lo Shu magic square. Test the function in the program.
# Lo Shu sequence
# 4   9   2
# 3   5   7
# 8   1   6


def check(data):
    if sum(data[0]) == sum(data[1]) == sum(data[2]) == \
            (data[0][0] + data[1][1] + data[2][2]) == \
            (data[2][0] + data[1][1] + data[0][2]):
        print(f'Последовательность является квадратом Ло Шу')
    else:
        print(f'Последовательность не является квадратом Ло Шу')


def get_data():
    lo_sho = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(lo_sho)):
        for j in range(len(lo_sho[i])):
            lo_sho[i][j] = int(input(f'Введите число в ячейку {i + 1}:{j + 1}: '))
    return lo_sho


def main():
    u_data = get_data()
    check(u_data)


if __name__ == '__main__':
    main()
