# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:14:43 2022

@author: palom
"""

import numpy as np
from PIL import Image

img = Image.open("koala.jpg")
img1 = img.convert("L")


Y = np.random.poisson(img, size=(1000,)+np.shape(img))
B = np.where(Y>=1,1,0) * 255
#lamb = (-1 * np.log(1- np.mean(B,0)))
temp = Image.fromarray(B)
final = temp.convert("L")
#saving final image
