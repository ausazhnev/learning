# Задание (RU)
# Данные о населении.
# В файле USPopulation.txt содержатся данные о среднегодовой численности населения США в тысячах с 1950 по 1990 год.
# Первая строка в файле содержит численность населения в 1950 году, вторая строка - численность в  1951 году и т.д.
# Напишите программу, которая считывает содержимое файла в список. Программа должна показать приведенные ниже данные:
#  - среднегодовое изменение численности населения в течение указанного периода времени.
#  - год с наибольшим увеличением численности населения в течение указанного периода.
#  - год с наименьшим увеличением численности населения в течении указанного периода времени.
#
# Task (EN)
# Population data.
# In the file USPopulation.txt contains data on the average annual population of the United States in thousands from
# 1950 to 1990. The first line in the file contains the population in 1950, the second line contains the population
# in 1951, etc.
# Write a program that reads the contents of a file into a list. The program should show the following data:
# - the average annual change in the population over a specified period of time.
# - the year with the largest increase in the population during the specified period.
# - the year with the smallest increase in the population during the specified period of time.
# from typing import List, Any


def get_data():
    f_data = open('dop\\9. USPopulation.txt', 'r')
    population_list = []
    for value in f_data:
        value = int(value.strip('\n'))
        population_list.append(value)
    f_data.close()
    return population_list


def show_calc(population_list):
    change_population = []
    for i in range(len(population_list)):
        if i != 0: change_population.append(population_list[i] - population_list[i-1])
    print(f'Среднегодовое увеличение численности: {(sum(change_population) / len(change_population)):.2f}')
    max_index = change_population.index(max(change_population))
    print(f'Больше всего людей появилось в {1950 + max_index} году, увеличение на {max(change_population)}')
    min_index = change_population.index(min(change_population))
    print(f'Меньше всего людей появилось в {1950 + min_index} году, увеличение на {min(change_population)}')


def main():
    population_list = get_data()
    show_calc(population_list)


if __name__ == '__main__':
    main()
