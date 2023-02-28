# Задание #1 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходные данные для создания словарей находятся в файлах:
# 'dop/tab_9_1_1.png', 'dop/tab_9_1_3.png', 'dop/tab_9_1_3.png'
#
# Task # 1 to chapter 9
# The text of the task is in the file tasks_en.txt
# The initial data for creating dictionaries is in the files:
# 'dop/tab_9_1_1.png', 'dop/tab_9_1_3.png', 'dop/tab_9_1_3.png'

CLASSROOM = {'CS101': 3003, 'CS102': 4501, 'CS103': 6755, 'CS104': 1244, 'CS105': 1411}
TEACHER = {'CS101': 'Hains', 'CS102': 'Alvardo', 'CS103': 'Rich', 'NT110': 'Berk', 'CM241': 'Li'}
TIME = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}


# Получение данных от пользователя
def get_user_data():
    return input(f'[#] > Введите номер интересующего курса:\n'
                 f'[#] > > '
                 )


# Обработка запроса. Создаём новый словарь в который добавляем данные по ключу введенному
# пользователем если в исходном словаре данных нет, то в новый словарь не чего не добавляется
def data_processing(data):
    answer = {}
    if data in CLASSROOM:
        answer['room'] = CLASSROOM[data]
    if data in TEACHER:
        answer['teacher'] = TEACHER[data]
    if data in TIME:
        answer['time'] = TIME[data]
    return answer


# Вывод данных на экран
def show_result(answer, user_data):
    # метод get возвращает значение по его ключу, если значение не найдено,
    # возвращается значение заданное нами при вызове метода
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
