# Задание №12 к главе 8
# Текст задания находится в файле tasks_ru.txt
# решение через слайсы слов
#
# Task №12 to Chapter 8
# The text of the task is in the file tasks_en.txt
# word slice solution

user_string = input(f'[#] > Введите строку для преобразования: ').upper()
user_string = user_string.split()
for word in user_string:
    print(f'{word[1:]}{word[0]}КИ ', sep='', end='')
