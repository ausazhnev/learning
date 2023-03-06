import random

# Класс Coin имитирует монету, которую
# можно подбрасывать (теперь это модуль, который хранится в файле).


class Coin:
    # Метод __init__ инициализирует
    # атрибут данных __sideup значением 'Орел'
    def __init__(self):
        self.__sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если число
    # равно 0, то __sideup получает значение 'Орел'.
    # В противном случае __sideup получает значение 'Решка'
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается __sideup
    def get_sideup(self):
        return self.__sideup
