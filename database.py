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
    print("Students viewed succesfully")
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
def update_student():
    conn=connect()
    cursor=conn.cursor()
    student_id=int(input("Enter student ID to update:"))
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student=cursor.fetchone()
    if not student:
        print("Student not found.")
        conn.close()
        return 

    print("Leave blank if you don't want to change")
    new_name=input(f"Enter new name({student[1]}): ")
    new_math = input(f"Enter new Math marks ({student[2]}): ")
    new_science = input(f"Enter new Science marks ({student[3]}): ")
    new_english = input(f"Enter new English marks ({student[4]}): ")
    #keep old values if user presses enter
    new_name = new_name if new_name else student[1]
    new_math = int(new_math) if new_math else student[2]
    new_science = int(new_science) if new_science else student[3]
    new_english = int(new_english) if new_english else student[4]

    cursor.execute(""" 
                   UPDATE students
                   SET name = ?, math = ?, science = ?, english = ?
                   WHERE id = ?
                   """,(new_name, new_math, new_science, new_english, student_id))
    
    conn.commit()
    conn.close()
    print("Student updated successfully!")
def delete_student():
    conn = connect()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    print(f"Deleting student: {student[1]} (ID: {student[0]})")
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

    conn.close()

if __name__ == "__main__":
    create_table()
