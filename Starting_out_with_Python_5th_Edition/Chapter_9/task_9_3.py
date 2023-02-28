# Задание #3 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходный файл для кодирования 'dop/orig_file.txt',
# закодированный файл для декодирования 'dop/code_file.txt' (создается если выбрать кодирование)
#
# Task #3 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source file to encode 'dop/orig_file.txt',
# encoded file to decode 'dop/code_file.txt' (created if encoding is selected)

# Словарь, который будет использоваться для кодирования
CODES = {"A": "%", "a": "9", "B": "@", "b": "#", "C": ":", "c": ";", "D": "'", "E": "(",
         "e": ")", "F": "{", "f": "}", "G": "<", "g": ">", "H": "=", "h": "-", "I": "+",
         "i": "*", "J": "/", "j": "^", "K": "%", "k": "$", "L": "|", "l": "!", "M": "?",
         "m": "_", "N": "8", "n": "7", "O": "6", "o": "5", "P": "4", "p": "3", "Q": "2",
         "q": "1", "R": "0", "r": ".", "S": ",", "s": "~", "T": "¡", "t": "!", "U": "[",
         "u": "]", "V": "¿", "v": "®", "W": "¤", "w": "β", "X": "€", "x": "Δ", "Y": "¥",
         "y": "£", "Z": "™", "z": "π"
         }

# Чтение оригинального файла и запись его кодированной версии в новый файл
# Перебираем символы в строках и находим такой ключ в словаре CODES, если ключ найден то
# записываем значение этого ключа в файл, если ключ не найден то записываем в файл исходное
# значение
def coding():
    with open('dop/orig_file.txt', 'r', encoding='utf8') as f_orig:
        data_in_file = f_orig.readlines()
        print(data_in_file)
        with open('dop/code_file.txt', 'w', encoding='utf8') as f_code:
            for line in data_in_file:
                for ch in line:
                    if ch in CODES:
                        print(CODES[ch])
                        f_code.write(CODES[ch])
                    else:
                        f_code.write(ch)


# Функция принимает список содержащий пары ключ значение из словаря CODES и текущий символ строки
# в цикле находит этот символ среди item[1] и присваивает возвращаемой переменной значение
# из item[0] возвращая его для записи в декодированную строку. Если значение не находится
# возвращается исходный символ
def kay_val(ch, l_codes):
    new_ch = ch
    for item in l_codes:
        if ch == item[1]:
            new_ch = item[0]
            # Если символ найден, прекращаем цикл, что бы не было лишних итераций
            break
    return new_ch


# Декодирование полученной из файла строки
# l_codes - список содержащий пары ключ - значения из словаря CODES
# передаем в kay_val(ch, l_codes) текущий символ строки и список l_codes
def decoding():
    with open('dop/code_file.txt', 'r', encoding='utf8') as f_code:
        decode_str = ''
        l_codes = CODES.items()
        for line in f_code:
            for ch in line:
                decode_str += kay_val(ch, l_codes)
        line = f_code.readline()
        print(decode_str)


# Отрисовка меняю и проверка корректности введенного пользователем значения
def menu():
    user_change = input(f'[#] ------------------------------- [#]\n'
                        f'[#] > Какие данные вы хотите получить ?\n'
                        f'[#] > [1] - Кодировать файл\n'
                        f'[#] > [2] - Декодировать файл\n'
                        f'[#] > [0] - Выход\n'
                        f'[#] > > '
                        )
    if user_change.isdigit() and (int(user_change) >= 0 or int(user_change) <= 2):
        return int(user_change)
    else:
        menu()
        return user_change


def main():
    user_change = menu()
    if user_change == 1:
        coding()
    elif user_change == 2:
        decoding()
    else:
        print(f'[#] > Закрываем протокол комуникации. . .')


if __name__ == '__main__':
    main()
