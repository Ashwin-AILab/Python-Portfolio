print("===== Welcome to Library Management System =====")

library = []

while True:

    print("""\n1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit""")

    print()

    try:
        a = int(input("Enter your choice = "))
        print()

        if a == 1:

            bn = input("Enter Book Name = ")

            if len(bn) == 0:
                print("Book name can't be empty")
                continue

            print()

            an = input("Enter Author Name = ")

            if len(an) == 0:
                print("Author name can't be empty")
                continue

            print()

            qty = int(input("Enter Book Quantity = "))

            if qty <= 0:
                print("Invalid Book Quantity")
                continue

            print()

            dic = {
                "Book name": bn,
                "Author name": an,
                "Quantity": qty
            }

            library.append(dic)

            print("Book Added Successfully!")
            print()

        elif a == 2:

            if len(library) == 0:
                print("No books found in library.")

            else:
                for book in library:
                    print("------------------------")
                    print(f"Book Name : {book['Book name']}")
                    print(f"Author    : {book['Author name']}")
                    print(f"Quantity  : {book['Quantity']}")
                    print("------------------------")

        elif a == 3:

            search = input("Enter Book Name to Search = ")
            print()

            found = False

            for book in library:
                if search.lower() == book["Book name"].lower():
                    print("----- Book Found -----")
                    print(f"Book Name : {book['Book name']}")
                    print(f"Author    : {book['Author name']}")
                    print(f"Quantity  : {book['Quantity']}")
                    print("------------------------")
                    found = True

            if not found:
                print("Book Not Found!")

        elif a == 4:

            issue = input("Enter Book Name to Issue = ")
            print()

            found = False

            for book in library:
                if issue.lower().strip() == book["Book name"].lower().strip():
                    found = True

                    if book["Quantity"] > 0:
                        book["Quantity"] -= 1
                        print("Book Issued Successfully!")
                        print("Remaining Quantity =", book["Quantity"])
                    else:
                        print("Book Out of Stock!")

            if not found:
                print("Book Not Found!")

        elif a == 5:

            ret = input("Enter Book Name to Return = ")
            print()

            found = False

            for book in library:
                if ret.lower().strip() == book["Book name"].lower().strip():
                    book["Quantity"] += 1
                    print("Book Returned Successfully!")
                    print("Updated Quantity =", book["Quantity"])
                    found = True

            if not found:
                print("Book Not Found!")

        elif a == 6:

            delete = input("Enter Book Name to Delete = ")
            print()

            found = False

            for book in library:
                if delete.lower().strip() == book["Book name"].lower().strip():
                    library.remove(book)
                    print("Book Deleted Successfully!")
                    found = True
                    break

            if not found:
                print("Book Not Found!")

        elif a == 7:
            print("Thank You for Using Library Management System!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Invalid Input")