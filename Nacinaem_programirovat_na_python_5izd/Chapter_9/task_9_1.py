# Задание №1 к главе 9
# Текст задания находится в файле tasks_ru.txt
#
# Task №1 to chapter 9
# The text of the task is in the file tasks_en.txt

CLASSROOM = {'CS101': 3003, 'CS102': 4501, 'CS103': 6755, 'CS104': 1244, 'CS105': 1411}
TEACHER = {'CS101': 'Hains', 'CS102': 'Alvardo', 'CS103': 'Rich', 'NT110': 'Berk', 'CM241': 'Li'}
TIME = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}


def get_user_data():
    return input(f'[#] > Введите номер интересующего курса?\n'
                 f'[#] > > '
                 )


def data_processing(data):
    answer = {}
    if data in CLASSROOM:
        answer['room'] = CLASSROOM[data]
    if data in TEACHER:
        answer['teacher'] = TEACHER[data]
    if data in TIME:
        answer['time'] = TIME[data]
    return answer


def show_result(answer, user_data):
    print(f'[#] > Данные для курса:\t {user_data}\n'
          f'[#] > Номер аудитории:\t {answer.get("room", "Данные не найдены")}\n'
          f'[#] > Преподаватель:\t {answer.get("teacher", "Данные не найдены")}\n'
          f'[#] > Время занятий:\t {answer.get("time", "Данные не найдены")}'
          )


def main():
    user_data = get_user_data()
    answer = data_processing(user_data)
    show_result(answer, user_data)


if __name__ == '__main__':
    main()
