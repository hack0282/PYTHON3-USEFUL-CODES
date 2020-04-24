#regular expressions
#email validation
#password validation
import re

pattern = re.compile(r"(^[a-zA-Z0-90-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$)")
pattern1 = re.compile(r"([A-Za-z0-9$!%#@]{7,}[0-9])")
email = input("enter your valid email=")
password = input('enter password')
passwordlen = '*' * len(password)
print(email)
print(passwordlen)
a = pattern.findall(email)
if a:
    print('it\'s valid')
else:
    print('not valid')
b = pattern1.findall(password)
if b:
    print('it\'s valid')
else:
    print('not valid')