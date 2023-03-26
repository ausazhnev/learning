import sqlite3


def main():
    # Присоединяемся к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Получить курсор
    cur = conn.cursor()
    # Получить описание и розничные цены
    cur.execute('SELECT Description, RetailPrice FROM Products')
    # Извлечь результаты инструкции SELECT
    results = cur.fetchall()
    # Перебрать строки и показать результаты
    for row in results:
        print(f'{row[0]:35} {row[1]:5}')
    # Закрыть соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
