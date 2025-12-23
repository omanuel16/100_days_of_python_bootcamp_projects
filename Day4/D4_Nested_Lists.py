import random

Payer_list = ["Hector", "Oscar", "Dany", "Osw", "Bety", "Eli"]

#random choose in two lines
the_one = random.randint(0,5)
print(Payer_list[the_one])

#random choose in one line
print(random.choice(Payer_list))
# to konw the list length
print(len(Payer_list))

# NESTED LIST
Friend_payer_list = ["Pepe", "Meño", "Alejandro", "Diana"]
all_payers = [Friend_payer_list, Payer_list]
print (all_payers)
print(all_payers[1][1])
print(all_payers[1])