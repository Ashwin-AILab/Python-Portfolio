print("Welcome to Student Result Management System")

students = []

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    try:
        choice = int(input("Enter Choice = "))

        if choice == 1:
            name = input("Enter Student's Name = ")

            eng = float(input("Enter Marks of English = "))
            phy = float(input("Enter Marks of Physics = "))
            chem = float(input("Enter Marks of Chemistry = "))
            maths = float(input("Enter Marks of Mathematics = "))
            ped = float(input("Enter Marks of Physical Education = "))

            total_marks = eng + phy + chem + maths + ped
            per = total_marks / 5

            if per >= 90:
                grade = "A+"
            elif per >= 75:
                grade = "A"
            elif per >= 60:
                grade = "B"
            elif per >= 40:
                grade = "C"
            else:
                grade = "Fail"

            student = {
                "name": name,
                "total_marks": total_marks,
                "percentage": per,
                "grade": grade
            }

            students.append(student)

            print("\nStudent Added Successfully!")

        elif choice == 2:
            if len(students) == 0:
                print("\nNo students found!")
            else:
                for s in students:
                    print("\n----------------------")
                    print(f"Name: {s['name']}")
                    print(f"Total: {s['total_marks']}")
                    print(f"Percentage: {s['percentage']:.2f}")
                    print(f"Grade: {s['grade']}")

        elif choice == 3:
            search = input("Enter student name to search: ")

            found = False

            for s in students:
                if s["name"].lower() == search.lower():
                    print("\n--- Student Found ---")
                    print(f"Name: {s['name']}")
                    print(f"Total: {s['total_marks']}")
                    print(f"Percentage: {s['percentage']:.2f}")
                    print(f"Grade: {s['grade']}")
                    found = True
                    break

            if not found:
                print("Student not found!")

        elif choice == 4:
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")