# Задание №10 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №10 to Chapter 8
# The text of the task is in the file tasks_en.txt


def get_user_data():
    return input(f'[#] > Введите строку:\n'
                 f'[#] > > '
                 )


def analizer(user_str):
    temp_ch = []
    cout, max_value = 0, 0
    max_ch = user_str[0]
    for ch in user_str:
        if ch not in temp_ch:
            temp_ch.append(ch)
    for i in temp_ch:
        for j in user_str:
            if i.upper() == j.upper():
                cout += 1
        if max_value < cout:
            max_value = cout
            max_ch = j
        cout = 0
    return max_ch, max_value


def show_result(max_ch, max_value):
    print(f'[#] > В вашем строке чаще всего встречается символ. . .\n'
          f'[#] > {max_ch} > {max_value}'
          )


def main():
    user_str = get_user_data()
    max_ch, max_value = analizer(user_str)
    show_result(max_ch, max_value)


if __name__ == '__main__':
    main()
