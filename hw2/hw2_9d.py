# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:13:29 2022

@author: palom
"""
import random
import numpy as np
import matplotlib.pyplot as plt

X = [random.randint(1, 6) for x in range(10000)]
Y = [random.randint(1, 6) for x in range(10000)]
Z = np.add(X, Y)

plt.hist(Z, range(1, 15), edgecolor='black', linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title('10000 Random Values from the Summed Set Z')
