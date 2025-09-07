import random

# Create a list of choices
choices = ["rock", "paper", "scissors"]

# Get computer's choice
computer = random.choice(choices)

# Example of how it works
print("Computer chose:", computer)

# Full game example
def play_game():
    print("\nLet's play Rock, Paper, Scissors!")
    print("Enter your choice (rock/paper/scissors):")
    
    # Get player's choice
    player = input().lower()
    
    # Get computer's choice
    computer = random.choice(choices)
    
    # Show both choices
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    
    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock crushes scissors")
        else:
            print("You lose! Paper covers rock")
    elif player == "paper":
        if computer == "rock":
            print("You win! Paper covers rock")
        else:
            print("You lose! Scissors cuts paper")
    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors cuts paper")
        else:
            print("You lose! Rock crushes scissors")
    else:
        print("Invalid choice! Please enter rock, paper, or scissors")

# Play the game
play_game()
