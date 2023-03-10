# Задание #2 к главе 11
# Текст задания находится в файле tasks_ru.txt
# Описание класса Employee и класса ShiftSupervisor находится
# в файле 'modul_11_1.py'
#
# Task #2 to chapter 11
# The text of the task is in the file tasks_en.txt
# The description of the Employee class and the ShiftSupervisor
# class is in file 'modul_11_1.py'

import modul_11_1 as worker


def main():
    super_worker = worker.ShiftSupervisor()
    print(f'Введите данные сотрудника:')
    print(f'==========================')
    super_worker.set_name(input(f'Введите имя старшего смены: '))
    super_worker.set_id_num(input(f'Введите идентификационный номер: '))
    super_worker.set_annual_salary(input(f'Введите размер оклада: '))
    super_worker.set_annual_bonus(input(f'Введите размер годового бонуса: '))
    print()
    print(f'==========================')
    plan = input(f'Годовой план выполнен ? (д/н) ')
    print(f'==========================')
    print(f'Сводные данные:')
    print(f'Старший смены: {super_worker.get_name()} id:{super_worker.get_id_num()}')
    print(f'Базовый оклад: {super_worker.get_annual_salary()}')
    if plan.lower() == 'д': plan = 'выполнен'
    else: plan = 'не выполнен'
    print(f'Статус годового плана: {plan}')
    if plan == 'выполнен': print(f'Годовой бонус к выплате: {super_worker.get_annual_bonus()}')


if __name__ == '__main__':
    main()
