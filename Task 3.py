# Task 3
import string
import random
complexity_level = ["easy", "medium", "hard"]

def password_generator(length, complexity):
    if complexity == "easy":
        characters = string.ascii_lowercase

    elif complexity == "medium":
        characters = string.ascii_letters+string.digits

    elif complexity == "hard":
        characters = string.ascii_letters + string.digits+string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Please Enter the desired length for your password: "))
            if length <= 0:
                print("The length of the password must be a positive integer.")
                return

            complexity = input("Please enter the complexity level(easy,medium,hard)")

            if complexity not in complexity_level:
                print("Invalid input. Please choose from the following options")
                return


            password = password_generator(length,complexity)
            print("Your generated password is:", password)
            print("Thankyou")

            another_password = input("Generate another password? (yes/no): ").lower()
            if another_password != "yes":
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the password length.")

if __name__ == "__main__":
    main()