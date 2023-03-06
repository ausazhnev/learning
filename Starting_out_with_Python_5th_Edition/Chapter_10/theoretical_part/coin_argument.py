# Эта программа передает объект Coin
# в качестве аргумента в функцию

import coin


# Эта функция подбрасывает монету
def flip(obj):
    obj.toss()


def main():
    # Создать объект Coin
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орел'
    print(my_coin.get_sideup())

    # Передает объект в функцию flip
    flip(my_coin)

    # Эта инструкция может показать
    # 'Орел' либо 'Решка'
    print(my_coin.get_sideup())


if __name__ == '__main__':
    main()
