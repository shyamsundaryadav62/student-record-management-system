students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        students.append([roll, name, branch])
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent Records:")
        for s in students:
            print("Roll No:", s[0], "| Name:", s[1], "| Branch:", s[2])

    elif choice == "3":
        roll = input("Enter Roll No to search: ")
        found = False
        for s in students:
            if s[0] == roll:
                print("Found -> Roll No:", s[0], "| Name:", s[1], "| Branch:", s[2])
                found = True
                break
        if not found:
            print("Student not found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")