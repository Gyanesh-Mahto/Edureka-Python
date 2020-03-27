#Random Module:
#--------------#
'''
This module implements pseudo-random number generators for various distributions
'''
import random
#random.seed(1010)  #When seed is used, our results will be always constant

print(random.uniform(6,2))

num=random.randrange(100)   #Generates a random integer within the given range
print(num)

ran=random.randrange(0,100,20)  #Generates a randomly selected element from range(start,stop,step)
print(ran)

inte=random.randint(0,30)   #Return a random integer N such that a<=N<=b
print(inte)

'''
Random Module - Real life application:
---------------------------------------
-> For encrypting your banking session on the internet.
-> To randomly allow a new enemy spaceship to appear and shoot at you in gaming.
-> To simulate possible rainfall when we make a computerized model for estimating the
environmental impact of building a dam.
'''