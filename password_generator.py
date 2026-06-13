import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    # Build the character pool based on user choices
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected!")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("Generated password:", password)
