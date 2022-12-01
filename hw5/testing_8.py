# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:44:48 2022

@author: palom
"""

import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

# read the image of a plant seedling as grayscale from the outset
#image = skimage.io.imread(fname="hw5_input.jpg", as_gray=True)
image = skimage.io.imread(fname="contrast_stretch.jpg", as_gray=True)

# display the image
fig, ax = plt.subplots()
plt.imshow(image, cmap="gray")

histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
histogram[0] = 50000
histogram[255] = 95000
print(histogram)
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([-0.1, 1.1])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
