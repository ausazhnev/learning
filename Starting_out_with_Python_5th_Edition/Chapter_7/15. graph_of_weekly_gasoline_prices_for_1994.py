# Задание (RU)
# 15. График еженедельных цен на бензин за 1994 год.
# Файл "dop\15. 1994_weekly_gas_averages.txt"  содержит среднюю цену бензина в течении каждой недели 1994 года.
# (В файле 52 строки) Используя пакет matplotlib, напишите программу Python, которая считывает содержимое файла и
# затем строит либо линейный график либо гистограмму. Не забудьте показать содержательные метки вдоль осей 'x' и 'y',
# а так же метки делений.
#
# Task (EN)
# 15. Graph of weekly gasoline prices for 1994.
# The file "dop\15.1994_weekly_gas_averages.txt" contains the average price of gasoline for each week in 1994.
# (File has 52 lines) Using the matplotlib package, write a Python program that reads the contents of a file and
# then plots either a line plot or a bar chart. Don't forget to show content labels along the 'x' and 'y' axes,
# as well as tick marks.


import matplotlib.pyplot as plt


F_NAME = '15. 1994_weekly_gas_averages.txt'


def get_data():
    f_data = open(f'dop\\{F_NAME}', 'r')
    l_data = []
    for value in f_data:
        l_data.append(float(value))
    f_data.close()
    return l_data


def show_diag(y_coords):
    x_coords = [i for i in range(52)]
    plt.plot(x_coords, y_coords)

    plt.title('Graph of weekly gasoline prices for 1994')
    plt.grid(True)
    plt.xlabel('Недели')
    plt.ylabel('Стоимость')

    plt.yticks([0.99, 1.05, 1.1, 1.15, 1.2],['$0.99', '$1.05', '$1.1', '1.15', '$1.2',])
    plt.xticks(x_coords, x_coords)
    plt.show()


def main():
    l_data = get_data()
    show_diag(l_data)


if __name__ == '__main__':
    main()
