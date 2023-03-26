import sqlite3

def main():
    conn = sqlite3.connect('../db/contacts.db')
    cur = conn.cursor()

    # Здесь вставить код для выполнения операций с базой данных.

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
