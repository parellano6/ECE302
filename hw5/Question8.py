# -*- coding: utf-8 -*-
'''
import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('hw5_input.jpg')
  
# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
  
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)
  
# Save the output.
cv2.imwrite('log_transformed.jpg', log_transformed)
'''

'''
import cv2
import numpy as np
  
# Open the image.
img_rgb = cv2.imread('hw5_input.jpg')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 0.8, 0.9, 1.0, 1.2, 2.2]:
      
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
  
    # Save edited images.
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

  
# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
  
# Open the image.
img_rgb = cv2.imread('hw5_input.jpg')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  
# Define parameters.
r1 = 130
s1 = 150
r2 = 175
s2 = 255
  
# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)
  
# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
  
# Save edited image.
cv2.imwrite('contrast_stretch.jpg', contrast_stretched)


