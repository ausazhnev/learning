import sqlite3

def main():
    # Присоединяемся к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Получить курсор
    cur = conn.cursor()
    # Выбрать все столбцы из каждой строки таблицы Products
    cur.execute('SELECT * FROM Products')
    # Извлечь все результаты
    results = cur.fetchall()
    # Показать результаты
    for row in results:
        print(f'{row[0]:2} {row[1]:35} {row[2]:5} {row[3]:6} {row[4]:5}')
    # Закрываем соединение с базой
    conn.close()


if __name__ == '__main__':
    main()
