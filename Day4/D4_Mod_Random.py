# Create a program to show randomly heads or tails
# article for number generator http://en.wikipedia.org/wiki/Mersenne_Twister
# video about pseudoradom https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# Python doc for random https://docs.python.org/3/library/random.html


import random

#heads_val = random.randint(1,5)
#tails_val = random.randint(6,10)

rand_val = random.randint(1,10)

if rand_val <= 5:
    print("Heads")
    print(rand_val)
else:
    print("tails")
    print(rand_val)
