# Задание №4 к главе 8
# Текст задания находится в вайле tasks_ru.txt
#
# Task №4 to Chapter 8
# The text of the task is in the file tasks_en.txt


MORZE_RU = (('А', '.-'), ('Б', '-...'), ('В', '.--'), ('Г', '--.'), ('Д', '-..'), ('Е', '.'),
            ('Ё', '.'), ('Ж', '...-'), ('З', '--..'), ('И', '..'), ('Й', '.---'), ('К', '-.-'),
            ('Л', '.-..'), ('М', '--'), ('Н', '-.'), ('О', '---'), ('П', '.--.'), ('Р', '.-.'),
            ('С', '...'), ('Т', '-'), ('У', '..-'), ('Ф', '..-.'), ('Х', '....'), ('Ц', '-.-.'),
            ('Ч', '---.'), ('Ш', '----'), ('Щ', '--.-'), ('Ъ', '.--.-.'), ('Ы', '-.--'),
            ('Ь', '-..-'), ('Э', '..-..'), ('Ю', '..--'), ('Я', '.-.-')
            )
MORZE_EN = (('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
            ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
            ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
            ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
            ('Y', '-.-'), ('Z', '--..')
            )
MORZE_GEN = ((' ', ' '), (',', '--..--'), ('.', '.-.-.-'), ('?', '..--..'), ('0', '-----'),
             ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'),
             ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.')
             )


def language_selection():
    user_lang = input(f'[*] Выберете язык кодирования: [1] - Русский [2] - English\n'
                      f'[*] > > ')
    if not check(user_lang):
        user_lang = language_selection()
    if int(user_lang) == 1:
        return MORZE_RU
    else:
        return MORZE_EN


def check(data):
    if data == '1' or data == '2':
        return True
    else:
        print(f'[*] > Введите  1 или 2 Повторите ввод.<')


def show_result(data):
    print(f'Ваша строка кодированая азбукой морзе:..\n'
          f'[#] > > {data}')


def convertation(data, lang):
    total_str = ''
    for ch in data:
        for i in range(len(lang)):
            if ch.upper() == lang[i][0]:
                total_str += lang[i][1]
                continue
        for i in range(len(MORZE_GEN)):
            if ch.upper() == MORZE_GEN[i][0]:
                total_str += MORZE_GEN[i][1]
    return total_str


def get_data():
    return input(f'[#] Введите строку для конвертации:\n'
                 f'[#] > > ')


def main():
    dictionary = language_selection()
    user_data = get_data()
    convert_srt = convertation(user_data, dictionary)
    show_result(convert_srt)


if __name__ == '__main__':
    main()
