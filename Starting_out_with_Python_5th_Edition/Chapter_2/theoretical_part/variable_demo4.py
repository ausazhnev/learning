# Эта программа показывает повторное присвоение значения переменной.
# Присвоить значение переменной roubles
roubles = 2.75
print('У меня на счете', roubles, 'рублей')
# Вывод через f-строку
print(f'У меня на счете {roubles} рублей')

# Повторно присвоить значение переменной roubles,
# чтобы она ссылалась на другое значение.
roubles = 99.95
print('А теперь там', roubles, 'рублей')
# Вывод через f-строку
print(f'А теперь там {roubles} рублей')
