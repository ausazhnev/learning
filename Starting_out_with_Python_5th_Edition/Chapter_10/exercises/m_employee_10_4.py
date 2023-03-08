# Класс Employee

class Employee:
    def __init__(self, name, ident, department, office):
        self.__name = name
        self.__ident = ident
        self.__department = department
        self.__office = office

    # Методы-мутаторы
    def set_name(self, name):
        self.__name = name

    def set_ident(self, ident):
        self.__ident = ident

    def set_department(self, department):
        self.__department = department

    def set_office(self, office):
        self.__office = office

    # Методы-получатели
    def get_name(self):
        return self.__name

    def get_ident(self):
        return self.__ident

    def get_department(self):
        return self.__department

    def get_office(self):
        return self.__office

    def __str__(self):
        return f'Имя: \t\t\t\t\t\t{self.__name}\n' \
               f'Идентификационнаф номер: \t{self.__ident}\n' \
               f'Отдел: \t\t\t\t\t\t{self.__department}\n' \
               f'Должность: \t\t\t\t\t{self.__office}'