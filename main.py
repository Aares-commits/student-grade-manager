from database import create_table, add_student
from menu import display_menu
create_table()
while True:
    choice=display_menu()

    if choice =="1":
        add_student()
    elif choice == "2":
            from database import view_students
            view_students()
    elif choice == "3":
         from database import search_student
         search_student()
    elif choice == "4":
        from database import update_student
        update_student()
    elif choice == "5":
        from database import delete_student
        delete_student()  
    elif choice == "6":
        print("Goodbye!")
        break


