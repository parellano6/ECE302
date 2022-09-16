# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:36:16 2022

@author: palom
"""
import random
import numpy as np
import matplotlib.pyplot as plt

totval = 10000

Z = [random.randint(1, 6) for x in range(totval)]
for i in range(99):
    X = [random.randint(1, 6) for x in range(totval)]
    Z = np.add(X, Z)

plt.hist(Z, range(6, 602), linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title(str(totval) + ' Random Values from the Summed Set Z')