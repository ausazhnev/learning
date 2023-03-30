# 1. Напишите SQL-инструкцию SELECT, которая выводит все столбцы
# из каждой строки в таблице Stock
cur.execute('SELECT * FROM Stock')

# 2. Напишите SQL-инструкцию SELECT, которая выводит все столбец
# TradingSymbol из каждой строки в таблице Stock
cur.execute('SELECT TradingSymbol FROM Stock')

# 3. Напишите SQL-инструкцию SELECT, которая выводит все столбец
# TradingSymbol и NumShares из каждой строки в таблице Stock
cur.execute('SELECT TradingSymbol, NumShares FROM Stock')

# 4. Напишите SQL-инструкцию SELECT, которая выводит все столбец
# TradingSymbol только из тех строк, в которых значение PurchasePrice превышает 25.00
cur.execute('SELECT TradingSymbol FROM Stock WHERE PurchasePrice > 25')

# 5. Напишите SQL-инструкцию SELECT, которая выводит все столбцы
# из строк в которых TradingSymbol начинается с "SU"
cur.execute('SELECT * FROM Stock WHERE TradingSymbol LIKE "SU%"')

# 6. Напишите SQL-инструкцию SELECT, которая вернет столбец TradingSymbol только из тех строк,
# в которых SellingPrice больше, чем PurchasePrice, а NumShares больше 100.
cur.execute('''SELECT TradingSymbol FROM Stock 
                                    WHERE 
                                        SellingPrice > TradingSymbol AND
                                        NumShares > 100''')

# 6. Напишите SQL-инструкцию SELECT, которая вернет столбец TradingSymbol и столбец NumShares
# только из тех строк, в которых SellingPrice больше PurchasePrice, а NumShares превышает 100.
# Результат должен быть отсортирован по столбцу NumShares порядке возрастания.
cur.execute('''SELECT TradingSymbol, NumShares FROM Stock
                                            WHERE
                                                SellingPrice > PurchasePrice AND 
                                                NumShares > 100 
                                            ORDER BY
                                                NumShares DESC''')

# 7. Напишите SQL-инструкцию SELECT, которая вернет столбец TradingSymbol и столбец NumShares
# только из тех строк в которых SellingPrice больше PurchasePrice, в NumShares превышает 100.
# Результаты должны быть отсортированы по столбцу NumShares в порядке возрастания.
cur.execute('''SELECT TradingSymbol, NumShares FROM Stock
                                            WHERE
                                                SellingPrice > PurchasePrice AND 
                                                NumShares > 100 
                                            ORDER BY
                                                NumShares''')

# 8. Напишите SQL-инструкцию, которая вносит новую строку в таблицу Stock. Строка должна иметь
# следующие значения столбцов:
# TradingSymbol: XYZ
# CompanyName: Компания XYZ
# NumShares: 150
# PurchasePrice: 12.55
# SellingPrice: 22.47
cur.execute('''INSERT INTO Stock 
                        (TradingSymbol, CompanyName, NumShares, PurchasePrice, SellingPrice)
                      VALUES
                        ("XYZ", "Компания XYZ", 150, 12.55, 22.47)''')

# 9. Напишите SQL-инструкцию, которая исполнит следующее: для каждой строки в таблице Stock, если
# столбец TradingSymbol имеет значение "XYZ", изменить это значение на "ABC"
cur.execute('''UPDATE Stock SET TradingSymbol = "ABC"
                            WHERE TradingSymbol == "XYZ"''')

# 10. Напишите SQL-инструкцию, которая удалит строки в таблице Stock, в которых число акций
# меньше 10.
cur.execute('''DELETE FROM Stock WHERE NumShares < 10''')

# 11. Напишите SQL-инструкцию, которая создаст таблицу Stock если она не существует.
cur.execute('''CREATE TABLE  IF NOT EXISTS Stock (TradingSymbol TEXT, 
                                                  CompanyName TEXT,
                                                  NumShares INTEGER,
                                                  PurchasePrice REAL,
                                                  SellingPrice REAL)''')

# 12. Напишите SQL-инструкцию, которая удалит таблицу Stock если она существует.
cur.execute('''DROP TABLE Stock IF EXISTS''')