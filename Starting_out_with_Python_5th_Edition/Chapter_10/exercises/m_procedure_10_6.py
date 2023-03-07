# Класс Procedure
class Procedure:
    def __init__(self, name, date, doctor, price):
        self.__name = name
        self.__date = date
        self.__doctor = doctor
        self.__price = price

    # Методы-мутаторы
    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_price(self, price):
        self.__price = price

    # Методы-получатели
    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_doctor(self):
        return self.__doctor

    def get_price(self):
        return self.__price