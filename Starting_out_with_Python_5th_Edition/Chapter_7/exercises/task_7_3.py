# Задание #3 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #3 to chapter 7
# The text of the task is in the file tasks_en.txt

MONTH_LIST = ('Январе', 'Феврале', 'Марте', 'Апреле', 'Мае', 'Июне',
              'Июле', 'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре'
              )


def get_rain_level(month_list):
    rain_level_list = []
    for month in month_list:
        rain_level_list.append(float(input(f'Введите уровень осадков в {month}: ')))
    return rain_level_list


def show_result(rain_level_list, month_list):
    print('=' * 50)
    print(f'Результат анализа данных:')
    print(f'За год выпало {sum(rain_level_list)} мм. осадков.')
    print(f'Среднее количество осадков в месяц составило '
          f'{(sum(rain_level_list) / len(rain_level_list)):.2f} мм'
          )
    print(f'Максимальный уровень осадков в году {max(rain_level_list)} мм выпал в '
          f'{month_list[rain_level_list.index(max(rain_level_list))]}'
          )
    print(f'Минимальный уровень осадков в году {min(rain_level_list)} мм выпал в '
          f'{month_list[rain_level_list.index(min(rain_level_list))]}'
          )


def main():
    print(f'Введите количество осадков по месяцам:')
    rain_level_list = get_rain_level(MONTH_LIST)
    show_result(rain_level_list, MONTH_LIST)


if __name__ == '__main__':
    main()
