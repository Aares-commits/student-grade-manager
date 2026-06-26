from database import create_table, add_student
from menu import display_menu
create_table()
while True:
    choice=display_menu()

    if choice =="1":
        add_student()
    elif choice == "6":
        print("Goodbye!")
        break


