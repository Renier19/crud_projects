import random

def word_guessing_game():
    # List of words to guess from
    words = ["python", "programming", "computer", "algorithm", "database", 
             "network", "developer", "internet", "software", "keyboard"]
    
    # Select a random word
    word = random.choice(words)
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # letters guessed by user
    
    lives = 6  # number of tries
    
    # Getting user input until the word is guessed or lives run out
    while len(word_letters) > 0 and lives > 0:
        # Show used letters
        print("\nYou have used these letters:", " ".join(used_letters))
        print(f"You have {lives} lives left.")
        
        # Show the word with dashes for unguessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_list))
        
        # Get user input
        user_letter = input("\nGuess a letter: ").lower()
        
        # Check if the letter is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # add to used letters
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # remove from letters to be guessed
                print("Good guess!")
            else:
                lives = lives - 1
                print("Wrong guess!")
                
        elif user_letter in used_letters:
            print("You already used that letter. Try another one.")
            
        else:
            print("Invalid character. Please enter a letter.")
    
    # Game ended - check if won or lost
    if lives == 0:
        print(f"\nSorry, you died. The word was {word}")
    else:
        print(f"\nCongratulations! You guessed the word {word}!!")

# Start the game
print("Welcome to Word Guessing Game!")
word_guessing_game()

# Ask if player wants to play again
while input("\nDo you want to play again? (yes/no): ").lower().startswith('y'):
    word_guessing_game()
