import sqlite3


def main():
    # Подключиться к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Получить курсор
    cur = conn.cursor()
    # Получить от пользователя минимальную цену
    min_price = float(input(f'Введите минимальную цену: '))
    # Отправить инструкцию SELECT в СУБД
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   WHERE RetailPrice >= ?''',
                   (min_price,))
    # Извлечь результаты инструкции SELECT
    results = cur.fetchall()
    if len(results) > 0:
        # Показать результаты
        print(f'Вот результаты:')
        print()
        print(f'Описание                           |  Цена')
        print(f'------------------------------------------')
        for row in results:
            print(f'{row[0]:35}| {row[1]:5}')
    else:
        print(f'Не одного изделия не найдено.')
    # Закрываем соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
