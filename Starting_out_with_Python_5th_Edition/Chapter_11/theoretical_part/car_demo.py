# Эта программа демонстрирует класс Car.

import vehicles


def main():
    # Создать объект на основе класса Car.
    # Легковое авто: 2007 Audi с 12500 милями пробега,
    # ценой $21500.00 и с 4 дверями.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Показать данные легкового автомобиля.
    print(f'Изготовитель: {used_car.get_make()}')
    print(f'Модель: {used_car.get_model()}')
    print(f'Пробег: {used_car.get_mileage()}')
    print(f'Цена: {used_car.get_price()}')
    print(f'Количество дверей: {used_car.get_doors()}')


if __name__ == '__main__':
    main()
