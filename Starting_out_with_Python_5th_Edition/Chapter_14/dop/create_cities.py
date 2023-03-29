# Создаем базу данных cities и наполняем ее данными
# для выполнения задания по программированию 14_1

import sqlite3


def main():
    conn = None
    try:
        conn = sqlite3.connect('../db/cities.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Cities (CityID INTEGER PRIMARY KEY NOT NULL, 
                                                          CityName TEXT,
                                                          Population INTEGER)''')

        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Москва", 13098000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Санкт-Петербург", 5598000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Новосибирск", 1634000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Екатеринбург", 1544000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Казань", 1309000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Нижний Новгород", 1226000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Челябинск", 1190000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Красноярск", 1188000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Самара", 1173000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Уфа", 1145000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Ростов-на-Дону", 1142000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Омск", 1126000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Краснодар", 1099000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Воронеж", 1058000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Пермь", 1034000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Волгоград", 1028000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Саратов", 901000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Тюмень", 847000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Барнаул", 631000)''')
        cur.execute('''INSERT INTO Cities (CityName, Population)
                                           VALUES ("Ижевск", 623000)''')
        conn.commit()
        print(f'База данных создана и наполнена данными')
    except sqlite3.Error as err:
        print(f'Ошибка базы данных {err}')
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
