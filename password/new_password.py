import random
import string

def generate_password(length=12):
    """generates password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

# usage example
password_length = 12 
print("Ваш новый пароль:", generate_password(password_length))