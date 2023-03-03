# Задание #6 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #6 to chapter 2
# The text of the task is in the file tasks_en.txt

F_TAX = 0.05
R_TAX = 0.025

price = float(input(f'Введите стоимость покупки: '))
print(f'Федеральный налог составит: ${price * F_TAX:.2f}')
print(f'Региональный налог составит: ${price * R_TAX:.2f}')
print(f'Общая стоимость с учетом налогов: ${price + (price * F_TAX) + (price * R_TAX):.2f}')
