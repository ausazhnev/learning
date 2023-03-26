import sqlite3


def main():
    # Присоединяемся к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Получаем курсор
    cur = conn.cursor()
    # Получаем от пользователя ProductId
    pid = int(input(f'введите ID изделия: '))
    # Получаем наименование и текущую цену для этого изделия
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   WHERE ProductId == ?''', (pid,))
    results = cur.fetchone()
    # Если ID изделия найден, то продолжить...
    if results is not None:
        # Напечатать текущую цену
        print(f'Текущая цена для: {results[0]}: ${results[1]:.2f}')
        # Получить новую цену
        new_price = float(input(f'Введите новую цену: '))
        # Обновить цену в таблице
        cur.execute('''UPDATE Products SET RetailPrice = ? WHERE ProductId == ?''',
                       (new_price, pid))
        # Зафиксировать изменения
        conn.commit()
        print(f'Цена была изменена.')
    else:
        # Сообщить об ошибке
        print(f'ID изделия {pid} не найден')
    # Закрыть соединение с базой
    conn.close()


if __name__ == '__main__':
    main()
