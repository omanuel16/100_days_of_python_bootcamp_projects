from operator import concat
import random

# 26 items
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 10 itmes
number = ['0','1','2','3','4','5','6','7','8','9']
# 6 items
symbols = ['!','#','$','%','&','*']
#print("Welcome to the PyPassword Geenrator! \n Use it! ")
nr_letters = int(input("How many letters woould you like in your passwords?\n"))
nr_symbols = int(input("How many symbols woudl you like? \n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy level  - Concern is that the password letters and number are not in a random order
password = "" # Here it is creating a string NOT A LIST
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_numbers):
    password += random.choice(number)
for char in range(0, nr_symbols):
    password += random.choice(symbols)

print("This password was created with the Easy version code \n"+ password)

# Better version

password_list = [] # Here it is creating a LIST
for char in range (0, nr_letters):
    password_list.append(random.choice(letters))
for char in range (0, nr_numbers):
    password_list.append(random.choice(number))
for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
# Now the list will be need to be run in a loop to convert it to a string

new_pass = ""
for char in password_list:
    new_pass += char
print(f"This password was created with the hard version code \n {new_pass}")