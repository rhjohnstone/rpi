import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

x, ten_y = np.loadtxt("output.txt").T

plt.plot(x, ten_y/10)
plt.show()
