import re       

name = input('enter your name:')
password = input('enter your password')
if not password:
    print('password cannot be empty')
elif re.search(r'name',password):
    print('password cant have your name in it' )



def check_lowercase(password):
    return bool(re.search(r'[a-z]',password))

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_digit(password):
    return bool(re.search(r'\d',password))

def check_spec_character(password):
    return bool(re.search (r'(!@#$%^&*)',password))

def check_character_lenght(password):
    return len(password)>=8

def strenght(password):
    score=0 
    if check_character_lenght(password): score =+1
    if check_digit(password): score=+1
    if check_lowercase(password):score=+1
    if check_spec_character(password):score=+1
    if check_uppercase(password):score=+1
    return score


score = strenght(password)

if score == 5:
    print("strong")
if score >=3:
    print("moderate")
else: 
    print("weak")

