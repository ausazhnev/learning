# Задание №5 к главе 8
# Текст задания находится в вайле tasks_ru.txt
#
# Задача может быть решена проще с помощью словарей.
# Но данный материал на момент написания кода в книге не проходился.
#
# Task №5 to Chapter 8
# The text of the task is in the file tasks_en.txt
#
# The problem can be solved more easily with the help of dictionaries.
# But this material was not covered in the book at the time of writing the code.


CONVERT_LIST = (('A', 2), ('B', 2), ('C', 2),
                ('D', 3), ('E', 3), ('F', 3),
                ('G', 4), ('H', 4), ('I', 4),
                ('J', 5), ('K', 5), ('L', 5),
                ('M', 6), ('N', 6), ('O', 6),
                ('P', 7), ('Q', 7), ('R', 7), ('S', 7),
                ('T', 8), ('U', 8), ('V', 8),
                ('W', 9), ('X', 9), ('Y', 9), ('Z', 9),
                )


def convertation(data):
    new_phone = ''
    for ch in data:
        found = False
        for j in range(len(CONVERT_LIST)):
            if ch.upper() == CONVERT_LIST[j][0]:
                new_phone += str(CONVERT_LIST[j][1])
                found = True
                break
        if not found:
            new_phone += ch
    return new_phone


def get_data():
    user_data = input(f'[#] Введите номер телефона в формате XXX-XXX-XXXX\n'
                      f'> > ')
    return user_data


def show_result(data):
    print(f'Перекодированый номер телефона:\n'
          f'> > {data}')


def main():
    user_phone = get_data()
    new_phone = convertation(user_phone)
    show_result(new_phone)


if __name__ == '__main__':
    main()
