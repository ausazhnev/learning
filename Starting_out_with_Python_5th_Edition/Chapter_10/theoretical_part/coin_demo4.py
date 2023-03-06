# Эта программа импортирует модуль coin
# и создает экземпляр класса Coin

import coin
def main():
    # Создать объект на основе класса Coin.
    my_coin = coin.Coin()

    # Показать обращенную вверх сторону монеты.
    print(f'Эта сторона обращена вверх: {my_coin.get_sideup()}')

    # Подбрасываем монету.
    print(f'Я собираюсь подбросить монету десять раз:')
    for cout in range(10):
        my_coin.toss()
        print(f'{my_coin.get_sideup()}')


if __name__ == '__main__':
    main()
