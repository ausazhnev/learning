# Задание #14 к главе 7
# Текст задания находится в файле tasks_ru.txt
# Данные находятся "dop\14. spending_per_month.txt"
#
# Task #14 to chapter 7
# The text of the task is in the file tasks_en.txt
# The data is "dop\14.spending_per_month.txt"

import matplotlib.pyplot as ptl

F_NAME = '14. spending_per_month.txt'


def get_data():
    l_name = []
    l_money = []
    with open(f'../dop/{F_NAME}', 'r') as f_data:
        line = f_data.readline()
        while line:
            line = line.strip('\n')
            l_name.append(line)
            line = f_data.readline()
            line = line.strip('\n')
            l_money.append(line)
            line = f_data.readline()
    return l_name, l_money


def show_diag(l_name, l_money):
    ptl.pie(l_money, labels=l_name)
    ptl.show()


def main():
    l_name, l_money = get_data()
    show_diag(l_name, l_money)


if __name__ == '__main__':
    main()
