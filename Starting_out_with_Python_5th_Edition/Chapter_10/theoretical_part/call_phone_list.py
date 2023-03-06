# Эта программа создает пять обектов CellPhone
# и сохраняет их в список

import cellphone


def main():
    # Получить список объектов CellPhone.
    phones = make_list()
    # Показать данные в списке
    display_list(phones)


def make_list():
    # Создать пустой список.
    phone_list = []

    # Добавить пять объектов CellPhone в список.
    print(f'Введите данные о пяти телефонах.')
    for cout in range(1, 6):
        # Получить данные о телефоне.
        print(f'Номер телефона {cout}:')
        man = input(f'Введите производителя: ')
        mod = input(f'Введите номер модели: ')
        retail = float(input(f'Введите розничную цену: '))
        print()

        # Создать новый объект CellPhone в памяти
        # и присвоить его переменной phone
        phone = cellphone.CellPhone(man, mod, retail)

        # Добавить объект в список
        phone_list.append(phone)

    return phone_list

# Функция distlay_list принимает список с объектами
# CellPhone в качестве аргумента и показывает
# хранящиеся в каждом объекте данные


def display_list(phone_list):
    for item in phone_list:
        print(item)
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


if __name__ == '__main__':
    main()
