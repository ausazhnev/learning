# Задание №14 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №14 to Chapter 8
# The text of the task is in the file tasks_en.txt

FILE_NAME = 'GasPrices.txt'

def get_list_1_2_3():
    file = open(f'dop\\{FILE_NAME}', 'r')               # получаем данные из файла и создаем
    gas_list = []                                       # новый список.
    for line in file:                                   # на выходе получаем список формата
        line = line.strip()                             # [xx, xx, xxxx, x.xx] содержащий числа
        tmp_list = line.split(':')                      # int и float а не строковые значения str
        tmp = [int(i) for i in tmp_list[0].split('-')]
        tmp.append(float(tmp_list[1]))
        gas_list.append(tmp)
    file.close()
    return gas_list


# def again():
#     print(f'[#] ----------------------------------------- [#]\n'
#           f'[#] > Получить еще данные ?\n'
#           f'[#] > [1] - Да\n'
#           f'[#] > [Любое другое] - Нет'
#           )
#     if input(f'[#] > > ') == '1': menu()
#     else: print(f'[#] > Закрываем протокол комуникации. . .')



def year_key(data):
    return data[2]


def average_for_month():
    data_list = get_list_1_2_3()            # получаем данные из файла в общий список даты в
    data_list.sort(key=year_key)            # списке представлены числами (int)
                                            # сортируем список по году
    print(data_list)
    # year_list = []



def average_for_year():
    data_list = get_list_1_2_3()
    data_list.sort(key=year_key)            # сортируем полученый список по индексу 2 (год)
    cout = 0
    total = 0
    year = data_list[0][2]
    for line in data_list:
        if line[2] == year:
            total += line[3]
            cout += 1
        else:
            print(f'[#] > Средняя цена за {year} = {(total / cout):.3f}')
            year = line[2]
            cout = 0
            total = 0                                               # цикл не выводит данные по
            total += line[3]                                        # последнему году из файла
            cout += 1                                               # эти данные выводим после
    print(f'[#] > Средняя цена за {year} = {(total / cout):.3f}')   # завершения цикла


def get_list_4_5():
    file = open(f'dop\\{FILE_NAME}', 'r')               # получаем данные из файла и создаем
    gas_list = []                                       # новый список.
    for line in file:                                   # на выходе получаем список формата
        line = line.strip()
        line = line.split(':')
        tmp = []
        tmp.append(line[0])
        tmp.append(float(line[1]))
        gas_list.append(tmp)
        tmp = []
    file.close()
    return gas_list


def price_key(data):
    return data[1]


def price_list_up():
    data_list = get_list_4_5()
    data_list.sort(key=price_key)               # сортировка производится по ключу выбранного
    file = open(f'dop\\price_up.txt', 'w')      # в функции price_key(data)
    for line in data_list:
        file.write(f'{line[0]}:{line[1]}\n')    # строки в файл записываются в формате
    print(f'[#] > Обработка. . .\n'             # XX-XX-XXXX:X.XXX как в исходном файле задания
          f'[#] > Файл сформирован и сохранен - {file.name}')
    file.close()


def price_list_dn():                                # читай комментарии к price_list_up():
    data_list = get_list_4_5()
    data_list.sort(key=price_key, reverse=True)     # reverse=True - сортитирует в обратном
    file = open(f'dop\\price_dn.txt', 'w')          # порядке
    for line in data_list:
        file.write(f'{line[0]}:{line[1]}\n')
    print(f'[#] > Обработка. . .\n'
          f'[#] > Файл сформирован и сохранен - {file.name}')
    file.close()




    # new_str = ''
    # for line in range(len(data_list)-1, 0, -1):
    #     for i in range(len(data_list[line])):
    #         new_str += str(data_list[line][i])
    #         if i == 0 or i == 1: new_str += '-'
    #         if i == 2: new_str += ':'
    #     file.write(f'{new_str}\n')
    #     new_str = ''
    # print(f'[#] > Обработка. . .\n'
    #       f'[#] > Файл сформирован и сохранен - {file.name}')
    # file.close()


def menu():
    print(f'[#] ----------------------------------------- [#]\n'
          f'[#] > Какие данные вы хотите получить ?\n'
          f'[#] > [1] - средняя цена за год\n'
          f'[#] > [2] - средняя цена за месяц\n'
          f'[#] > [3] - наибольшая и наименьшая цена в году\n'
          f'[#] > [4] - список цен по возрастанию (будет сохранен в файл)\n'
          f'[#] > [5] - список цен по убыыванию (будет сохранен в файл)\n'
          f'[#] > [0] - Выход'
          )
    user_change = input(f'[#] > > ')
    if check_cange(user_change) == False:
        menu()
    return user_change


def check_cange(data):
    if data.isdigit():
        if int(data) >= 0 and int(data) < 6:
            print(f'[#] > Выбор принят. . . ')
            return True
    print(f'[#] > Ошибка выбора! повторите свой выбор.')
    return False


def main():
    user_change = menu()
    if user_change == '1': average_for_year()
    elif user_change == '2': average_for_month()
    # elif user_change == 3:
    elif user_change == '4': price_list_up()
    elif user_change == '5': price_list_dn()
    else: print(f'Закрываем протокол комуникации. . .')
    # if user_change != '0': again()



if __name__ == '__main__':
    main()
