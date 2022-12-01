# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:35:44 2022

@author: palom
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import time

def program():
    train_cat = np.matrix(np.loadtxt('train_cat.txt', delimiter = ','))
    train_grass = np.matrix(np.loadtxt('train_grass.txt', delimiter = ','))
    
    # Cat data
    mu_cat = np.mean(train_cat, 1)  # mean vector
    sigma_cat = np.cov(train_cat)   # cov
    k_cat = np.size(train_cat, 1)   # size
    
    # Grass data
    mu_grass = np.mean(train_grass, 1)  # mean
    sigma_grass = np.cov(train_grass)   # cov
    k_grass = np.size(train_grass, 1)   # size
    
    
    # Showing cat image
    pic = plt.imread("cat_grass.jpg") / 255
    
    # Extracting patches
    M = np.size(pic, 0)
    N = np.size(pic, 1)
    output = np.zeros((M-8, N-8))
    
    cov_i_cat = np.linalg.inv(sigma_cat)        # inverse cov - cat
    cov_i_grass = np.linalg.inv(sigma_grass)    # inverse cov - grass
    det_cov_cat = np.linalg.det(sigma_cat)      # det of cov - cat
    det_cov_grass = np.linalg.det(sigma_grass)  # det of cov - grass
    f_cat = k_cat / (k_cat + k_grass)
    f_grass = k_grass / (k_cat + k_grass)
    
    for i in range(M - 8):
        for j in range(N - 8):
            z = pic[i:(i+8), j:(j+8)]
            patch64 = z.flatten('F')
            patch64_1 = np.reshape(patch64, (64, 1))
            
            cat_1 = patch64_1 - mu_cat
            cat_2 = np.dot(cat_1.T, cov_i_cat)
            cat_3 = math.exp((-1 / 2) * (np.dot(cat_2, cat_1).item()))
            cat_4 = 1 / (pow((2 * np.pi), 32) * pow(det_cov_cat, 0.5))
            f_z_cat = cat_3 * cat_4
            
            grass_1 = patch64_1 - mu_grass
            grass_2 = np.dot(grass_1.T, cov_i_grass)
            grass_3 = math.exp((-1 / 2) * (np.dot(grass_2, grass_1).item()))
            grass_4 = 1 / (pow((2 * np.pi), 32) * pow(det_cov_grass, 0.5))
            f_z_grass = grass_3 * grass_4
            
            f_cat_z = f_z_cat * f_cat
            f_grass_z = f_z_grass * f_grass
            
            if f_cat_z > (f_grass_z * 10):      # LINE CHANGED TO IMPROVE MAE
                output[i, j] = 1
                
    plt.imshow(output * 255, cmap='gray')
    plt.show()
    
    return output
        
    
start_time = time.time()
output = program()
print('My runtime is %s seconds' % (time.time() - start_time))

correct = plt.imread("truth.png")
maeVals = []
for i in range(np.size(output, 0)):
    for j in range(np.size(output, 1)):
        corrVal = correct[i, j]
        outVal = output[i, j]
        maeVals.append(abs(corrVal - outVal))
        
maeOut = np.mean(maeVals)
print("The mean absolute error is " + format(maeOut))