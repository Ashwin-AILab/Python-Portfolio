print("===== Random Password Generator =====")

import random as r

while True:
    try:
        length = int(input("\nEnter the password length: "))
        print()

        if length <= 0:
            print("Password length must be greater than 0.")

        else:

            num = input("Include numbers? (y/n): ").lower()
            
            if num == 'y':
                print("Numbers will be included in the password.")
            else:
                print("Numbers will not be included in the password.")
            print()

            print("Symbols like ! @ # $ % & *")
            sym = input("Include symbols? (y/n): ").lower()
            
        
            if sym == 'y':
                print("Symbols will be included in the password.")
            else:
                print("Symbols will not be included in the password.")
            print()
            
            print("Uppercase letters like A B C D E F G")
            up = input("Include uppercase letters? (y/n): ").lower()
            print()

            if up == 'y':
                print("Uppercase letters will be included in the password.")
            else:
                print("Uppercase letters will not be included in the password.")
            print()
            
            chars = 'abcdefghijklmnopqrstuvwxyz'
            
            if num == 'y':
                chars += '0123456789'

            if sym == 'y':
                chars += '!@#$%&*'

            if up == 'y':
                chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            print()
            gen = r.choices(chars, k=length)

            password = ''.join(gen)

            print("\nGenerated Password:", password)
            print()

            again = input("\nDo you want to generate another password? (y/n): ").lower()
            print()
            if again != 'y':
                print("\nThank you for using Random Password Generator!")
                break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        print()