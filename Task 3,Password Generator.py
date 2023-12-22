import random

def generate_password(length=30):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(characters[random.randint(0, len(characters)-1)] for _ in range(length))
    return password

def main():
    print("\t\t\t Welcome To Password Generator")
    valid_input = False
    while not valid_input:
        user_input = input("Enter the desired password length: ")
        if user_input.isdigit() and int(user_input) > 0:
            password_length = int(user_input)
            valid_input = True
        else:
            print("Invalid input. Please enter a positive integer.")

    password = generate_password(password_length)
    print("Generated Password:", password)


main()

