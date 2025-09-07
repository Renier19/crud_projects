animals = [
    "cat", "dog", "bear", "lion", "wolf", "bird", "fish",
    "giraffe", "elephant", "penguin", "dolphin", "kangaroo",
    "zebra", "monkey", "turtle", "rabbit", "panda",
    "rhinoceros", "hippopotamus", "chimpanzee", "crocodile",
    "butterfly", "octopus", "gorilla", "hamster"
]

countries = [
    "spain", "china", "italy", "japan", "india",
    "germany", "mexico", "canada", "brazil", "france",
    "england", "russia", "egypt", "korea", "turkey",
    "australia", "argentina", "indonesia", "portugal",
    "switzerland", "netherlands", "philippines"
]

food = [
    "pizza", "pasta", "rice", "bread", "cake", "soup",
    "burrito", "pancake", "sausage", "chicken", "cookie",
    "sandwich", "noodles", "icecream", "muffin",
    "hamburger", "chocolate", "spaghetti", "pineapple",
    "strawberry", "blueberry", "watermelon"
]

sports = [
    "golf", "rugby", "tennis", "soccer",
    "baseball", "football", "cricket", "bowling",
    "hockey", "cycling", "boxing", "skating",
    "volleyball", "basketball", "gymnastics", "wrestling",
    "swimming", "badminton", "skateboard"
]

import random

guessed_letters = []
lives = 6

def get_category(category):
    if category == 1:
        word = random.choice(animals)
        return(word)
    elif category == 2:
        print("COUNTRIES")
        word = random.choice(countries)
        return(word)
    elif category == 3:
        word = random.choice(food)
        return(word)
    elif category == 4:
        word = random.choice(sports)
        return(word)

def check_letter(letter, word):
    if letter in word:
        print(f"{letter} is in the word")
        guessed_letters.append(letter)

    else:
        global lives
        lives -= 1
        print(f"{letter} is not in the word!")

    display = ""
    for char in word:
        if char in guessed_letters:
            display += char.upper() + " "
        else:
            display += "_ "
    print(f"Word: {display}")

def check_win(word):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True
    
def main():
    print("Welcome to Word guessing Game!")
    print("Please Choose a category:")
    print("[1] Animals")
    print("[2] Countries")
    print("[3] Food")
    print("[4] Sports")
    category = int(input("Please choose above"))
    random_word = get_category(category)

    while lives > 0:
        letter = input("Please enter a letter: ")
        check_letter(letter, random_word)

        if check_win(random_word):
            print(f"CONGRATULATIONS!!! your word was {random_word}")
            break

        print(f"You have {lives} lives left" )
        
    if lives == 0:
        print(f"Game over! your word was {random_word}")
    

    


main()
