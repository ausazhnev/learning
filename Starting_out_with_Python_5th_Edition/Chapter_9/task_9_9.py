# Задание #9 к главе 9
# Текст задания находится в файле tasks_ru.txt
#
# Task #9 to chapter 9
# The text of the task is in the file tasks_en.txt

import random


# создаем новую колоду карт
def create_deck():
    deck = {'2 червей': 2, '3 червей': 3, '4 червей': 4, '5 червей': 5, '6 червей': 6,
            '7 червей': 7, '8 червей': 8, '9 червей': 9, '10 червей': 10, 'Валет червей': 10,
            'Дама червей': 10, 'Король червей': 10, 'Туз червей': 1,

            '2 бубей': 2, '3 бубей': 3, '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
            '7 бубей': 7, '8 бубей': 8, '9 бубей': 9, '10 бубей': 10, 'Валет бубей': 10,
            'Дама бубей': 10, 'Король бубей': 10, 'Туз бубей': 1,

            '2 треф': 2, '3 треф': 3, '4 треф': 4, '5 треф': 5, '6 треф': 6,
            '7 треф': 7, '8 треф': 8, '9 треф': 9, '10 треф': 10, 'Валет треф': 10,
            'Дама треф': 10, 'Король треф': 10, 'Туз треф': 1,

            '2 пик': 2, '3 пик': 3, '4 пик': 4, '5 пик': 5, '6 пик': 6,
            '7 пик': 7, '8 пик': 8, '9 пик': 9, '10 пик': 10, 'Валет пик': 10,
            'Дама пик': 10, 'Король пик': 10, 'Туз пик': 1,
            }
    return deck


# выбираем случайную карту из колоды и "передаем" ее игроку
def deal(deck, player):
    card = random.choice(list(deck))
    # если выпадает туз, проверяем какое значение ему присвоить.
    # для этого получаем сумму очков в руке пользователя
    if deck.get(card) == 1:
        if 21 >= (sum(player.values()) + 11):
            player[card] = 11
            deck.pop(card)
        else:
            player[card] = deck.pop(card)
    else:
        player[card] = deck.pop(card)


# отрисовываем стол этого раунда
def show_table(pc, user, cout_pc, cout_user, massage):
    card_str = ''
    print(f'------------------------------------------------------------')
    print(f'|'.ljust(2), end='')
    print(f'Карты дилера: '.center(56), end='')
    print(f'|'.rjust(2))
    for card in pc: card_str += card + ' | '
    print(f'|'.ljust(2), end='')
    print(f'| {card_str}'.center(56), end='')
    card_str = ''
    print(f'|'.rjust(2))
    print(f'|'.ljust(2), end='')
    print(f'Всего очков: {cout_pc}'.center(56), end='')
    print(f'|'.rjust(2))
    print(f'|-------------------- '.ljust(17), end='')
    print(f'{massage}'.center(16), end='')
    print(f' --------------------|'.rjust(17))
    print(f'|'.ljust(2), end='')
    print(f'Карты игрока: '.center(56), end='')
    print(f'|'.rjust(2))
    for card in user: card_str += card + ' | '
    print(f'|'.ljust(2), end='')
    print(f'| {card_str}'.center(56), end='')
    print(f'|'.rjust(2))
    print(f'|'.ljust(2), end='')
    print(f'Всего очков: {cout_user}'.center(56), end='')
    print(f'|'.rjust(2))
    print(f'------------------------------------------------------------')


# проверяем результаты в руке каждого игрока
def analysis(pc, user, end_game, cout_raund, deck):
    cout_pc = sum(pc.values())
    cout_user = sum(user.values())
    # логика выбора победителя
    cout_raund += 1
    if cout_pc >= 21 or cout_user >= 21:
        end_game = True
        if cout_pc > 21 and cout_user > 21:
            massage = 'Ничья'
        elif (cout_user < cout_pc or cout_user == 21) and cout_pc != 21:
            massage = 'Игрок победил'
        else:
            massage = 'Дилер победил'
    else:
        massage = f'Раунд: {cout_raund}'
    show_table(pc, user, cout_pc, cout_user, massage)
    # если колода закончилась
    if len(deck) == 0:
        print(f'Колода закончилась')
        end_game = True
    return cout_raund, end_game


# Если словарь deck пуст, спрашиваем у пользователя создать ли новую колоду
def new_game():
    user_change = input(f'Открыть новую колоду карт? \n'
                        f'да - "д", нет - любое другое\n'
                        f'> > '
                        )
    if user_change.lower() == 'д': return True
    else: return False


def main():
    pc_player, user_player = {}, {}
    cout_raund = 0
    end_game = False
    # создаем новую колоду
    deck = create_deck()
    while not end_game:
        # если колода не пустая сдаем карты на стол
        if len(deck) != 0:
            deal(deck, pc_player)
            deal(deck, user_player)
            cout_raund, end_game = analysis(pc_player, user_player, end_game, cout_raund, deck)
        else:
            #  Запрашиваем, открыть ли новую колоду
            if new_game():
                deck = create_deck()
            else:
                print(f'Спасибо за игру. Приходи еще.')
                break
        print()
        # когда победитель определен
        if end_game:
            end_game = False
            pc_player = {}
            user_player = {}
            cout_raund = 0


if __name__ == '__main__':
    main()
