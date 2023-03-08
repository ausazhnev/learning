# Задание #8 к главе 10
# Текст задания находится в файле tasks_ru.txt
#
# Task #8 to chapter 10
# The text of the task is in the file tasks_en.txt

import m_retailitem_10_5 as retailitem
import m_cashregister_10_8 as cashregister


# Создаем список всех продуктов которые будут использоваться для продажи
# продукты хранятся в списке для удобства дальнейшей работы с ними
def create_product():
    product_list = []
    product1 = retailitem.RetailItem('Пинжак', 12, 59.95)
    product_list.append(product1)
    product2 = retailitem.RetailItem('Дизайнерские джинсы', 40, 34.95)
    product_list.append(product2)
    product3 = retailitem.RetailItem('Рубашка', 20, 25.95)
    product_list.append(product3)
    product4 = retailitem.RetailItem('Носки', 102, 1.95)
    product_list.append(product4)
    product5 = retailitem.RetailItem('Трусы', 85, 2.25)
    product_list.append(product5)
    return product_list


# Добавляем выбранный продукт в корзину пользователя
# значение item при обращении к списку корректируется на 1
# так как в меню выбора товары начинаются с 1 а не с 0
def choice_product(product_list):
    print(f'Добавить товар в корзину:')
    for item in range(len(product_list)):
        print(f'[{item+1}] > {product_list[item]}')
    return int(input(f'Введите номер товара для добавления в корзину '
                     f'или 0 что бы завершить покупки: '
                     ))


# Добавляем в список новый объект
def add_in_register(product_list, report, choice):
    choice -= 1
    report.purchase_item(product_list[choice])
    print(f'Товар {product_list[choice].get_name()}, добавлен в козину')


# Показать общий чек с добавленными товарами
def show_report(report):

    for item in report.get_item():
        print(item)
    # Итоговая стоимость покупки.
    print(f'всего к оплате: ${report.get_total():.2f}')


def main():
    product_list = create_product()
    report = cashregister.CashRegister()
    choice = None
    while choice != 0:
        choice = choice_product(product_list)
        if choice != 0:
            add_in_register(product_list, report, choice)
    # Когда корзина собрана передаем ее для формирования чека
    show_report(report)
    # Очищаем содержимое списка хранящего объекты
    report.clear()


if __name__ == '__main__':
    main()
