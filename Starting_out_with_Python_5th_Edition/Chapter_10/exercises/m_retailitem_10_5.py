# Класс RetailItem

class RetailItem:
    def __init__(self, description=None, price=None, store=None):
        self.__description = description
        self.__price = price
        self.__store = store

    def __str__(self):
        return f'Описание: {self.__description}, ' \
               f'Кол-во на складе: {self.__store}, ' \
               f'Цена: {self.__price:.2f}'
