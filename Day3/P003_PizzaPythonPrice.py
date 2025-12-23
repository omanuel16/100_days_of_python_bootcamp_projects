print("Welcome to the Pizza Python Price Calculator!")
size = input("what size pizza do you want? S, M, L: ").upper()
add_peperoni = input("Do you want to add peperoni? Y or N: ").upper()
add_cheese = input("Do you want to add cheese? Y or N: ").upper()
bill = 0
if size == "S":
    bill += 15
    if add_peperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_peperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_peperoni == "Y":
        bill += 3
if add_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")  

