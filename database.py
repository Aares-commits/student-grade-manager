import sqlite3

def connect():
    try:
        conn = sqlite3.connect("grades.db")
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

def create_table():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                        id integer primary key autoincrement,
                        name text,
                        math integer,
                        science integer,
                        english integer)""")
        conn.commit()
        print("Table ready!")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

def add_student():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))

        for mark in [math, science, english]:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

        cursor.execute("INSERT INTO students (name, math, science, english) VALUES (?, ?, ?, ?)",
                       (name, math, science, english))
        conn.commit()
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Marks must be numbers.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()

def view_students():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
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
    except sqlite3.Error as e:
        print(f"Error viewing students: {e}")
    finally:
        conn.close()

def search_student():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        student_id = int(input("Enter student ID to search: "))
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        if student:
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Math: {student[2]}")
            print(f"Science: {student[3]}")
            print(f"English: {student[4]}")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input! ID must be a number.")
    except sqlite3.Error as e:
        print(f"Error searching student: {e}")
    finally:
        conn.close()

def update_student():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        student_id = int(input("Enter student ID to update: "))
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        print("Leave blank if you don't want to change.")
        new_name = input(f"Enter new name ({student[1]}): ").strip()
        new_math = input(f"Enter new Math marks ({student[2]}): ")
        new_science = input(f"Enter new Science marks ({student[3]}): ")
        new_english = input(f"Enter new English marks ({student[4]}): ")

        new_name = new_name if new_name else student[1]
        new_math = int(new_math) if new_math else student[2]
        new_science = int(new_science) if new_science else student[3]
        new_english = int(new_english) if new_english else student[4]

        for mark in [new_math, new_science, new_english]:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

        cursor.execute("""UPDATE students
                          SET name = ?, math = ?, science = ?, english = ?
                          WHERE id = ?""",
                       (new_name, new_math, new_science, new_english, student_id))
        conn.commit()
        print("Student updated successfully!")
    except ValueError:
        print("Invalid input! Marks must be numbers.")
    except sqlite3.Error as e:
        print(f"Error updating student: {e}")
    finally:
        conn.close()

def delete_student():
    conn = connect()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        student_id = int(input("Enter student ID to delete: "))
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        print(f"Deleting student: {student[1]} (ID: {student[0]})")
        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Invalid input! ID must be a number.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_table()