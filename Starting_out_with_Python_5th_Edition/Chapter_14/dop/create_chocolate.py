# Создадим базу данных chocolate и наполним ее данными
# для проработки листингов из теоретической части

import sqlite3


def main():
    conn = sqlite3.connect('../db/chocolate.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Products (ProductId INTEGER PRIMARY KEY NOT NULL,
                                          Description TEXT,
                                          UnitCost REAL,
                                          RetailPrice REAL,
                                          UnionOnHand INTEGER)''')
    cur.execute('''INSERT INTO Products (Description, UnitCost, RetailPrice, UnionOnHand)
                                         VALUES ('Плитка темного шоколада', 2.99, 5.99, 197),
                                         ('Плитка средняя темного шоколада', 2.99, 5.99, 406),
                                         ('Плитка молочного шоколада', 2.99, 5.99, 266),
                                         ('Шоколадные трюфели', 5.99, 11.99, 398),
                                         ('Плитка шоколада с карамелью', 3.99, 6.99, 272),
                                         ('Плитка шоколада с малиной', 3.99, 6.99, 363),
                                         ('Плитка шоколада с кешью', 4.99, 9.99, 325),
                                         ('Смесь горячего шоколада', 5.99, 12.99, 222),
                                         ('Стружка из полусладкого шоколада', 1.99, 3.99, 163),
                                         ('Стружка из белого шоколада', 1.99, 3.99, 293)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
