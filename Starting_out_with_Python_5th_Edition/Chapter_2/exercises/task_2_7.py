# Задание #7 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #7 to chapter 2
# The text of the task is in the file tasks_en.txt

distance = float(input(f'Введите пройденное расстояние (км): '))
fuel = float(input(f'Введите объем потраченного топлива (л): '))
print(f'Расход топлива составляет {fuel / distance:.2f} л/км')
