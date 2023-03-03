# Задание #11 к главе 2
# Текст задания находится в файле tasks_ru.txt
#
# Task #11 to chapter 2
# The text of the task is in the file tasks_en.txt

man = int(input(f'Сколько в классе мальчиков?: '))
girl = int(input(f'Сколько в классе девочек?: '))
all = man + girl
print(f'В классе {(man / all) * 100:.0f}% мальчиков')
print(f'В классе {(girl / all) * 100:.0f}% девочек')
