# 1. Что покажет приведенная ниже программа?
# def main():
#     num = 0
#     show_me(num)
# def show_me(arg):
#     if arg < 10:
#         show_me(arg+1)
#     else:
#         print(arg)
# main()
# Результат выполнения
# > 10

# 2. Что покажет приведенная ниже программа?
# def main():
#     num = 0
#     show_me(num)
# def show_me(arg):
#     print(arg)
#     if arg < 10:
#         show_me(arg+1)
# main()
# Результат выполнения
# > 0
# > 1
# > 2
# > 3
# > 4
# > 5
# > 6
# > 7
# > 8
# > 9
# > 10

# 3. В приведенной ниже функции применен цикл. Перепишите его в виде
# рекурсивной функции, которая выполняет ту же самую операцию.
# def traffic_sign(n):
#     while n > 0:
#         print(f'Не парковаться')
#         n = n - 1

def traffic_sign(n):
    if n > 0:
        print(f'Не парковаться')
        traffic_sign(n-1)
