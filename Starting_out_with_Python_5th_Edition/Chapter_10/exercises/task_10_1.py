# Задание #1 к главе 10
# Текст задания находится в файле tasks_ru.txt
# Описание класса Pet находится в файле 'm_pet_10_1.py':
#
# Task # 1 to chapter 10
# The text of the task is in the file tasks_en.txt
# Описание класса Pet находится в файле 'm_pet_10_1.py':

# Импортируем модуль и даем ему псевдоним 'pet'
import m_pet_10_1 as pet


def main():
    # Создаем объект класса Pet
    my_pet = pet.Pet()
    print(f'Питомец создан!')

    # Установка атрибутов объекта с помощью методов мутаторов
    name = input(f'Введите имя питомца: ')
    my_pet.set_name(name)
    animal_type = input(f'Введите тип питомца: ')
    my_pet.set_animal_type(animal_type)
    age = input(f'Введите возраст питомца: ')
    my_pet.set_age(age)

    # Вывод информации обращаясь к методам получателем
    print(f'Мы знаем о питомце:')
    print(f'Имя питомца: {my_pet.get_name()}')
    print(f'Тип питомца: {my_pet.get_animal_type()}')
    print(f'Возраст питомца: {my_pet.get_age()}')

    # вывод информации через метод __str__() передавая объект в метод
    print(f'Все через метод __str__: {my_pet}')


if __name__ == '__main__':
    main()
