# List store related data in order
#data structure artcle https://docs.python.org/3/tutorial/datastructures.html

Cryto_assests = ["BTC", "ETH", "RPX", "USDT"]

print(Cryto_assests[0]) # it will print BTC
print(Cryto_assests[-1]) # it iwll print the last of the list and every 
# you can edit a value making reference of the position you want to change:
Cryto_assests[2] = "XRP"
print(Cryto_assests[2])
# to add a new item you need to append
Cryto_assests.append("BNB")
# or you can extend the list with a new list 
Cryto_assests.extend(["SOL","TRX"])
print(Cryto_assests)