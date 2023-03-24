# Задание #11 к главе 7
# Текст задания находится в файле tasks_ru.txt
# Ло Шу последовательность
# 4   9   2
# 3   5   7
# 8   1   6
#
# Task #11 to chapter 7
# The text of the task is in the file tasks_en.txt
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
