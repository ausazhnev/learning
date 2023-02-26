# Задание (RU)
# Статистика дождевых осадков
# Разработайте программу, которая позволяет пользователю занести в список общее количество дождевых осадков за каждый
# из 12 месяцев. Программа должна вычислить и показать суммарное количество дождевых осадков за год, среднее
# ежемесячное количество дождевых осадков и месяцы с самым высоким и самым низким количеством дождевых осадков
#
# Task (EN)
# Rainfall statistics
# Develop a program that allows the user to list the total amount of rainfall for each of the 12 months.
# The program should calculate and show the total rainfall for the year, the average monthly rainfall
# and the months with the highest and lowest rainfall

def get_rain_level(month_list):
    rain_level = []
    for month in month_list:
        rain_level.append(float(input(f'Введите уровень осадков в {month}: ')))
    return rain_level


def calculate(rain_level, month_list):
    total = 0
    for value in rain_level:
        total += value
    print(f'За год выпало {total} мм. осадков.')
    print(f'Среднее количество осадков в месяц составило {(total / len(rain_level)):.2f} мм')
    max_index = rain_level.index(max(rain_level))
    print(f'Максимальный уровень осадков в году {max(rain_level)} мм выпал в {month_list[max_index]}')
    min_index = rain_level.index(min(rain_level))
    print(f'Минимальный уровень осадков в году {min(rain_level)} мм выпал в {month_list[min_index]}')


def main():
    MONTH_LIST = ('Январе', 'Феврале', 'Марте', 'Апреле', 'Мае', 'Июне',
                  'Июле', 'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре')
    print(f'Введите количество осадков по месяцам:')
    rain_level = get_rain_level(MONTH_LIST)
    # Рассчет статистики
    calculate(rain_level, MONTH_LIST)


if __name__ == '__main__':
    main()
