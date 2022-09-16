# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 05:25:38 2022

@author: palom
"""
import matplotlib.pyplot as plt
import numpy as np
import cmath
import math

k = 1.37488681 * (10 ** 9)
x0 = 3
y0 = 20
x = np.arange(-50, 50.1, 0.1)

psi1 = []
psi2 = []

val1 = 0 + 1j

for i in x:
    psi1.append(abs(cmath.exp(val1 * k * math.sqrt( (i - x0) ** 2 + (y0 **2))) / ((i - x0) ** 2 + y0 ** 2)) ** 2)

for j in x:
    psi2.append(abs(cmath.exp(val1 * k * math.sqrt( (j + x0) ** 2 + (y0 **2))) / ((j + x0) ** 2 + y0 ** 2)) ** 2)

plt.scatter(x, psi1)                # psi1 for first slit
plt.scatter(x, psi2, c="orange")    # psi2 for second slit

plt.scatter(x, np.add(psi1, psi2), c="red")     # adding two slits together
plt.xlabel('Location')
plt.ylabel('Probability')
plt.title('"Probability” of Finding an Electron in Region −50λ ≤ x ≤ 50λ\n')
plt.show()