# Эта программа имитирует головоломку 'Ханойские башни'.

def main():
    # Задать несколько исходных значений.
    num_discs = 3
    from_ped = 1
    to_peg = 3
    temp_peg = 2

    # Решить головоломку
    move_discs(num_discs, from_ped, to_peg, temp_peg)
    print(f'Все кольца перемещены!')


# Функция move_discs() демонстрирует процесс перемещения
# колец в головоломке "Ханойские башни".
# Параметры функции:
# num_discs - количество перемещаемых колец.
# from_ped - стержень, с которого взять кольцо.
# to_peg - стержень, на который кольцо перемещается.
# temp_peg - временный стержень.
def move_discs(num_discs, from_ped, to_peg, temp_peg):
    if num_discs > 0:
        move_discs(num_discs-1, from_ped, temp_peg, to_peg)
        print(f'Переместить кольцо со стрежня {from_ped} на стержень {to_peg}')
        move_discs(num_discs-1, temp_peg, to_peg, from_ped)


if __name__ == '__main__':
    main()
