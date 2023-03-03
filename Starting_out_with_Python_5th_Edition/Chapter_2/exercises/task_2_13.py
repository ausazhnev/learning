# Задание #13 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #13 to chapter 2
# The text of the task is in the file tasks_en.txt

beds_length = float(input(f'Введите длину гряды (м): '))
loza_length = float(input(f'Пространство которое занимает виноградная лоза (м): '))
delta_loz = float(input(f'Расстояние между лозами (м): '))
cout_loz = (beds_length - 2 * loza_length) / delta_loz
print(f'Вы можете посадить {cout_loz} лоз')
