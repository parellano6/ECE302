"""
Program that solves problem 9
"""
import numpy as np
import matplotlib.pyplot as plt
import random


# Multiplies the matricies specified in 9a
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[1],
           [2],
           [3]]

print("The resulting matrix multiplcation is:")
print(np.matmul(matrix1, matrix2))


# Plots a sine function on the interval [−π, π] with 1000 data points
x = np.arange(-1 * np.pi, np.pi, (2 * np.pi / 1000))
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Sine Function from [−π, π]')
plt.show()


# Generate histogram of 10,000 uniformly distributed random numbers on interval [0, 1).
num_vals = [random.random() for x in range(10000)]
plt.hist(num_vals, edgecolor='black', linewidth=1.2)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Uniformly Distributed Random Numbers on Interval [0, 1)')