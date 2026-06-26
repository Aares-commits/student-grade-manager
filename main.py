import sqlite3
def connect():
    conn = sqlite3.connect("grades.db")
    return conn
def create_table():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(id integer primary key autoincrement, name text, math integer,
                    science integer, english integer)""")
    conn.commit()
    conn.close()
    print("Table ready!")

create_table()
