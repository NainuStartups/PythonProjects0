import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller!")

    while True:
        # Ask the user if they want to roll the dice
        input("Press Enter to roll the dice or type 'exit' to quit: ")

        # Roll the dice
        roll = roll_dice()
        
        # Show the result of the dice roll
        print(f"You rolled a {roll}!")

        # Ask if the user wants to roll again or quit
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the program
if __name__ == "__main__":
    main()
