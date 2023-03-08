# Класс RetailItem

class RetailItem:
    def __init__(self, description=None, store=None, price=None):
        self.__description = description
        self.__price = price
        self.__store = store

    def get_name(self):
        return self.__description
    #
    # def get_store(self):
    #     return self.__store
    #
    def get_price(self):
        return self.__price

    def __str__(self):
        return f'Описание: {self.__description}, ' \
               f'Кол-во на складе: {self.__store}, ' \
               f'Цена: {self.__price:.2f}'
