# Задание №11 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №11 to Chapter 8
# The text of the task is in the file tasks_en.txt

def get_user_data():
    return input(f'[#] > Введите строку:\n'
                 f'[#] > > '
                 )


def converter(user_str):
    flag = True                                 # flag = True используется для определения первой
    new_str = ''                                # буквы в заданной строке что бы не ставить перед
    for ch in user_str:                         # ней пробел и не менять ее регистр
        if ch.isupper() and flag != True:       # пример: ОстановисьИРочуствуйЗапахРоз
            new_str += ' ' + ch.lower()         # вывод: Остановись и рочуствуй запах роз
        else:
            new_str += ch
            flag = False
    return new_str


def show_result(new_srt):
    print(f'[#] > Отформативанная строка. . .\n'
          f'[#] > {new_srt}'
          )


def main():
    user_str = get_user_data()
    new_str = converter(user_str)
    show_result(new_str)


if __name__ == '__main__':
    main()
