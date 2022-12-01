# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:25:37 2022

@author: palom
"""
import matplotlib.pyplot as plt
import numpy as np

# Showing cat image
pic = plt.imread("cat_grass.jpg")

out = plt.figure(figsize = (15,32))
plt.imshow(pic)
plt.title("Input Image")
plt.show()

# Extracting patches
val1 = np.size(pic, 0)
val2 = np.size(pic, 1)
outMatrix = [[0]*0]*64

for i in range(val1 - 8):
    for j in range(val2 - 8):
        patch = pic[i:(i + 8), j:(j + 8)]
        patch64 = patch.flatten('F')
        patch64_1 = np.reshape(patch64, (64, 1))
        print("i: " + str(i) + " j: " + str(j))
        outMatrix = np.append(outMatrix, patch64_1, 1)
        outMatrix.shape
        
mean_vec = np.mean(outMatrix, 1) # mean
cov = np.cov(outMatrix) # covariance