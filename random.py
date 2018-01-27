# Using the lcg algo to create a custom random number generator
from threading import Thread
import time

a = 1103515245
# Declaring the multiplier
m = 2 ** 32
# Declaring the modulus
c = 12345
# Declaring the increment
global seed
# Using time to initialise the seed
seed = time.time()


# Generating greater and lower numbers simultaneously
def parallel():
    Thread(target=lower()).start()
    Thread(target=higher()).start()


# Random number generation function
def random():
    global seed
    seed = (a * seed + c) % m
    return (int)(round(seed % (end - start)))


# We need only 27% of the total numbers to be lower
def lower():
    for i in range(0, (int)(round(total * .27))):
        value = (int)(round(random()/2))
        print (start + value),
        print ',',


# 73% of the numbers are greater thus generating a biased series
def higher():
    for i in range(0, (int)(round(total * .73))):
        value = (int)(round(random()/2))
        print (start + ((end - start + 1) / 2) + value),
        print ',',


start = input("Enter the lower bound : \n")
end = input("Enter the upper bound : \n")
total = input("Enter the length of the series : \n")
print "The random number series is : \n"
# Starting the function
parallel()
