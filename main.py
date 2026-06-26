from database import (create_table, add_student, view_students,
                      search_student, update_student, delete_student)
from menu import display_menu

if __name__ == "__main__":
    create_table()

    while True:
        choice = display_menu()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
