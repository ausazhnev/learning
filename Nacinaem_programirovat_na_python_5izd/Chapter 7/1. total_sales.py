# Задание (RU)
# Общий объем продаж
# Разработайте программу, которая просит пользователя ввести продажи магазина за каждый день недели. Суммы должны
# храниться в списке. Примените цикл, что бы вычислить объем продаж за неделю и показать результат.
#
# Task (EN)
# Total Sales
# Develop a program that asks the user to enter the store's sales for each day of the week. The amounts must be
# stored in a list. Apply a loop to calculate weekly sales and show the result.

def get_daily_sales(day_list):
    days_sales_list = []
    for day in day_list:
        if day != 'Вторник':
            days_sales_list.append(float(input(f'Сумма продаж в {day}: ')))
        else:
            days_sales_list.append(float(input(f'Сумма продаж во {day}: ')))
    return days_sales_list


def weekly_sales(sales_for_week):
    total = 0
    for value in sales_for_week:
        total += value
    return total


def main():
    DAYS_WEEK = ('Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу', 'Воскресенье')
    print(f'Введите продажи торговой точки за каждый день недели:')
    days_sales_list = get_daily_sales(DAYS_WEEK)
    print(f'Суммрные продажи за неделю составлют {weekly_sales(days_sales_list)} руб')


if __name__ == '__main__':
    main()
