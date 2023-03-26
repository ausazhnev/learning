import sqlite3


def main():
    # Подсоединение к базе данных
    conn = sqlite3.connect('../db/chocolate.db')
    # Получить курсор
    cur = conn.cursor()
    # Получить от пользователя ID изделия
    pid = int(input(f'Введите ID изделия для его удаления: '))
    # Получить описание этого изделия.
    cur.execute('''SELECT Description FROM Products 
                   WHERE ProductId == ?''', (pid,))
    results = cur.fetchone()
    # Если ID изделия найден, то продолжить...
    if results is not None:
        # Подтвердить желание удалить изделие.
        sure = input(f'Вы уверены, что хотите удалить {results[0]}? (д/н)')
        # Если да, то удалить изделие.
        if sure.lower() == 'д':
            cur.execute('''DELETE FROM Products 
                           WHERE ProductId == ?''', (pid,))
            # Зафиксировать изменения
            conn.commit()
            print(f'Изделие успешно удалено.')
    else:
        # Сообщить об ошибке
        print(f'ID изделия {pid} не найден.')
    # Закрыть соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()
