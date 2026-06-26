from database import connect

def insert_sample_data():
    conn = connect()
    cursor = conn.cursor()

    students = [
        ("Ravi Kumar", 85, 90, 78),
        ("Priya Singh", 92, 88, 95),
        ("Arjun Das", 70, 65, 80),
        ("Sneha Rao", 55, 60, 58),
        ("Karthik M", 98, 95, 99)
    ]

    cursor.executemany("""
        INSERT INTO students (name, math, science, english)
        VALUES (?, ?, ?, ?)
    """, students)

    conn.commit()
    conn.close()
    print("Sample data added!")

insert_sample_data()