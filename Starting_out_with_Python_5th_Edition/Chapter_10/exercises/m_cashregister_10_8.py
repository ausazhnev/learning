# Класс CashRegisrter

class CashRegister:
    def __init__(self):
        self.__items_lst = []

    # Добавить объект в список
    def purchase_item(self, obj):
        self.__items_lst.append(obj)

    # Получить список содержащийся в объекте
    def get_item(self):
        return self.__items_lst

    # Получаем полную стоимость обращаясь к
    # атрибутам класса хранимого объекта
    def get_total(self):
        self.__total = 0
        for item in self.__items_lst:
            self.__total += item.get_price()
        return self.__total

    # Очищаем список
    def clear(self):
        self.__items_lst.clear()

    # для тестов
    # def __str__(self):
    #     return {self.__items_lst}'
