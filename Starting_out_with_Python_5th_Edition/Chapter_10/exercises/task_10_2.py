# Задание #2 к главе 10
# Текст задания находится в файле tasks_ru.txt
# Описание класса Pet находится в файле 'm_car_10_2.py':
#
# Task #2 to chapter 10
# The text of the task is in the file tasks_en.txt
# Описание класса Pet находится в файле 'm_car_10_2.py':

# Импортируем модуль и даем ему псевдоним 'car'
import m_car_10_2 as car


def main():
    # Создаем объект класса Car
    my_car = car.Car(2020, 'Mazda')

    # Изменяем значение атрибута __speed с помощью метода accelerate()
    # и выводим значение на экран с помощью метода get_speed()
    print(f'Ускоряемся. . .')
    for cout in range(5):
        my_car.accelerate()
        print(f'Текущая скорость: {my_car.get_speed()}')

    # Изменяем значение атрибута __speed с помощью метода breaks()
    # и выводим значение на экран с помощью метода get_speed()
    print(f'Тормозим. . .')
    for cout in range(5):
        my_car.breaks()
        print(f'Текущая скорость: {my_car.get_speed()}')


if __name__ == '__main__':
    main()
