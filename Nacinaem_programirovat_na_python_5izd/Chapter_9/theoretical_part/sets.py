# операции со множествами. имена студентов баскетбольной и бейсбольной команды

# set operations. names of basketball and baseball students

baseball = set(['Джони', 'Кармкн', 'Аида', 'Алисия'])
basketball = set(['Ева', 'Кармен', 'Алисия', 'Сара'])

# Отобразить элементы множества basketball
print(f'Эти студенты состоят в бейсбольной команде:')
for name in basketball:
    print(name)

# Отобразить элементы множества baseball
print()
print(f'Эти студенты состоят в баскетбольной команде:')
for name in basketball:
    print(name)

# Продемонстрировать пересечение
print()
print(f'Эти стденты играют в баскетбол и бейсбол:')     # отображаем только элементы которые
for name in basketball.intersection(baseball):          # содаржатся в обоих множествах
# for name in basketball & baseball: -альтернатиыный способ записи
    print(name)

# Продемонстрировать объединение
print()
print(f'Эти студенты играют в одну или обе спортивные игры:')    # отображат элементы обоих множеств
for name in basketball.union(baseball):
# for name in basketball | basketball: -альтернатиыный способ записи
    print(name)

# Продемонстрировать разность между бейсболом и баскетболом
print()
print(f'Эти студенты играют в баскетбол, но не играют в бейсбол:')  # Отображает элементы basketball
for name in basketball.difference(baseball):                    # которые не встречаются в baseball
# for name in basketball - baseball: -альтернатиыный способ записи
    print(name)

# Продемонстрировать разность между баскетболом и бейсболом
print()
print(f'Эти студенты играют в бейсбол, но не играют в баскетбол:')  # Отображает элементы baseball
for name in baseball.difference(basketball):                    # которые не встречаются в basketball
# for name in baseball - basketball: -альтернатиыный способ записи
    print(name)

# Продемонстрировать симантическую разность
print()
print(f'Эти студенты играют в одну из спортивных игр, но не в обе:')    # Отображается список элементов
for name in basketball.symmetric_difference(baseball):                  # которые содержатся только
# for name in basketball ^ baseball: -альтернатиыный способ записи      # в одном из множеств
    print(name)