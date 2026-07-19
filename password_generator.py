import random
import string

def generate_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers :
        characters += digits
    if special_char:
        characters += special

    password = ""
    having_number = False
    having_special = False

    while len(password) < min_length or (numbers and not having_number) or (special_char and not having_special):
        another_char = random.choice(characters)
        password += another_char

        if another_char in digits:
            having_number = True
        elif another_char in special:
            having_special = True

    return password

length = int(input("Enter the length of your password : "))
add_number = input("Do you want to add numbers to your password(yes/no) : ").lower() == "yes"
add_character = input("Do you want to add some characters to your password(yes/no) : ").lower() == "yes"
pwd = generate_password(length, add_number, add_character)
print("Generated Password : ", pwd)
