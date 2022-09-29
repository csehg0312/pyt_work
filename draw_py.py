#importing

import matplotlib.pyplot as plt
import numpy as np

#defining points
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

#drawing
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, 'o')
plt.show()