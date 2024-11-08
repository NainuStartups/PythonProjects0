import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    # List of valid choices
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get the player's choice
        player_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

        # Check if the input is valid
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
