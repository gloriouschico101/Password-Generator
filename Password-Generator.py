import random
import string

letters = string.ascii_letters

password = ""

for i in range(10):
    password = password + random.choice(letters)

print(password)