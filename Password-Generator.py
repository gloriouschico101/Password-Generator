import random
import string

letters = string.ascii_letters

password = ""

length = int(input("Enter a password length between 0-50: "))

if length < 0 or length > 50:
    print("Error: Please enter a number between 0 and 50")

else:
    for i in range(length):
        password = password + random.choice(letters)

print(password)