# Задание #12 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #12 to chapter 2
# The text of the task is in the file tasks_en.txt

shares = 2000
buy_price = 40.00
sell_price = 42.75
total = (shares * sell_price) - ((shares * sell_price) * 0.03) - \
        ((shares * buy_price) * 0.03) - (shares * buy_price)
print(f'Джо заплатил за акции:\t\t\t\t${shares * buy_price:,.2f}')
print(f'Джо заплатил брокеру при покупке:\t${(shares * buy_price) * 0.03:,.2f}')
print(f'Джо получил за акций:\t\t\t\t${shares * sell_price}')
print(f'Джо заплатил брокеру при продаже:\t${(shares * sell_price) * 0.03:,.2f}')
print(f'В итоге Джо получил:\t\t\t\t${total:,.2f}')
