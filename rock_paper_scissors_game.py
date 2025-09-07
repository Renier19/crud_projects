import random

def rock_paper_scissor():
    choices = ["Rock", "Paper", "Scissors"]
    score_computer = 0
    score_player = 0
    
    while score_computer < 5 and score_player < 5:
        # Get player's choice
        player = input("\nPlease enter your choice (Rock/Paper/Scissors): ").capitalize()
        if player not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue
            
        # Get computer's choice
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        # Check for tie
        if player == computer:
            print("It's a tie!")
            continue
            
        # Check who wins
        if (player == "Scissors" and computer == "Rock") or \
           (player == "Paper" and computer == "Scissors") or \
           (player == "Rock" and computer == "Paper"):
            print("You lost this round!")
            score_computer += 1
        else:
            print("You won this round!")
            score_player += 1
            
        # Show current score
        print(f"\nScore - You: {score_player}, Computer: {score_computer}")
    
    # Show final result
    print("\nGame Over!")
    if score_player == 5:
        print("Congratulations! You won the game!")
    else:
        print("Computer wins the game!")

# Start the game
rock_paper_scissor()
