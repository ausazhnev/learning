# Задание (RU)
# 14. Круговая диаграмма расходов.
# Создайте текстовый файл, который содержит расходы за прошлый месяц по приведенным ниже статьям:
# арендная плата, бензин, продукты питания, одежда, платежи по автомобилю, прочие.
# Напишите программу на Python, которая считывает данные из файла и использует пакет matolotlib для построения
# круговой диаграммы, показывающей, как вы тратите свои деньги.
# Данные находятся "dop\14. spending_per_month.txt"
#
# Task (EN)
# 14. Pie chart of expenses.
# Create a text file that contains last month's expenses for the following items:
# rent, gasoline, food, clothing, car payments, other.
# Write a Python program that reads data from a file and uses the matolotlib package to build a pie chart showing
# how you spend your money.
# The data is "dop\14.spending_per_month.txt"

import matplotlib.pyplot as ptl

F_NAME = '14. spending_per_month.txt'

def get_data():
    l_name = []
    l_mony = []
    f_data = open(f'dop\\{F_NAME}', 'r')
    line = f_data.readline()
    while line:
        line = line.strip('\n')
        l_name.append(line)
        line = f_data.readline()
        line = line.strip('\n')
        l_mony.append(line)
        line = f_data.readline()
    f_data.close()
    return l_name, l_mony

def show_diag(l_name, l_mony):
    ptl.pie(l_mony, labels=l_name)
    ptl.show()

def main():
    l_name, l_mony = get_data()
    show_diag(l_name, l_mony)

if __name__ == '__main__':
    main()
