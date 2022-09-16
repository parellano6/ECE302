# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:15:14 2022

@author: palom
"""
import random
import numpy as np
import matplotlib.pyplot as plt

totval = 10000

X = [random.randint(1, 6) for x in range(totval)]
Y = [random.randint(1, 6) for x in range(totval)]
Z = np.add(X, Y)

count_5_7 = 0
for i in Z:
    if i == 5 or i == 6 or i == 7:
        count_5_7 += 1

prob_5_7 = count_5_7 / totval

print("The probability that a value in set Z is in (4, 7] is " + str(prob_5_7))

plt.hist(Z, range(1, 15), edgecolor='black', linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title(str(totval) + ' Random Values from the Summmed Set Z')
