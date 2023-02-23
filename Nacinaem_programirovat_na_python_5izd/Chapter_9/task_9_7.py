# Задание #7 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходный файл для анализа 'dop\WorldSeriesWinners.txt'
#
# Task #7 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source file for analysis 'dop\WorldSeriesWinners.txt'

F_NAME = 'WorldSeriesWinners.txt'


def create_dict():
    with open(f'dop\\{F_NAME}', 'r', encoding='utf8') as file:
        # собираем словарь год - название команды
        # если World Series Not Played в словарь не добавляем
        data = file.readlines()
        dict_year = {}
        dict_win = {}
        year = 1903
        for item in data:
            item = item.strip()
            if not item[0:23] == 'World Series Not Played':
                dict_year[year] = item
                year += 1
                # собираем второй словарь команда - число побед
                if item not in dict_win:
                    dict_win[item] = 1
                else:
                    dict_win[item] = dict_win.get(item) + 1
            else:
                year += 1
        return dict_year, dict_win


# ввод года который интересует пользователя
# сразу проводится проверка на соответствие диапазону
def get_user_data():
    u_data = input(f'[#] -------------------------- [#]\n'
                   f'[#] > Введите год с 1903 по 2009:\n'
                   f'[#] > > '
                   )
    if u_data.isdigit() and (1903 <= int(u_data) <= 2009):
        return int(u_data)
    else:
        u_data = get_user_data()
        return u_data


# выводим на экран пользователю данные о какая команда победила в заданном году
# и сколько раз побеждала эта команда в Мировой серии
# если указан год в котором Мировая серия не проводилась, сообщаем об этом пользователю
def show_result(year, dict_year, dict_win):
    winner = dict_year.get(year, 'Мировая серия в этом году не проводилась')
    if winner != 'Мировая серия в этом году не проводилась':
        print(f'[#] > В {year} году, победила команда "{winner}"\n'
              f'[#] > Всего команда "{winner}" побеждала {dict_win.get(winner)} раз(а)')
        print()
    else:
        print(f'[#] > {winner}')


def main():
    dict_year, dict_win = create_dict()
    user_data = get_user_data()
    show_result(user_data, dict_year, dict_win)


if __name__ == '__main__':
    main()
