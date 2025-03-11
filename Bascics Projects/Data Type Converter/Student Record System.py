###  Student Record System (DataTypes)

def student_records():
    students = {}
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            students[name] = grade
        elif choice == '2':
            for name, grade in students.items():
                print(f"{name}: {grade}")
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

student_records()