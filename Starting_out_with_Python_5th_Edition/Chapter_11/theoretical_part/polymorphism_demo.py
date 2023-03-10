# эта программа демонстрирует полиформизм.

import animals

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы
# show_species и make_sound.
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


def main():
    # Создать объект Mammal, объект Dog
    # и объект Cat.
    mammal = animals.Mammal('Обычное животное')
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


if __name__ == '__main__':
    main()
