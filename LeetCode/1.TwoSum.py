# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target. You may assume that each input would have exactly one solution, and
# you may not use the same element twice. You can return the answer in any order.

# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]


def my(nums, target):
    for i in range(len(nums)):
        # Вычисляем с каким значением нужно сложить значение
        # переменной i что бы получить target
        temp = target - nums[i]
        try:
            # Проверяем есть ли в списке значение равное переменной temp,
            # если значение найдено, то присваиваем индекс переменной j.
            # Начальной позицией для поиска является позиция следующая за текущим значением i
            j = nums.index(temp, i+1)
            # Если такое значение найдено, переменной j присваивается номер индекса
            # найденного элемента и возвращаем индексы
            return [i, j]
        # Если в списке не находится значение равное значению
        # переменной temp, вызывается исключение и цикл переходит
        # к следующему значению из списка
        except ValueError:
            pass


# Выводим на экран, значение индексов искомых элементов
# для ответа на leetcode эти строки не нужны
nums, target = [3, 2, 4], 6
print(my(nums, target))
