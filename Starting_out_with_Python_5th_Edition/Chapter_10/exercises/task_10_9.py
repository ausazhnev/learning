# Задание #9 к главе 10
# Текст задания находится в файле tasks_ru.txt
#
# Task #9 to chapter 10
# The text of the task is in the file tasks_en.txt

import m_question_10_9 as question
import m_player_10_9 as player
from random import sample

FILE_NAME = 'question.txt'


# Создаем список вопросов из файла с заготовкой
def create_list():
    question_list = []
    with open(f'../dop/{FILE_NAME}', 'r') as file:
        for line in file:
            disc = line.strip().strip()
            answer1 = file.readline().strip()
            answer2 = file.readline().strip()
            answer3 = file.readline().strip()
            answer4 = file.readline().strip()
            correct = file.readline().strip()
            quest = question.Question(disc, answer1, answer2, answer3, answer4, correct)
            question_list.append(quest)
    return question_list


# Формируем список вопросов для игры
def rnd_list(question_list):
    if len(question_list) <= 10:
        # Если количество вопросов не четное
        # то делаем отсекаем лишний вопрос
        if (len(question_list) % 2) == 0:
            count = len(question_list)
        else:
            count = len(question_list) - (len(question_list) % 2)
    else:
        count = 10
    # Перемешиваем элементы списка в случайном порядке
    return sample(question_list, count)


# Выводим на экран вопрос и данные игрока которому он задается
def ask(player, quest):
    print(f'Вопрос игроку: {player.get_name()}')
    print(f'[X] > {quest.get_discription()}')
    print(f'[1] > {quest.get_answer1()}')
    print(f'[2] > {quest.get_answer2()}')
    print(f'[3] > {quest.get_answer3()}')
    print(f'[4] > {quest.get_answer4()}')
    print('-' * 32)
    p_answer = input(f'[X] > Выберете вариант ответа: ')
    print('-' * 72)
    # Если ответ правильный вызываем метод увеличивающий счет игрока
    if p_answer == quest.get_correct():
        player.add_point()


# Проверяем показатель очков и выводим данные о победителе на экран
def show_win(player_1, player_2):
    if player_1.get_score() > player_2.get_score():
        print(f'Победил {player_1.get_name()}, набрав {player_1.get_score()} очка(ков).')
    elif player_2.get_score() > player_1.get_score():
        print(f'Победил {player_2.get_name()}, набрав {player_2.get_score()} очка(ков).')
    else:
        print(f'Ничья! вы набрали одинаковое количество очков.')


# Создаем объекты класса игрок
def create_player(num):
    name = input(f'Введите имя игрока №{num}: ')
    obj = player.Player(name)
    return obj


def main():
    # Создать объекты игроков
    player_1 = create_player(1)
    player_2 = create_player(2)
    # Создать список объектов с вопросами для игры
    question_list = create_list()
    # Изменить порядок вопросов на произвольный
    question_list = rnd_list(question_list)
    separete = len(question_list) / 2
    count = 1
    for item in question_list:
        # Пока вопросы не кончились, задаем их игрокам
        if count <= separete:
            ask(player_1, item)
        else:
            ask(player_2, item)
        count += 1
    show_win(player_1, player_2)


if __name__ == '__main__':
    main()
