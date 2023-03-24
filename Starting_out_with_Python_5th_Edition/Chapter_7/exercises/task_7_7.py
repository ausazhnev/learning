# Задание #7 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #7 to chapter 7
# The text of the task is in the file tasks_en.txt

MAX_ERROR = 5


def get_data(f_name):
    with open(f'dop\\{f_name}', 'r') as f_answer:
        answer_list = []
        for value in f_answer:
            value = value.strip('\n')
            answer_list.append(value)
    return answer_list


def check_student_answers(answer, a_student):
    good_answer = 0
    bad_answer_list = []
    for i in range(len(answer)):
        if answer[i] == a_student[i]:
            good_answer += 1
        else:
            bad_answer_list.append(i+1)
    if len(bad_answer_list) <= MAX_ERROR:
        print(f'Поздравляем! Вы прошли тест')
    else:
        print(f'Тест провален! ошибок более {MAX_ERROR}. Запишитесь на пересдачу')
        print(f'Вы верно ответили на {good_answer} вопросов')
        print(f'Вы не верное ответили на {len(bad_answer_list)} вопросов')
        print(f'Вы не верно ответили на вопросы: {bad_answer_list}')


def main():
    orig_answer = get_data('7. correct_answers.txt')
    student_answer = get_data('7. student_not_pass.txt')
    check_student_answers(orig_answer, student_answer)


if __name__ == '__main__':
    main()
