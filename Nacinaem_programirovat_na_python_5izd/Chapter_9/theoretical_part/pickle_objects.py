# демонстрация консервации объектов

# demonstration of conservation of objects

import pickle


def save_data(file):
    # Создаем пустой словарь
    person = {}
    # Собираем данные от пользователя
    person['Name'] = input(f'[#] > Введите имя:\n'
                           f'[#] > > '
                           )
    person['Age'] = input(f'[#] > Введите возраст:\n'
                          f'[#] > > '
                          )
    person['Mass'] = input(f'[#] > Введите массу тела:\n'
                           f'[#] > > '
                           )
    # консервация данных
    pickle.dump(person, file)


def main():
    again = 'д'
    with open('..\\dop\\info.dat', 'wb') as f_info:
        while again.lower() == 'д':
            save_data(f_info)
            again = input(f'[#] > Повторить ввод данных ? (д/н):\n'
                          f'[#] > > '
                          )


if __name__ == '__main__':
    main()
