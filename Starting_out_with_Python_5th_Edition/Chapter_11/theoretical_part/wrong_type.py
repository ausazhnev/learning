# выволнение завершится ошибкой!
# AttributeError: 'str' object has no attribute 'show_species'


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


def main():
    # Передать символьное значение в функцию show_mammal_info
    show_mammal_info('Я - последовательность символов')


if __name__ == '__main__':
    main()
