import re

name = input('Enter your name: ')
password = input('Enter your password: ')

# Check for empty password
if not password:
    print('Password cannot be empty.')

# Check if the password contains the user's name
elif name.lower() in password.lower():
    print('Password cannot contain your name.')

else:
    # Password validation functions
    def check_lowercase(password):
        return bool(re.search(r'[a-z]', password))

    def check_uppercase(password):
        return bool(re.search(r'[A-Z]', password))

    def check_digit(password):
        return bool(re.search(r'\d', password))

    def check_spec_character(password):
        return bool(re.search(r'[!@#$%^&*]', password))

    def check_character_length(password):
        return len(password) >= 8

    def strength(password):
        score = 0
        if check_character_length(password): score += 1
        if check_digit(password): score += 1
        if check_lowercase(password): score += 1
        if check_spec_character(password): score += 1
        if check_uppercase(password): score += 1
        return score

    # Check the strength
    score = strength(password)

    if score == 5:
        print("Strength: Strong")
    elif score >= 3:
        print("Strength: Moderate")
    else:
        print("Strength: Weak")
