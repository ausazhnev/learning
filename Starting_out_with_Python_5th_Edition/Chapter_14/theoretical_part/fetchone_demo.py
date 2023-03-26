import sqlite3


def main():
    # Подсоединяемся к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Подучаем курсор
    cur = conn.cursor()
    # Выбрать все столбцы из каждой строки таблицы Products
    cur.execute('SELECT Description, RetailPrice FROM Products')
    # Извлечь первую строку результатов
    row = cur.fetchone()
    while row is not None:
        # Показать строку
        print(f'{row[0]:35} {row[1]:5}')
        # Извлечь следующую строку
        row = cur.fetchone()
    # Закрываем соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
