import random
import string


def weak_password_generator(length):
    characters = string.ascii_lowercase
    password = "".join(random.choice(characters) for i in range(length))
    return password


def strong_password_generator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-"
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    return password


def select_password_generator():
    print("Welcome to the Passwords Generator ")
    print("\nPlease choose which kind of Password you would like to have:")
    print("1. Weak Password")
    print("2. Strong Password")
    choice = input("Your choice: ")
    if choice == "1":
        return weak_password_generator
    elif choice == "2":
        return strong_password_generator
    else:
        print("Wrong typo. Try again.")
        return None


def generate_password():
    global running
    running = True

    while running:
        password_generator = select_password_generator()
        if password_generator is not None:
            password = password_generator(8)
            print("Your password is:", password)
            file = open("password.txt", "a")
            file.write(password + "\n")
            file.close()
            repeat = input("Do you want to generate another password? (y/n): ")
            while repeat not in ["y", "n"]:
              print("Please enter y or n.")
              repeat = input("Do you want to generate another password? (y/n): ")
            if repeat == "n":
                running = False


if __name__ == "__main__":
    generate_password()
