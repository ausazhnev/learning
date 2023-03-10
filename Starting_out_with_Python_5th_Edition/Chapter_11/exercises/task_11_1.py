# Задание #1 к главе 11
# Текст задания находится в файле tasks_ru.txt
# Описание класса Employee и класса ProductionWorker находится
# в файле 'modul_11_1.py'
#
# Task # 1 to chapter 11
# The text of the task is in the file tasks_en.txt
# The description of the Employee class and the ProductionWorker
# class is in file 'modul_11_1.py'

import modul_11_1 as employee

# Константы для обозначения смен
DAY_SHIFT = 1
NIGHT_SHIFT = 2

def main():
    worker = employee.ProductionWorker()
    print(f'Введите данные о сотруднике:')
    print(f'----------------------------')
    worker.set_name(input(f'Введите имя сотрудника: '))
    worker.set_id_num(input(f'Введите идентификационный номер сотрудника: '))
    worker.set_working_shift(input(f'Выберете смену [1] - дневная, [2] - ночная: '))
    worker.set_hourly_rate(input(f'Введите почасовую ставку: '))
    print()
    print(f'Вот введенные Вами данные:')
    print(f'--------------------------')
    print(f'Имя сотрудника: {worker.get_name()}')
    print(f'Идентификационный номер сотрудника: {worker.get_id_num()}')
    # Получаем числовое обозначение смены и конвертируем в текст
    if worker.get_working_shift() == DAY_SHIFT: shift = 'дневную'
    else: shift = 'ночную'
    print(f'Сотрудник работает в {shift} смену.')
    print(f'Почасовая ставка: {worker.get_hourly_rate()}')


if __name__ == '__main__':
    main()
