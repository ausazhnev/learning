# Эта программа импортирует имитационный модуль
# и создает три экземляра класса Coin.

import coin

def main():
    # Создать три экземпляра класса Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Показать повернутую вверх сторону каждой монеты.
    print(f'Вот три монеты, у которых эти стороны обращены вверх: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Подбросить монету.
    print(f'Подбрасываю все три монеты. . .')
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Показать повернутую вверх сторону каждой монеты.
    print(f'Теперь обращены вверх эти стороны: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

if __name__ == '__main__':
    main()
