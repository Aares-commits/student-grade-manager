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

if __name__ == "__main__":
    create_table()
def add_student():
    conn=connect()
    cursor=conn.cursor()
    name=input("Enter student name: ")
    math=int(input("Enter Math marks: "))
    science=int(input("Enter Science marks: "))
    english=int(input("Enter English marks: "))
    cursor.execute("INSERT INTO students (name, math, science, english) VALUES (?, ?, ?, ?)", \
    (name, math, science, english))
    conn.commit()
    conn.close()
    print("Student added succesfully!")