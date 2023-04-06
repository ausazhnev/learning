# Раздел 1 Модуль №3 Часть №9
# текст задания можно найти в файле tasks.txt


# на сайт отправляется только сама функция
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x + (5-(x % 5))

x = int(input('Введите число: '))
print(closest_mod_5(x))