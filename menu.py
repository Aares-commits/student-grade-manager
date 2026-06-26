def display_menu():
    """Display the main menu and return user's choice."""
    print("\n" + "="*40)
    print("    STUDENT GRADE MANAGER")
    print("="*40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("="*40)
    
    while True:
        choice = input("Enter your choice (1-6): ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")
