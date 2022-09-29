#importing
import matplotlib.pyplot as plt
import numpy as np

#defining points
xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
ypoints = np.array([17, 18, 20, 19, 16, 26, 15, 16, 24, 24, 15, 21, 16, 23, 15, 20, 15, 15, 18, 16, 34, 51, 54, 45, 53, 31, 33, 16, 34, 23, 63, 28, 25, 17, 42, 16, 36, 28, 25, 15, 5])

#drawing out the points
plt.plot(xpoints, ypoints, '*--g')


#drawing the lines


plt.show()
