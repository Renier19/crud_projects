import random
import string

def generate_random_string(length, use_letters=True, use_digits=True, use_punctuation=True):
    # Initialize an empty string for our character set
    characters = ''
    
    # Add selected character types to our set
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
        
    # If no character types were selected, use letters as default
    if not characters:
        characters = string.ascii_letters
        
    # Generate and return the random string
    return ''.join(random.choices(characters, k=length))

def main():
    print("Welcome to Random String Generator!")
    
    # Get the desired length
    while True:
        try:
            length = int(input("\nEnter the length of the random string: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get character type preferences
    print("\nWhat types of characters would you like to include?")
    use_letters = input("Include letters? (yes/no): ").lower().startswith('y')
    use_digits = input("Include numbers? (yes/no): ").lower().startswith('y')
    use_punctuation = input("Include special characters? (yes/no): ").lower().startswith('y')
    
    # Generate and display the random string
    result = generate_random_string(length, use_letters, use_digits, use_punctuation)
    
    print("\nYour random string is:")
    print(result)
    
    # Show what characters were used
    print("\nCharacter types used:")
    print("Letters:", "Yes" if use_letters else "No")
    print("Numbers:", "Yes" if use_digits else "No")
    print("Special characters:", "Yes" if use_punctuation else "No")

if __name__ == "__main__":
    main()
