# Задание #13 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #13 to chapter 7
# The text of the task is in the file tasks_en.txt

import random


def game_language():
    print(f'Выберете язык ответов магического шара.')
    print(f'1 - Русский')
    print(f'2 - English')
    language = int(input(f'Введите 1 или 2: '))
    if language == 1:
        return '13. ball_responses_ru.txt'
    else:
        return '13. ball_responses.txt'


def get_answer_list(f_name):
    f_answer = open(f'dop\\{f_name}', 'r')
    list_answer = []
    for value in f_answer:
        value = value.strip('\n')
        list_answer.append(value)
    return list_answer


def get_answer(answer_list):
    rnd = random.randint(0, 12)
    print(f'{answer_list[rnd]}')


def main():
    language_choice = game_language()
    list_answer = get_answer_list(language_choice)
    user_question = input(f'Введите свой вопрос или "0" что бы выйти\n'
                          f': - ')
    while user_question != '0':
        get_answer(list_answer)
        user_question = input(f'Введите свой вопрос или "0" что бы выйти\n'
                              f': - ')


if __name__ == '__main__':
    main()
