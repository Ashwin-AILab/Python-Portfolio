print("""====================================
      PYTHON BANKING SYSTEM
====================================""")

import random as r

accounts = {}

while True:
    print("""1. Create Account
2. Login
3. Exit""")
    print()

    try:
        choice = int(input("Enter your choice = "))

        if choice == 1:

            name = input("Enter Full Name: ").capitalize()

            while True:
                pin = input("Create 4-digit PIN: ")

                if len(pin) == 4 and pin.isdigit():
                    break

                print("PIN length should be 4")

            while True:
                dep = int(input("Enter Initial Deposit: "))

                if dep > 0:
                    break

                print("Wrong Deposit Amount")

            acc_no = str(r.randint(10000, 99999))

            print()

            print("Your Account Number is:", acc_no)

            accounts[acc_no] = {
                "Account Holder Name": name,
                "PIN": pin,
                "Balance": dep
            }

        elif choice == 2:
            print("============= LOGIN =============")

            ent_acc_no = input("Enter Account Number: ")
            ent_pin = input("Enter PIN: ")

            if ent_acc_no in accounts and accounts[ent_acc_no]["PIN"] == ent_pin:
                print("Login Successful")

                while True:
                    print("""================================
        BANK MENU
================================

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Account Details
6. Logout""")

                    try:
                        select = int(input("Enter Choice: "))

                        if select == 1:
                            print("Your Current Balance is: ₹", accounts[ent_acc_no]["Balance"])
                            print()

                        elif select == 2:
                            deposit = int(input("Enter Amount to Deposit: "))

                            if deposit > 0:

                                accounts[ent_acc_no]["Balance"] += deposit

                                print("₹", deposit, "Deposited Successfully!")
                                print("Updated Balance: ₹", accounts[ent_acc_no]["Balance"])

                            else:
                                print("Invalid Input !!")

                        elif select == 3:
                            withdraw = int(input("Enter Amount to Withdraw: "))

                            if withdraw > accounts[ent_acc_no]["Balance"]:
                                print("Insufficient Balance!")

                            elif withdraw > 0:

                                accounts[ent_acc_no]["Balance"] -= withdraw

                                print("₹", withdraw, "Withdrawn Successfully!")
                                print("Updated Balance: ₹", accounts[ent_acc_no]["Balance"])

                            else:
                                print("Invalid Input !!")

                        elif select == 4:

                            rec = input("Enter Receiver Account Number: ")

                            if rec in accounts:

                                if rec == ent_acc_no:
                                    print("Cannot Transfer To Same Account")

                                else:
                                    amt = int(input("Enter Amount: "))

                                    if amt > 0 and amt <= accounts[ent_acc_no]["Balance"]:

                                        accounts[ent_acc_no]["Balance"] -= amt
                                        accounts[rec]["Balance"] += amt

                                        print("Transfer Successful!")

                                    else:
                                        print("Invalid Amount !!")

                            else:
                                print("Invalid Receiver's Account Details !!")

                        elif select == 5:
                            print("========== ACCOUNT DETAILS ==========")
                            print("Name:", accounts[ent_acc_no]["Account Holder Name"])
                            print("Account Number:", ent_acc_no)
                            print("Balance: ₹", accounts[ent_acc_no]["Balance"])

                        elif select == 6:
                            print("Logged Out Successfully!")
                            break

                        else:
                            print("Invalid Input !!")

                    except ValueError:
                        print("Invalid Input !!")

            else:
                print("Invalid Login Information")

        elif choice == 3:
            print("Thanks for using Bank Management System")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid input")