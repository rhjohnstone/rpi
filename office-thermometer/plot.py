import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from datetime import datetime

x, ten_y = np.loadtxt("output.txt", dtype=int).T
time = np.array([datetime.fromtimestamp(t) for t in x])

h = 5
fs = 14
fig, ax = plt.subplots(1, 1, figsize=(2*h,h))
ax.plot(time, ten_y/10)
ax.set_ylabel('Temperature (C)', fontsize=fs)
ax.set_xlabel('Time', fontsize=fs)
ax.set_title('"Winter" 2020 in the Tokyo Office', fontsize=fs)
fig.tight_layout()
fig.savefig('office-temp.png')
plt.show()
