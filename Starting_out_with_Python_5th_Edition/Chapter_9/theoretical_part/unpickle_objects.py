# Демонстрация расконсервации объектов

# Demonstration of depreservation of objects

import pickle


#  Вывести на экран расконсервированный словарь
def display_data(data):
    print(f'[#] > Имя > {data["Name"]}')
    print(f'[#] > Возраст > {data["Age"]}')
    print(f'[#] > Масса > {data["Mass"]}')


def main():
    end_of_file = False  # флаг окончания файла
    with open('..\\dop\\info.dat', 'rb') as f_data:
        while not end_of_file:
            try:
                # расконсервировать объект полученый из файла в данной итерации цикла
                person = pickle.load(f_data)
                # показать объект
                display_data(person)
                print(f'[#] >')
            except EOFError:
                # Изменить флаг окончания файла.
                end_of_file = True


if __name__ == '__main__':
    main()
