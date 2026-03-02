import secrets
import string


def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = ""
    password = []

    if use_letters:
        characters += string.ascii_letters
        password.append(secrets.choice(string.ascii_letters))

    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        return "Error: You must select at least one character type."

    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    print("=== Secure Password Generator ===")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)

    print("\nGenerated Secure Password:")
    print(password)


if __name__ == "__main__":
    main()
