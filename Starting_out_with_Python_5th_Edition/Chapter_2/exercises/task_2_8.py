# Задание #8 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #8 to chapter 2
# The text of the task is in the file tasks_en.txt

price = float(input(f'Введите общую стоимость блюд: '))
tips = price * 0.18
tax = price * 0.07
print(f'Чаевые: {tips:.2f}\n'
      f'Налог: {tax:.2f}\n'
      f'Итоговая сумма: {price + tips + tax:,.2f}')
