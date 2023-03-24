# Задание #4 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #4 to chapter 7
# The text of the task is in the file tasks_en.txt

def get_user_numbers():
    numbers_list = []
    for i in range(20):
        numbers_list.append(float(input(f'Введите число №{i+1}: ')))
    return numbers_list


def show_result(numbers_list):
    print(f'Сумма чисел в списке: {sum(numbers_list):.2f}')
    print(f'Среднее арифметическое: {(sum(numbers_list) / len(numbers_list)):.2f}')
    print(f'Максимальный уровень осадков в году {max(numbers_list):.2f}')
    print(f"Минимальный уровень осадков в году {min(numbers_list):.2f}")


def main():
    print(f'Введите 20 целых чисел для анализа.')
    numbers_list = get_user_numbers()
    show_result(numbers_list)


if __name__ == '__main__':
    main()
