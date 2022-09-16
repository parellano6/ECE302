# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:59:12 2022

@author: palom
"""
import random
import numpy as np
import matplotlib.pyplot as plt

X = [random.randint(1, 6) for x in range(100)]
Y = [random.randint(1, 6) for x in range(100)]
Z = np.add(X, Y)

plt.hist(Z, range(1, 15), edgecolor='black', linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title('100 Random Values from the Summed Set Z')