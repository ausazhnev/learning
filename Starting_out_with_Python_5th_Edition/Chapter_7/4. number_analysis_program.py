# Задание (RU)
# Программа анализа чисел
# Разработайте программу, которая просит пользователя ввести ряд из 20 чисел.
# Программа должна сохранить числа в списке и затем показать приведенный ниже данные:
# Наименьшее число в списке
# Наибольшее число в списке
# Сумма чисел в списке
# Среднее арифметическое значение чисел в списке
#
# Task (EN)
# Number Analysis Program
# Develop a program that asks the user to enter a series of 20 numbers.
# The program should save the numbers in the list and then show the following data:
# The smallest number in the list
# The largest number in the list
# The sum of the numbers in the list
# The arithmetic mean of the numbers in the list

def get_numbers():
    numbers_list = []
    for i in range(20):
        numbers_list.append(float(input(f'Введите число №{i+1}: ')))
    return numbers_list


def calculate(numbers_list):
    total = 0
    for value in numbers_list:
        total += value
    print(f'Сумма чисел в списке: {total:.2f}')
    print(f'Среднее арифметическое: {(total / len(numbers_list)):.2f}')
    print(f'Максимальный уровень осадков в году {max(numbers_list):.2f}')
    print(f"Минимальный уровень осадков в году {min(numbers_list):.2f}")


def main():
    print(f'Введите 20 целых чисел для анализа.')
    numbers_list = get_numbers()
    calculate(numbers_list)


if __name__ == '__main__':
    main()
