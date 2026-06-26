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
def view_students():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Math: {student[2]}")
            print(f"Science: {student[3]}")
            print(f"English: {student[4]}")
            print("-" * 30)
    conn.close()
    print("Students views succesfully")
def search_student():
    conn=connect()
    cursor=conn.cursor()
    student_id=int(input("Enter student ID to search: "))
    cursor.execute("SELECT * FROM students where id = ?",(student_id,))
    student=cursor.fetchone()
    if student:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Math: {student[2]}")
        print(f"Science: {student[3]}")
        print(f"English: {student[4]}")
    else:
        print("Student not found")
    
    conn.close()



    
    