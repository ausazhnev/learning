# Эта программа консервирует объекты CellPhone

import pickle
import cellphone

# Константа для хранения имени файла.
FILENAME = 'callphone.dat'

def main():
    # Инициализируем переменную для управления циклом.
    again = 'д'

    with open(f'../dop/{FILENAME}', 'wb') as output_file:

        # Получаем данные от пользователя.
        while again.lower() == 'д':
            # Получаем данные о сотовом телефоне.
            man = input(f'Введите производителя: ')
            mod = input(f'Введите номер модели: ')
            retail = input(f'Введите розничную цену: ')

            # Создать объект CallPhone.
            phone = cellphone.CellPhone(man, mod, retail)

            # Законсервировать объект и записать его в файл
            pickle.dump(phone, output_file)

            # Получить еще один элемент данных?
            again = input(f'Введите еще один элемент данных? (д/н): ')

    # Так как использовался with для работы с файлом,
    # закрывать его не требуется
    print(f'Данные записаны в файл: {FILENAME}')


if __name__ == '__main__':
    main()
