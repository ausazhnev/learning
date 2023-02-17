# Задание №8 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №8 to Chapter 8
# The text of the task is in the file tasks_en.txt

def get_data():
    return input(f'[#] Введите строку для редактирования:\n'
                 f'[#] > > ')


def converter(data):
    flag = True
    new_string = ''
    for ch in data:
        if ch.isalpha():
            if flag == True:
                new_string += ch.upper()
                flag = False
            else:
                new_string += ch
        else:
            new_string += ch
        if ch == '.' or ch == '!' or ch == '?':
            flag = True
    return new_string


# Давнная функция носит декоратиыный характер
def processing():
    print(f'[#] > Выполняется обработка\n'
          f'[#] > . . \n'
          f'[#] > . . .')


def show_result(data):
    processing()
    print(data)


def main():
    user_sring = get_data()
    new_string = converter(user_sring)
    show_result(new_string)


if __name__ == '__main__':
    main()
