# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:57:43 2022

@author: palom
"""
import random
import matplotlib.pyplot as plt

X = [random.randint(1, 6) for x in range(10000)]

plt.hist(X, range(1, 8), edgecolor='black', linewidth=1.2, align = 'left')
plt.xlabel('Sample Space')
plt.ylabel('Frequency')
plt.title('10000 Random Values from the Set {1,2,3,4,5,6}')