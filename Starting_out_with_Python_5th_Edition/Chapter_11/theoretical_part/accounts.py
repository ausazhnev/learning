# Класс SavingAccount представляет
# сберегательный счет.
class SavingAccount:
    # Метод __init__ принимает аргументы для
    # номера счета, процентной ставки и остатка.
    def __init__(self, account_num, int_rate, bal):
        self.__accoun_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # Следующие ниже методы являются методами-мутаторами
    # атрибутов данных.
    def set_account_num(self, account_num):
        self.__accoun_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    # Следующие ниже методы являются методами-получателями
    # атрибутов данных.
    def get_account_num(self):
        return self.__accoun_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance


# Класс CD представляет счет
# депозитного сертификата (CD).
# Это подкласс класса SavingAccount.
class CD(SavingAccount):
    # Метод __init__ принимает аргументы для
    # номера счета, процентной ставки, остатка
    # и даты погашения.
    def __init__(self, account_num, int_rate, bal, mat_date):
        # Вызываем метод __init__ надкласса.
        SavingAccount.__init__(self, account_num, int_rate, bal)

        # Инициализируем атрибут __maturity_date
        self.__maturity_date = mat_date

    # Метод set_maturity_date является методом-мутатором
    # для атрибута __maturity_date.
    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # Метод get_maturity_date является методом-получателем
    # для атрибута __maturity_date.
    def get_maturity_date(self):
        return self.__maturity_date
