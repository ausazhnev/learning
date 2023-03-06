# Эта программа демонстрирует класс BankAccount.

import bankaccount


def main():
    # Получить начальный остаток на счете
    start_bal = float(input(f'Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    saving = bankaccount.BankAccount(start_bal)

    # Внести на счет зарплату пользователя
    pay = float(input(f'Сколько вы получили на этой неделе? '))
    print(f'Вношу эту сумму на Ваш счет. . . ')
    saving.deposit(pay)

    # Показать остаток на счете
    print(f'Ваш остаток на счете составляет ${saving.get_balance():,.2f}')

    # Получить сумму для снятия с банковского счета.
    cash = float(input(f'Какую сумму Вы желаете снять со счета? '))
    print(f'Снимаю эту сумму с Вашего банковского счета.')
    saving.withdraw(cash)

    # Показать остаток.
    print(f'Ваш остаток на счете составляет ${saving.get_balance():,.2f}')


if __name__ == '__main__':
    main()
