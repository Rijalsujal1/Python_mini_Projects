import string
import secrets


def generate_password(min_length, include_numbers=True, include_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if include_numbers:
        characters += digits
    if include_special:
        characters += special

    # Ensure password meets criteria
    while True:
        password = "".join(secrets.choice(characters) for _ in range(min_length))

        if include_numbers and not any(char in digits for char in password):
            continue
        if include_special and not any(char in special for char in password):
            continue
        return password


def get_boolean_input(prompt):
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")


def main():
    try:
        min_length = int(input("Enter the minimum password length: "))
        if min_length < 1:
            raise ValueError("Length must be at least 1.")
    except ValueError as e:
        print("Invalid input:", e)
        return

    include_numbers = get_boolean_input("Do you want to include numbers?")
    include_special = get_boolean_input("Do you want to include special characters?")

    password = generate_password(min_length, include_numbers, include_special)
    print(f"\n🔐 Your generated password is: {password}")

    # Optional: Copy to clipboard (if pyperclip is installed)
    try:
        import pyperclip

        pyperclip.copy(password)
        print("✅ Password has been copied to the clipboard.")
    except ImportError:
        print("ℹ️ Install 'pyperclip' module to enable clipboard copying.")


if __name__ == "__main__":
    main()
