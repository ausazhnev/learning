# Эта программа имеет рекурсивную функцию.

def main():
    # Первый аргумент 5 в функцию massage,
    # мы сообщаем ей, что нужно показать
    # сообщение 5 раз.
    massage(5)


def massage(times):
    if times > 0:
        print(f'Это рекурсивная функция.')
        massage(times - 1)


if __name__ == '__main__':
    main()
