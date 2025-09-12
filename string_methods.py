
def clean_name(name: str) -> str | None:
    """
    Validates and cleans a name.
    - Removes spaces
    - Capitalizes first letter
    - Returns None if invalid
    """
    name = name.strip()  # remove extra spaces
    if name.replace(" ", "").isalpha():
        return name.replace(" ", "").capitalize()
    return None


def get_name(label: str) -> str:
    """Keeps asking until a valid name is entered."""
    while True:
        user_input = input(f"Enter {label} name: ")
        cleaned = clean_name(user_input)
        if cleaned:
            print(f"original {user_input}: cleaned {cleaned}")
            return cleaned
        else:
            print(f"{label.upper()} NAME: LETTERS ONLY!")


# Main program
while True:
    first_name = get_name("First")
    last_name = get_name("Last")

    print(f"\n✅ Final cleaned full name: {first_name} {last_name}\n")

    

