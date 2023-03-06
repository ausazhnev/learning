# Эта программа расконсервирует объекты CellPhone

import pickle
import cellphone

# константа для имени файла.
FILENAME = 'callphone.dat'


def display_data(phone):
    print(f'Производитель:\t{phone.get_manufact()}')
    print(f'Модель:\t\t\t{phone.get_model()}')
    print(f'Розничная цена:\t{phone.get_retail_price()}')
    print()


def main():
    end_of_file = False  # Для обозначения конца файла

    # Открыть файл.
    with open(f'../dop/{FILENAME}', 'rb') as input_file:
        # Прочитать до конца файл.
        while not end_of_file:
            try:
                # Расконсервируем следующий объект
                phone = pickle.load(input_file)

                # Показать данные о сотовом телефоне
                display_data(phone)
            except EOFError:
                # Устанавливаем флаг, что бы обозначить, что
                # был достигнут конец файла.
                end_of_file = True

    # Така как использован with мы не
    # закрываем открытый файл
    # input_file.close()


if __name__ == '__main__':
    main()
