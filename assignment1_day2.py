#  Name:Asaph Saji, Roll no: 2311042


# Determine the value of π using throwing method by choosing a quarter circle of
# unit radius in the first quadrant. Plot the value of π versus number of throws
# 20 ≤ N ≤ 2, 000.

import matplotlib.pyplot as plt
from library import Myrand
import numpy as np

def pif(n):
    lcg =  Myrand(seed = 10)
    count = 0
    X , Y = [] , []
    for _ in range(n):
        x = lcg.rand()
        y = lcg.rand()
        X.append(x)
        Y.append(y)
        if x**2 + y**2 <= 1:
            count += 1
    pi_num = 4 * count / n
    return pi_num


Z = []
W = []
for i in range (20,2000,20):
    c = pif(i)
    W.append(i)
    Z.append(c)

sum = 0
for j in Z:
    sum +=j

avg = sum/len(W)

print(avg)
print(Z,W)
plt.plot(W,Z, marker = '.')
plt.title("Pi value vs throws")
plt.xlabel("Throws")
plt.ylabel("pi value")
plt.show()

################################################
#plot is attached
# average value of pi obtained = 3.1183043202110134
##################################################


# Generate pRNG having exponential distribution of the form exp(−x) from pRNG
# having uniform distribution in [0, 1). Generate at least 5,000 random numbers


def genex_random(n, seed=10):
    rng = Myrand(seed=seed)
    random_numbers = [rng.rand() for _ in range(n)]
    exponential_random= [-np.log(1 - u) for u in random_numbers]
    return exponential_random
w = genex_random(5000)

plt.hist(w, bins = 20, color = 'red', edgecolor='blue')
plt.show()
#######################################################
#plot is atttached
###################################################