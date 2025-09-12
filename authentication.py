
while True:
    try:
        user_email = str(input("Enter your email: "))
        if not user_email.endswith("@gmail.com"):
            print("INVALID USER INPUT")

        elif user_email[0].isupper() or " " in user_email:
            print("INVALID USER INPUT")

        else:
            print("CONGRATULATIONS YOU'RE IN!!")

        break





    except ValueError:
        print("Please enter a valid number")