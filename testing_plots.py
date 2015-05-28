''' A module that creates a graph on python'''

import numpy as np
import matplotlib as mpl
x_range= np.arange(0.1,10.,.01)
y_range = np.sin(x_range)
import matplotlib.pyplot as plt
plt.plot(x_range,y_range,'g')
plt.savefig('mysinwave2')
