# Задание #5 к главе 7
# Текст задания находится в файле tasks_ru.txt
# - Доработка
#  - Файл 'charge_accounts.txt'  у меня отсутствует. по этому я его сгенерировал сам.
# Код генерации можно найти в папке 'dop' -> ' 5. generation_charge_accounrs.py'
#
# Task #5 to chapter 7
# The text of the task is in the file tasks_en.txt
# - Modification
#  - The file 'charge_accounts.txt' is missing from me. That's why I generated it myself.
# The generation code can be found in the folder 'dop' -> ' 5. generation_charge_accounrs.py'


def check_account(account_number):
    f_account = open('../dop/charge_accounts.txt', 'r')
    account_list = f_account.readlines()
    if (account_number+'\n') in account_list:
        print(f'Введенный номер доступен.')
    else:
        print(f'Номер не досупен')
    f_account.close()


def get_account():
    check = True
    while check:
        account_number = input(f'Введите семизначный номер счета: ')
        if len(account_number) == 7 and account_number.isnumeric():
            check = False
            return account_number
        elif len(account_number) != 7:
            print(f'Номер счета должен содержать быть семизначным! Повторите ввод.')
        elif not account_number.isdigit():
            print(f'Нужно вводить только числа! Повторите ввод.')


def main():
    account_number = get_account()
    check_account(account_number)


if __name__ == '__main__':
    main()

# Пока писал, нашел более простую реализацию
'''
def get_account():
    check = True
    while check:
        account_number = input(f'Введите семизначный номер счета: ')
        try:
            account_number = int(account_number)
            if 1000000 <= account_number <= 9999999: # такая конструкция по тому, что  
                                                     # account_number уже преобразован в int
                check = False
                return account_number
            else:
                print(f'Номер счета должен содержать быть семизначным! Повторите ввод.')
        except:
            print(f'Нужно вводить только числа! Повторите ввод.')
'''