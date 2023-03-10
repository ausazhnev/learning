# Эта программа создает экземпляр класса SavingAccount
# и экземпляр класса CD

import accounts


def main():
    # Получить данные счета, процентную ставку,
    # и остаток сберегательного счета.
    print(f'Введите данные о сберегательном счете.')
    acct_num = input(f'Номер счета: ')
    int_tate = input(f'Процентная ставка: ')
    balance = float(input(f'Остаток: '))

    # Создаем объект SavingAccount
    saving = accounts.SavingAccount(acct_num, int_tate, balance)

    # Получить номер счета, процентную ставку,
    # остаток на счете и дату погашения счета CD
    print(f'Введите данные о счете CD:')
    acct_num = input(f'Номер счета: ')
    int_tate = input(f'Процентная ставка: ')
    balance = float(input(f'Остаток: '))
    maturity = input(f'Дата погашения: ')

    # Создаем объект CD
    cd = accounts.CD(acct_num, int_tate, balance, maturity)

    # Показать данные
    print(f'Вот введенные Вами данные:')
    print()
    print(f'Сберегательный счет')
    print('--------------------')
    print(f'Номер счета: {saving.get_account_num()}')
    print(f'Процентная ставка: {saving.get_interest_rate()}')
    print(f'Остаток на счете: {saving.get_balance()}')
    print()
    print(f'Счет депозитного сертификата (CD)')
    print('----------------------------------')
    print(f'Номер счета: {cd.get_account_num()}')
    print(f'Процентная ставка: {cd.get_interest_rate()}')
    print(f'Остаток на счете: {cd.get_balance()}')
    print(f'Дата погашения: {cd.get_maturity_date()}')

if __name__ == '__main__':
    main()
