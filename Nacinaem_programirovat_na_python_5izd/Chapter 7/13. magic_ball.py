# Задание (RU)
# 3. Магический шар.
# Напишите программу, моделирующую магический шар, т. е. игрушку, которая предсказывает и дает случайный ответ на общий
# вопрос,  требующий ответа "да" или "нет". Файл 13. ball_responses.txt содержит 12 ответов, в частности: "Не думаю",
# "Да, конечно!", "Не уверен" и т.д. Программа должна прочитать ответы из файла в список, предложить пользователю
# задать вопрос и затем показать один из ответов, отобранных из списка случайным образом. Программа должна продолжать
# работу до тех пор, пока пользователь не будет готов из нее выйти.
#  - 13. ball_responses_ru.txt - содержит ответы на Русском языке.
#
# Task (EN)
# 13. Magic ball.
# Write a program that simulates a magic ball, i.e. a toy that predicts and gives a random answer to a general yes or
# no question. File 13. ball_responses.txt contains 12 responses, in particular: "I don't think", "Yes, of course!",
# "I'm not sure" and so on. The program must read the answers from the file into a list, prompt the user to ask a
# question, and then display one of the answers selected at random from the list. The program should continue running
# until the user is ready to exit it.
#   - 13. ball_responses_ru.txt - contains answers in Russian.

import random


def game_language():
    print(f'Выберете язык ответов магического шара.')
    print(f'1 - Русский')
    print(f'2 - English')
    language = int(input(f'Введите 1 или 2: '))
    if language == 1: return '13. ball_responses_ru.txt'
    else: return '13. ball_responses.txt'


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
