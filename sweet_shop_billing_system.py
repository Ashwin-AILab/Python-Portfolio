print("\n========== Welcome to Shiva Sweet Shop ==========\n")

# Dictionary for sweets menu
sweets = {
    1: ("Gulab Jamun", 900),
    2: ("Rasgulla", 750),
    3: ("Jalebi", 300),
    4: ("Kaju Katli", 840),
    5: ("Barfi (Plain)", 540),
    6: ("Ladoo (Besan)", 400),
    7: ("Chandrakala", 120),
    8: ("Kalakand", 200),
    9: ("Peda", 240),
    10: ("Soan Papdi", 250),
    11: ("Carrot Halwa (Gajar ka Halwa)", 400),
    12: ("Rabri", 450),
    13: ("Moong Dal Halwa", 350),
    14: ("Mysore Pak", 450),
    15: ("Sandesh", 450)
}

print("Type 1 for Menu")
print("Type 2 to Exit\n")

try:
    a = int(input("Enter 1/2 = "))
    print()

    if a == 2:
        print("Hope to see you again!")

    elif a == 1:

        total_bill = 0

        while True:

            print("============== MENU ==============")

            for key, value in sweets.items():
                print(f"Type {key} for {value[0]} - Rs.{value[1]}/kg")

            print("Type 0 to Finish Billing")
            print()

            try:
                menu = int(input("Enter item number = "))

                if menu == 0:
                    break

                elif menu not in sweets:
                    print("Invalid Item Number!\n")
                    continue

                sweet_name, sweet_price = sweets[menu]

                print(f"\nSweet Name  : {sweet_name}")
                print(f"Sweet Price : Rs.{sweet_price} per kg\n")

                qty = float(input("Enter Quantity in kg = "))

                if qty <= 0:
                    print("Quantity must be greater than 0.\n")
                    continue

                item_bill = sweet_price * qty
                total_bill += item_bill

                print(f"\nQuantity    : {qty} kg")
                print(f"Item Bill   : Rs.{item_bill}\n")

                print("Item added successfully!\n")

            except ValueError:
                print("Invalid Input! Please enter valid numbers.\n")

        # GST Calculation
        gst = total_bill * 0.05
        final_bill = total_bill + gst

        # Final Receipt
        print("\n========== FINAL RECEIPT ==========")
        print(f"Bill Amount : Rs.{total_bill:.2f}")
        print(f"GST (5%)    : Rs.{gst:.2f}")
        print(f"Final Amount: Rs.{final_bill:.2f}")
        print("===================================\n")

        # Payment Section
        print("Choose Mode of Payment\n")
        print("""Type 1 for Cash Payment
Type 2 for UPI
Type 3 for Net Banking\n""")

        try:
            mode = int(input("Enter payment mode = "))
            print()

            match mode:
                case 1:
                    print("Your mode of payment is Cash")

                case 2:
                    print("Your mode of payment is UPI")
                    print("Please wait while we direct you to payment gateway")

                case 3:
                    print("Your mode of payment is Net Banking")
                    print("Please wait while we direct you to payment gateway")

                case _:
                    print("Invalid Payment Mode!")

        except ValueError:
            print("Invalid Input! Please enter a valid number.")

        print("\nThank You for shopping at Shiva Sweet Shop!")
        print("Hope to see you again!\n")

    else:
        print("Invalid Choice!")

except ValueError:
    print("Invalid Input! Please enter a valid number.")
