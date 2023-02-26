# RU
# Задание №1 к главе 8
# Текст задания находится в файле tasks_ru.txt
# функция "check"  проверяет введенное пользователем значение. Если введено не число
# запрашивается повторный ввод данных
#
# EN
# Task №1 to chapter 8
# The text of the task is in the file tasks_en.txt
# the "check" function checks the value entered by the user. If not a number,
# you are asked to re-enter the data

def get_user_data():
    user_data = input(f'Введите число: ')
    if check(user_data) == False:
        user_data = get_user_data()
    return user_data


def check(user_data):
    if not user_data.isdigit():
        print(f'Необходимо ввести число! Попробуйте снова.')
        return False


def show_result(user_data, result, tesult_str):
    print(f'Результат сложения всех однозначных чисел из {user_data} \n'
          f'составляет {result} = {tesult_str}')


def calculation(user_data):
    total = 0
    total_str = str(user_data[0])
    for num in user_data:
        total += int(num)
        if total > int(num):
            total_str += '+' + num
    return total, total_str


def main():
    user_data = get_user_data()
    result, result_str = calculation(user_data)
    show_result(user_data, result, result_str)


if __name__ == '__main__':
    main()
