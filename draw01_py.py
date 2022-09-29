#importing
import matplotlib.pyplot as plt
import numpy as np

#defining points
xpoints = np.array([25, 25, 25, 1, 49, 49, 1, 1, 49])
ypoints = np.array([25, 49, 1, 25, 25, 49, 1, 49, 1])

#drawing out the points
plt.plot(xpoints, ypoints, '*--g')


#drawing the lines


plt.show()
