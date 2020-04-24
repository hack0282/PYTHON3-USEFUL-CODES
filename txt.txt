#random password generator
import string
import random

password_characters = string.ascii_letters + string.digits + string.punctuation 
while True:
    if input("would you like a password to enter press yes/y or no/n:").lower() not in {'y' or 'yes'}:
        break
    length = int(input("enter password length:"))
    password = ''.join([random.choice(password_characters)          #string objectjoin random charcters
                        for _ in range(length)])
    print(password)
