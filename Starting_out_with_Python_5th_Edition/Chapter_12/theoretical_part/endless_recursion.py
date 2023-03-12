# Эта программа демонстрирует рекурсивную функцию.

def massage():
    print(f'Это рекурсивная функция.')
    massage()


def main():
    massage()


if __name__ == '__main__':
    main()
