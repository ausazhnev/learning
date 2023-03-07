# Задание #6 к главе 10
# Текст задания находится в файле tasks_ru.txt
# Исходная таблица с данными находится в файле 'dop\tab_10_6.png'
#
# Task #6 to chapter 10
# The text of the task is in the file tasks_en.txt
# The original data table is in the file 'dop\tab_10_6.png'

import m_patient_10_6 as patient, m_procedure_10_6 as procedure


# Создаем нового пациента в ручную
def create_patient():
    # Создаем пациента
    name = input(f'Введите ФИО пациента:\n'
                 f'> > '
                 )
    address = input(f'Введите адрес пациента: (индекс, область,город, улица)\n'
                    f'> > '
                    )
    phone = input(f'Введите контактный номер телефона:\n'
                  f'> > '
                  )
    confidant = input(f'Введите данные контактного лица: (Имя, номер телефона)\n'
                      f'> > '
                      )
    return patient.Patient(name, address, phone, confidant)


# Создаем процедуры по макеты (автоматически)
def auto_procedure(procedure_list):
    proc1 = procedure.Procedure('Врачебный осмотр', 'сегодня', 'Ирвин', 250.00)
    procedure_list.append(proc1)
    proc2 = procedure.Procedure('Рентгенография', 'сегодня', 'Джемисон', 500.00)
    procedure_list.append(proc2)
    proc3 = procedure.Procedure('Анализ крови', 'сегодня', 'Смит', 200.00)
    procedure_list.append(proc3)
    return procedure_list


# Создаем процедуры в ручную (количество не ограничено)
def manual_procedure(procedure_list):
    # Создаем процедуры
    name = input(f'Введите название процедуры:\n'
                 f'> > '
                 )
    date = input(f'Введите дату проведения процедуры:\n'
                 f'> > '
                 )
    doctor = input(f'Введите имя врача который будет проводить процедуру:\n'
                   f'> > '
                   )
    price = float(input(f'Введите стоимость процедуры:\n'
                        f'> > '
                        ))
    new_proc = procedure.Procedure(name, date, doctor, price)
    procedure_list.append(new_proc)
    return procedure_list


# Выводим на экран данные о пациенте
def show_patient(patient):
    # Выводим информацию о пациенте
    print(f'ФИО: {patient.get_name()}')
    print(f'Адрес: {patient.get_address()}')
    print(f'Телефон: {patient.get_phone()}')
    print(f'Доп. контакт: {patient.get_confidant()}')
    print()

# Выводим на экран данные о полученных процедурах
def show_procedure(procedure_list):
    total = 0
    print('Оказанные процедуры')
    print('-' * 34)
    for item in procedure_list:
        print(f'Наименование:     {item.get_name()}')
        print(f'Дата проведения:  {item.get_date()}')
        print(f'Врач исполнитель: {item.get_doctor()}')
        print(f'Стоимость:        {item.get_price():.2f}')
        total += item.get_price()
        print('-' * 34)
    print(f'Общая стоимость процедур: ${total:.2f}')


def main():
    # Данные о пациенте (объект процедура)
    # хранятся в списке
    new_patient = create_patient()

    # Даем пользователю возможность создать процедуры
    # в ручную или заполнить по готовому шаблону
    choice = input(f'Вы хотите ввести процедуры в ручную или заполнить данные автоматически?\n'
                   f'(д/н)\n'
                   f'> > '
                   )
    procedure_list = []
    if choice.lower() == 'д':
        procedure_list = auto_procedure(procedure_list)
    else:
        # Пользователь может в ручную ввести любое число
        # процедур за счет цикла while
        again = 'д'
        while again.lower() == 'д':
            procedure_list = manual_procedure(procedure_list)
            again = input(f'Ввести еще одну процедуру?\n'
                          f'(д/н)\n'
                          f'> > ')
        print(procedure_list)
    # Показать информацию о пациенте
    show_patient(new_patient)
    # Показать проведенные процедуры
    show_procedure(procedure_list)


if __name__ == '__main__':
    main()
