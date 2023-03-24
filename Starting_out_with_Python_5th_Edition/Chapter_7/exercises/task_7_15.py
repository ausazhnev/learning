# Задание #15 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #15 to chapter 7
# The text of the task is in the file tasks_en.txt


import matplotlib.pyplot as plt


F_NAME = '15. 1994_weekly_gas_averages.txt'


def get_data():
    f_data = open(f'../dop/{F_NAME}', 'r')
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
