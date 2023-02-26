# Задание №12 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №12 to Chapter 8
# The text of the task is in the file tasks_en.txt

# сделать через слайс слова

def get_user_data():
    return input(f'[#] > Введите строку:\n'
                 f'[#] > > '
                 )


def converter(data):
    temp_list = data.split()
    new_string = ''
    for word in temp_list:
        temp_word = ''
        for ch in range(1, len(word)):
            temp_word += word[ch]
        temp_word += word[0] + 'ки '
        new_string += temp_word
    return new_string


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
