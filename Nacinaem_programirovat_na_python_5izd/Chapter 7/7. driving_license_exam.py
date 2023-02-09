# Задание (RU)
# Экзамен на получение водительских прав.
# Местный отдел по выдаче удостоверений на право управления автомобиля попросил вас создать приложение, которое
# оценивает письменную часть экзамена на получение водительских прав. Экзамен состоит из 20 вопросов с множественным
# выбором. Вот правильные ответы: dop\7. correct_answers.txt (7. student_passed.txt 7. student_not_pass.txt)
# Ваша программа должна сохранить эти правильные ответы в список. Программа должна прочитать из текстового файла ответы
# испытуемого на каждый из 20 вопросов и сохранить эти ответы в еще один список. После того как ответы испытуемого
# будут считаны из файла, программа должна вывести сообщение о том, сдал испытуемый экзамен или нет. (Для сдачи
# экзамена испытуемый должен правильно ответить на 15 из 20 вопросов.) Затем программа должна вывести общее количество
# вопросов, ответы на которые были правильные, общее количество вопросов, ответы на которые были не правильные и список
# с номерами вопросов, ответы на которые были неправильными.
# Файлы с правильными ответами и ответами испытуемых находятся в директории dop
#
# Task (EN)
# Driving license exam.
# Your local driving license department has asked you to create an application that evaluates the written portion of
# a driver's license test. The exam consists of 20 multiple choice questions.
# Here are the correct answers: dop\7. correct_answers.txt (7. student_passed.txt 7. student_not_pass.txt)
# Your program must store these correct answers in a list. The program must read the testee's answers to each of the
# 20 questions from a text file and save these answers to another list. After the subject's answers are read from the
# file, the program should display a message indicating whether the subject passed the exam or not. (To pass the exam,
# the test taker must answer 15 out of 20 questions correctly.) The program should then display the total number of
# questions that were correct, the total number of questions that were incorrect, and a list of question numbers
# that were incorrect. .
# Files with the correct answers and the answers of the subjects are located in the dop directory


def get_data(f_name):
    f_answer = open(f'dop\\{f_name}', 'r')
    answer_list =[]
    for value in f_answer:
        value = value.strip('\n')
        answer_list.append(value)
    f_answer.close()
    return answer_list


def cheking_the_result(answer, a_student):
    good_answer = 0
    bad_answer = 0
    bad_list = []
    for i in range(len(answer)):
            if answer[i] == a_student[i]: good_answer += 1
            else:
                bad_answer += 1
                bad_list.append(i+1)
    if bad_answer <= 5: print(f'Поздравялем! Вы прошли тест')
    else: print(f'Ошибок болье 5-и. Попробуйте еще раз')
    print(f'Вы верно ответили на {good_answer} вопросов')
    print(f'Вы не верное ответили на {bad_answer} вопросов')
    if bad_answer > 1: print(f'Вы не верно ответили на вопросы: {bad_list}')


def main():
    orig_answer = get_data('7. correct_answers.txt')
    student_answer = get_data('7. student_not_pass.txt')
    cheking_the_result(orig_answer, student_answer)


if __name__ == '__main__':
    main()
