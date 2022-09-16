# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:22:32 2022

@author: palom
"""
import random
import numpy as np
import matplotlib.pyplot as plt

totval = 10000

Z = [random.randint(1, 6) for x in range(totval)]
for i in range(9):
    X = [random.randint(1, 6) for x in range(totval)]
    Z = np.add(X, Z)

plt.hist(Z, range(6, 62), edgecolor='black', linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title(str(totval) + ' Random Values from the Summed Set Z')