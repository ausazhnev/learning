# Задание (RU)
# Проверка доступности номера расходного счета.
# Среди исходного кода главы 7 вы найдете файл charge_accounts.txt. В нем содержится список допустимых номеров
# расходных счетов компании. Каждый номер счета представляет собой семизначное число, в частности 5658845.
# Напишите программу, которая считывает содержимое файла в список. Затем она должна попросить пользователя ввести
# номер расходного счета. Программа должна определить, что номер является допустимым, путем его поиска в списке.
# Если число в списке имеется, то программа должна вывести сообщение, указывающее на то, что номер допустимый.
# Если числа в списке нет, то программа должна вывести сообщение, указывающее на то что номер недопустим.
# - Доработка
#  - Файл 'charge_accounrs.txt'  у меня отсуствует. по этому я его сгенерировал сам.
# Код генерации можно найти в папке 'dop' -> ' 5. generation_charge_accounrs.py'
#
#
# Task (EN)
# Checking the availability of the expense account number.
# Among the source code of Chapter_7 you will find the file charge_accounts.txt . It contains a list of acceptable
# numbers of the company's expense accounts. Each account number is a seven-digit number, specifically 5658845.
# Write a program that reads the contents of a file into a list. Then it should ask the user to enter the expense
# account number. The program must determine that the number is valid by searching for it in the list.
# If there is a number in the list, the program should display a message indicating that the number is valid.
# If the number is not in the list, the program should display a message indicating that the number is invalid.
# - Modification
#  - The file 'charge_accounrs.txt' is missing from me. That's why I generated it myself.
# The generation code can be found in the folder 'dop' -> ' 5. generation_charge_accounrs.py'


def check_account(account_number):
    f_account = open('dop\\charge_accounts.txt', 'r')
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

# Пока писал нашел более простую реализацию
'''
def get_account():
    check = True
    while check:
        account_number = input(f'Введите семизначный номер счета: ')
        try:
            account_number = int(account_number)
            if 1000000 <= account_number <= 9999999: # такая конструция по тому, что account_number уже 
                                                     # преобразован в int
                check = False
                return account_number
            else:
                print(f'Номер счета должен содержать быть семизначным! Повторите ввод.')
        except:
            print(f'Нужно вводить только числа! Повторите ввод.')
'''