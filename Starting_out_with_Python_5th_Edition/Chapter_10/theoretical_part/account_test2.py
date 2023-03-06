# Эта программа демонстрирует класс BankAccount
# с добавлением в него метод __str__.

import bankaccount2


def main():
    # Получить начальный остаток.
    start_bal = float(input(f'Введите свой начальный баланс: '))

    # Создать объект BankAccount.
    saving = bankaccount2.BankAccount(start_bal)

    # Внести на счет зарплату пользователя
    pay = float(input(f'Сколько вы получили на этой неделе? '))
    print(f'Вношу эту сумму на Ваш счет. . . ')
    saving.deposit(pay)

    # Показать остаток
    print(saving)

    # Получить сумму для снятия с банковского счета.
    cash = float(input(f'Какую сумму Вы желаете снять со счета? '))
    print(f'Снимаю эту сумму с Вашего банковского счета.')
    saving.withdraw(cash)

    # Показать остаток
    print(saving)


if __name__ == '__main__':
    main()
