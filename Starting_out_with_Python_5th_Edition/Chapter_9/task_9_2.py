# Задание #1 к главе 9
# Текст задания находится в файле tasks_ru.txt
#
# Task #1 to chapter 9
# The text of the task is in the file tasks_en.txt

import random

# Словарь содержащий пары ключ : значение для вопросов викторины
question = {'Alabama': 'montgomery', 'Alaska': 'juneau', 'Arizona': 'phoenix',
            'Arkansas': 'little rock', 'California': 'sacramento', 'Colorado': 'denver',
            'Connecticut': 'hartford', 'Delaware': 'dover', 'Florida': 'tallahassee',
            'Georgia': 'atlanta', 'Hawaii': 'honolulu', 'Idaho': 'boise',
            'Illinios': 'springfield', 'Indiana': 'indianapolis', 'Iowa': 'des monies',
            'Kansas': 'topeka', 'Kentucky': 'frankfort', 'Louisiana': 'baton rouge',
            'Maine': 'augusta', 'Maryland': 'annapolis', 'Massachusetts': 'boston',
            'Michigan': 'lansing', 'Minnesota': 'st. paul', 'Mississippi': 'jackson',
            'Missouri': 'jefferson city', 'Montana': 'helena', 'Nebraska': 'lincoln',
            'Neveda': 'carson city', 'New Hampshire': 'concord', 'New Jersey': 'trenton',
            'New Mexico': 'santa fe', 'New York': 'albany', 'North Carolina': 'raleigh',
            'North Dakota': 'bismarck', 'Ohio': 'columbus', 'Oklahoma': 'oklahoma city',
            'Oregon': 'salem', 'Pennsylvania': 'harrisburg', 'Rhoda Island': 'providence',
            'South Carolina': 'columbia', 'South Dakoda': 'pierre', 'Tennessee': 'nashville',
            'Texas': 'austin', 'Utah': 'salt lake city', 'Vermont': 'montpelier',
            'Virginia': 'richmond', 'Washington': 'olympia', 'West Virginia': 'charleston',
            'Wisconsin': 'madison', 'Wyoming': 'cheyenne'
            }


def main():
    good_answer = 0
    bad_answer = 0
    again = 'д'
    # Скрипт работает в цикле, пока пользователь выбирает д/Д на вопрос о продолжении викторины
    while again == 'д':
        # Если словарь пуст, прекращаем викторину и переходим к результатам
        if len(question) == 0:
            print(f'[#] > Вопросы закончились.')
            break
        qest = random.choice(list(question))
        answer = input(f'[#] > Назовите столицу штата - {qest}\n'
                       f'[#] > > ').lower()
        if answer == question[qest]:
            good_answer += 1
        else:
            bad_answer += 1
        # Удаляем пару ключ значение из словаря, что бы вопросы не повторялись
        question.pop(qest)
        again = input(f'[#] > Хотите ответить на еще один вопрос ? (д/н)\n'
                      f'[#] > > '
                      ).lower()
    # Поле окончания викторины, выводим результаты пользователя на экран
    print(f'[#] > Ваш результат:\t\n'
          f'[#] > Правильных ответов:\t{good_answer}\n'
          f'[#] > Не правильных ответов:\t{bad_answer}'
          )


if __name__ == '__main__':
    main()
