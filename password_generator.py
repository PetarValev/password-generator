import random
import string
import argparse

def generate_passwords(count=1, length=16, characters=string.ascii_letters + string.digits + string.punctuation):
    passwords = [''.join(random.choice(characters) for _ in range(length)) for _ in range(count)]
    return passwords

def main():
    parser = argparse.ArgumentParser(
        description="Generate secure and random passwords with ease!",
        epilog="Enjoy secure password generation! 😎",
    )

    parser.add_argument("-c", "--count", type=int, default=1, help="Specify the number of passwords to generate. Default is 1.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Specify the length of each password. Default is 16 characters.")

    args = parser.parse_args()

    passwords = generate_passwords(count=args.count, length=args.length)

    for i, password in enumerate(passwords, 1):
        print(f"\nPassword {i}: {password}")


if __name__ == "__main__":
    main()
