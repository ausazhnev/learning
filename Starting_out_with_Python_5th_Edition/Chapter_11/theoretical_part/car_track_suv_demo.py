# Эта программа создает объекты Car, Truck
# и SUV

import vehicles


def main():
    # Создать объект Car для подержанного авто 2001 BMW
    # с 70000 милями пробега, ценой $15000
    # с 4 дверями.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Создать объект Truck для подержанного пикапа 2002
    # Toyota с 40000 милями пробега, ценой
    # $12000 с 4-колесным приводом.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, 4)

    # Создать объект suv для подержанного 2000
    # Volvo с 30000 милями пробега, ценой
    # $18500 и вместимостью 5 человек.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print(f'ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print(f'==========================')

    # Показать данные легкового автомобиля
    print(f'Изготовитель: {car.get_make()}')
    print(f'Модель: {car.get_model()}')
    print(f'Пробег: {car.get_mileage()}')
    print(f'Цена: {car.get_price()}')
    print(f'Количество дверей: {car.get_doors()}')
    print()

    # Показать данные пикапа
    print(f'Изготовитель: {truck.get_make()}')
    print(f'Модель: {truck.get_model()}')
    print(f'Пробег: {truck.get_mileage()}')
    print(f'Цена: {truck.get_price()}')
    print(f'Количество дверей: {truck.get_drive_type()}')
    print()

    # Показать данные джипа
    print(f'Изготовитель: {suv.get_make()}')
    print(f'Модель: {suv.get_model()}')
    print(f'Пробег: {suv.get_mileage()}')
    print(f'Цена: {suv.get_price()}')
    print(f'Количество дверей: {suv.get_pass_cap()}')


if __name__ == '__main__':
    main()
