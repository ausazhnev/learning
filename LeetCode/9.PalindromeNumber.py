# 9. Palindrome Number
# Easy
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore
# it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Переменная x содержит данные для тестирования
x = 10010014753
# Присваиваем переменной result значение True
result = True
# Преобразуем тип переменной х в строку
x = str(x)
# Определяем индекс последнего элемента входящего в строку
count = len(x) - 1
# Запускаем цикл, но проходить его будем до половины длинны массива + 1 символ
for i in range((count // 2) + 1):
    # Если значение символа с текущим индексом равно значению
    # с индексом идущем в обратном порядке продолжаем сравнение
    if x[i] == x[count]:
        # Перемещаем позицию индекса на 1
        count -= 1
    # Если значения не равны, меняем значение переменной result на False
    else:
        result = False
        # Прерываем цикл, так как результат уже не изменится
        break
# Выводим / возвращаем значение переменной result
print(result)

