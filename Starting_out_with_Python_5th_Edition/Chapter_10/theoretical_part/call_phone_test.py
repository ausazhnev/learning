# Эта программа тестирует класс CellPhone

import cellphone


def main():
    # Получить данные о телефоне.
    man = input(f'Введите производителя: ')
    mod = input(f'Введите номер модели: ')
    retail = float(input(f'Введите розничную цену: '))

    # Создать экземпляр класса CellPhone
    phone = cellphone.CellPhone(man, mod, retail)

    # Показать введенные данные.
    print(f'Вот введенные Вами данные:')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')


if __name__ == '__main__':
    main()
