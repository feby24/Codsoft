import random
import string

def generate_password(length):
    return ''.join(random.choice(string.printable) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print("Invalid input. Please enter a positive integer for the length.")
    else:
        password = generate_password(length)
        print("Generated password:", password)
