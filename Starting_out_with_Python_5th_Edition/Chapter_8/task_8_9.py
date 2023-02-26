# Задание №9 к главе 8
# Текст задания находится в файле tasks_ru.txt
#
# Task №9 to Chapter 8
# The text of the task is in the file tasks_en.txt

VOWEL_LIST = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
CONSONANT_LIST = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
                  'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
                  )


def get_data():
    return input(f'[#] > Введите предложение:\n'
                 f'[#] > > '
                 )


def analizer(data):
    vowel, consonant = 0, 0
    for ch in data:
        if ch.lower() in VOWEL_LIST:
            vowel += 1
        elif ch.lower() in CONSONANT_LIST:
            consonant += 1
    return vowel, consonant


def show_result(vowel, consonant):
    print(f'[#] > В вашем предложении:\n'
          f'[#] > {vowel} гласных\n'
          f'[#] > {consonant} согласных'
          )


def main():
    user_string = get_data()
    vowel, consonant = analizer(user_string)
    show_result(vowel, consonant)


if __name__ == '__main__':
    main()
