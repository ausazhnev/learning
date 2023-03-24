# Задание #9 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #9 to chapter 7
# The text of the task is in the file tasks_en.txt


def get_data():
    with open('../dop/9. USPopulation.txt', 'r') as f_data:
        population_list = []
        for value in f_data:
            value = int(value.strip('\n'))
            population_list.append(value)
    return population_list


def show_calc(population_list):
    change_population = []
    for i in range(len(population_list)):
        if i != 0:
            change_population.append(population_list[i] - population_list[i-1])
    print(f'Среднегодовое увеличение численности: '
          f'{(sum(change_population) / len(change_population)):.2f}'
          )
    print(f'Больше всего людей появилось в '
          f'{1950 + change_population.index(max(change_population))} году, '
          f'увеличение на {max(change_population)}'
          )
    print(f'Меньше всего людей появилось в '
          f'{1950 + change_population.index(min(change_population))} году, '
          f'увеличение на {min(change_population)}'
          )


def main():
    population_list = get_data()
    show_calc(population_list)


if __name__ == '__main__':
    main()
