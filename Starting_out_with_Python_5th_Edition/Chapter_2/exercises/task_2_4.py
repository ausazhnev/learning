# Задание #4 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #4 to chapter 2
# The text of the task is in the file tasks_en.txt

TAX = 0.07

product1 = float(input(f'Введите стоимость товара #1: '))
product2 = float(input(f'Введите стоимость товара #2: '))
product3 = float(input(f'Введите стоимость товара #3: '))
product4 = float(input(f'Введите стоимость товара #4: '))
product5 = float(input(f'Введите стоимость товара #5: '))

all_product = product1 + product2 + product3 + product4 + product5
tax_product = all_product * TAX
print(f'Общая стоимость товаров ${all_product:.2f}\n'
      f'Сумма налога: ${tax_product:.2f}\n'
      f'Итоговая сумма: ${all_product + tax_product:.2f}')
