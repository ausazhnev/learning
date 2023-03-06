# Задание #4 к главе 10
# Текст задания находится в файле tasks_ru.txt
# Описание класса Employee находится в файле 'm_employee_10_4.py'
# Исходная таблица с данными находится в файле 'dop\tab_10_4.png'
#
# Task #4 to chapter 10
# The text of the task is in the file tasks_en.txt
# The Employee class is written in the file 'm_employee_10_4.py'
# The original data table is in the file 'dop\tab_10_4.png'

import m_employee_10_4 as employee

worker1 = employee.Employee('Сьюзен Мейерс', 47899, 'Бухгалтерия', 'Вице-презедент')
worker2 = employee.Employee('Марк Джоуне', 39119, 'IT', 'Программист')
worker3 = employee.Employee('Джой Роджерс', 81774, 'Производственный', 'Инженер')

print(worker1)
print()
print(worker2)
print()
print(worker3)


