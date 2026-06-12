import random as r


def show_rules():
    print("\nRules :-")
    print("1. You have to guess a number between 1 and 10 (both inclusive).")
    print("2. You will have three attempts.")
    print("3. If your guess is correct, you win and the game ends.")
    print("4. If you can't guess the number in three attempts, you lose.")
    print("5. After the last attempt, you will see the correct number.\n")


def play_game():
    num = r.randint(1, 10)
    attempt = 1

    while attempt <= 3:

        try:
            guess = int(input("Guess a Number = "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.\n")
                continue

            if num == guess:
                print("\n Congratulations! You Won \n")
                break

            else:
                attempts_left = 3 - attempt
                print(f"Wrong Guess! Attempts left: {attempts_left}\n")
                attempt += 1

        except ValueError:
            print("Invalid Input! Please enter a valid number.\n")

    if attempt > 3:
        print(f" Game Over! The correct number was {num}\n")


print("\nWelcome")
print("\n===== Random Number Guess Game =====\n")

while True:

    print("Type 1 for Rules")
    print("Type 2 to Play")
    print("Type 3 to Exit")

    try:
        choice = int(input("= "))
        print()

        match choice:

            case 1:
                show_rules()

            case 2:
                play_game()

                # Replay option
                while True:

                    try:
                        replay = int(input("Do you want to play again?\n1. Yes\n2. No\n= "))
                        print()

                        if replay == 1:
                            play_game()

                        elif replay == 2:
                            print("Thanks for playing!")
                            exit()

                        else:
                            print("Please enter 1 or 2.\n")

                    except ValueError:
                        print("Invalid Input! Please enter a number.\n")

            case 3:
                print("Game Exited by User")
                break

            case _:
                print("Error! Please choose a valid option.\n")

    except ValueError:
        print("Invalid Input! Please enter a number.\n")
