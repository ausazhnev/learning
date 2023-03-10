# Эта программа демонстрирует полиформизм.

import animals


# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы
# show_species и make_sound.
def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('Это не млекопитающее')


def main():
    # Создать объект Mammal, объект Dog
    # и объект Cat
    mammal = animals.Mammal('обычное животно')
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном.
    print(f'вот несколько животных \n'
          f'и звуки которые они издаю.'
          )
    print(f'-------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('Я - последовательность символов')


if __name__ == '__main__':
    main()
