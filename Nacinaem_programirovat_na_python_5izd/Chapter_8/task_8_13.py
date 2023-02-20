# Задание №13 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №13 to Chapter 8
# The text of the task is in the file tasks_en.txt


# доделать! 10 наиболее 'созревших' чисел (чисел, которые не использовались долгое время), упорядоченных
# от наиболее 'созревших' до наименее 'созревших'

# Доделать работу меню. не срабатывает если ввести 2 раза неверный пункт

FILE_NAME = 'pbnumbers.txt'

# Получаем данне из текстового файда
def get_data():
    file = open(f'dop\\{FILE_NAME}', 'r')           # читаем данные из файла и сразу
    num_list = []                                   # собираем их в два списка
    pb_list = []                                    # num_list - список 5 выповших чисел
    for line in file:                               # список выпавших чисел PawerBall
        tokens = line.split()
        for i in range(len(tokens)):
            if i != 5:
                num_list.append(int(tokens[i]))
            else:
                pb_list.append(int(tokens[i]))
    return num_list, pb_list


def costom_key(data):                   # ключ сортировки выбирается
    return data[1]                      # элемент списка с индексом 1

# создаем список [[Значение],[Сколько раз появлялось]]
def data_processing(num_list):
    num_list = sorted(num_list)
    num_2d = [[0, 0]]
    for i in num_list:
        if int(num_2d[-1][0]) != i:
            num_2d.append([i, 1])
        else:
            num_2d[i][1] += 1
    num_2d.pop(0)
    num_2d.sort(key=costom_key)
    return num_2d


# 10 самых частых чисел
def privete_numbers(num_2d):
    num_list = ''
    for i in range(len(num_2d) - 1, len(num_2d) - 11, -1):
        num_list += ' ' + str(num_2d[i][0])
    show_result('10 наиболее распространенных чисел, упорядоченных по частоте', num_list)


# 10 самых не частых чисел
def rare_numbers(num_2d):
    num_list = ''
    for i in range(10):
        num_list += str(num_2d[i][0]) + ' '
    show_result('10 наименее распространенных чисел, упорядоченных по частоте', num_list)


# Вывод на экран частоты появления числе от 1 до 69
def show_frequncy(data, name_list):
    print(f'[#] > Частота появления {name_list}\n'
          f'[#] > Обработка. . .'
          )
    for i in range(len(data)):                              # для вывода используем цикл
        print(f'[#] > ', end='')                            # обходим полученный ранее
        for j in range(len(data[i])):                       # отсортированный список
            print(f'{data[i][j]} \t', end='')               # от меньшего к большему
        print()


# Выводим на эран частоту появления чисел от 1 до 25 (PowerBall
def number_frequncy(num_list):
    num_list = sorted(num_list)
    num_2d = [[0, 0]]                                       # создаем двумерный список для
    for i in num_list:                                      # хранения данных первый элемент число
        if int(num_2d[-1][0]) != i:                         # второй элемент число повторений
            num_2d.append([i, 1])
        else:                                               # если число в новом списке не встречалось
            num_2d[i][1] += 1                               # создаем новый элемент двумерного списка
    num_2d.pop(0)                                           # удаляем элемент списка с индексом 0 [[0],[0]]
    num_2d.sort(key=costom_key)                             # ключ сортировки оределяется в функии
    show_frequncy(num_2d, 'чисел от 1 до 25')               # отправляем на вывод переработаный
                                                            # список и сообщние для отображения


def show_result(massge, value):
    print(f'[#] > Обработка. . .\n'
          f'[#] > {massge}\n'
          f'[#] > {value}'
          )


def menu():
    print(f'[#] -------------------------------------------------------------------------- [#]\n'
          f'[#] > Какие данные вы хотите получить ?\n'
          f'[#] > [1] - 10 наиболее распространенных чисел, упорядоченных по частоте\n'
          f'[#] > [2] - 10 наименее распространенных чисел, упорядоченных по частоте\n'
          f'[#] > [3] - 10 наиболее \'созревших\' чисел (чисел, которые не использовались\n'
          f'[#] > \t\tдолгое время), упорядоченных от наиболее "созревших" до наименее "созревших"\n'
          f'[#] > [4] - частоту каждого числа от 1 до 69\n'
          f'[#] > [5] - частоту каждого числа от 1 до 26\n'
          f'[#] > [0] - Выход'
          )
    user_change = input(f'[#] > > ')
    if check_cange(user_change) is False:
        menu()
    return user_change


def check_cange(data):
    if data.isdigit():
        if int(data) >= 0 and int(data) <= 5:
            print(f'[#] > Выбор принят. . . ')
            return True
    print(f'[#] > Ошибка выбора! повторите свой выбор.')
    return False


def main():
    user_change = ''
    num_list, pb_list = get_data()
    num_2d = data_processing(num_list)
    while user_change != '0':
        user_change = menu()
        if user_change == '1': privete_numbers(num_2d)
        elif user_change == '2': rare_numbers(num_2d)
        elif user_change == '3': pass
        elif user_change == '4': show_frequncy(num_2d, 'чисел от 1 до 69')
        elif user_change == '5': number_frequncy(pb_list)
        elif user_change == '0':
            print(f'[#] > Закрываем протокол комуникации. . .')
            break
        # засунуть запрос на повторный вызов меню


if __name__ == '__main__':
    main()
