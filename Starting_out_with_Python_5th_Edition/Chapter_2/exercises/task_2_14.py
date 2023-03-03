# Задание #14 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #14 to chapter 2
# The text of the task is in the file tasks_en.txt

p = float(input(f'Какую сумму вносим на счет: '))
r = float(input(f'Годовая процентная ставка: '))
r = r / 100
n = int(input(f'Частота начисления процентного дохода в год: '))
t = int(input(f'конкретное количество лет: '))
total = p * (1 + (r / n)) ** (n * t)
print(f'Через {t} лет, вы получите: ${total:,.2f}')
