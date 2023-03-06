# Класс Employee

class Employee:
    def __init__(self, name, ident, department, office):
        self.__name = name
        self.__ident = ident
        self.__department = department
        self.__office = office

    def __str__(self):
        return f'Имя: \t\t\t\t\t\t{self.__name}\n' \
               f'Идентификационнаф номер: \t{self.__ident}\n' \
               f'Отдел: \t\t\t\t\t\t{self.__department}\n' \
               f'Должность: \t\t\t\t\t{self.__office}'