# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example
# 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
# Example
# 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
#
# Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


'''Мое решение'''
strs = ["flower", "fl", "flight"]  # Строка для тестирования
prefix_list = []  # Максимальная длинна входящей строки
flag = True  # Флаг для выхода из цикла
min_str = len(strs[0])  # Первично устанавливаем минимальную длину
                        # элемента равной длине первого элемента списка
# Определяем минимальную длину элемента в списке
for elem in strs:
    if min_str > len(elem):
        min_str = len(elem)

# что бы не получить ошибку индекса, индекс элемента списка не привесить полученный min_str
for i in range(min_str):
    # Для каждого индекса элемента, обходим каждый элемент входящего списка
    for j in range(len(strs)):
        # Если значения не равны, то устанавливаем флаг False
        if strs[0][i] != strs[j][i]:
            flag = False
    # Закончив обход с текущим индексом, если флаг не был изменен
    if flag is True:
        # Добавляем значение с текущим индексом в список
        prefix_list.append(strs[0][i])
    else:
        break
# Собираем в переменную максимальный префикс из списка
max_prefix = ''.join(prefix_list)
return max_prefix


'''Альтернативное решение'''
short = min(strs, key=len)  # получаем элемент списка с минимальной длиной (key=len)
for item in strs:  # Обходим каждый элемент входящего массива
    while len(short) > 0:  # Пока длинна минимального элемента больше нуля
        if item.startswith(short):  # Проверяем начинается ли текущий элемент списка с подстроки short
            break  # Если содержит подстроку, то выходим из цикла while, что бы не было лишних итераций
        else:
            # Иначе сокращаем длину строки содержащийся в short на 1, убирая последний символ
            short = short[:-1]  # переменной short присваиваем значение short [от первого, до последнего символа (последний не включается)]
return short