# Именованная константа
SPEED_CHANGE = 5


# Класс Car
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Метод увеличивает атрибут __speed на 5
    def accelerate(self):
        self.__speed += 5

    # Метод уменьшает атрибут __speed на 5
    def breaks(self):
        self.__speed -= 5

    # Метод возвращает значение атрибута __speed
    def get_speed(self):
        return self.__speed
