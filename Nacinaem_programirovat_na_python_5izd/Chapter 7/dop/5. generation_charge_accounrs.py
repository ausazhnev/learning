# Генаратор данных для задачи №5
# Номера счетов могут совпадать
#
# Data generator for task #5
# The account numbers may match

import random


def main():
    LIST_SIZE = 10000
    try:
        f_num_list = open('charge_accounts.txt', 'w')
        for i in range(LIST_SIZE):
            f_num_list.write(f'{random.randint(1000000, 9999999)}\n')
    except:
        print(f'Во время работы произошла ошибка')
    else:
        print(f'Файл успешно сгенерирован')
    finally:
        f_num_list.close()


if __name__ == '__main__':
    main()
