# Задание #1 к главе 7
# Текст задания находится в файле tasks_ru.txt
#
# Task #1 to chapter 7
# The text of the task is in the file tasks_en.txt

DAYS_WEEK = ('Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу', 'Воскресенье')


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
    print(f'Введите продажи торговой точки за каждый день недели:')
    days_sales_list = get_daily_sales(DAYS_WEEK)
    print(f'Суммарные продажи за неделю составляют {weekly_sales(days_sales_list)} руб')


if __name__ == '__main__':
    main()
