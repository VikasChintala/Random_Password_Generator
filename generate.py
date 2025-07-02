import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user how long the password should be
length = int(input("Enter password length: "))
print("Your new password is:", generate_password(length))
