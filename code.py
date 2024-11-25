"""
This is a simple example of how to use matplotlib to plot a function.

The function used is the sine function, which takes in a numpy array of x
values and returns the sine of those values.

The numpy array is created using the arange function, which takes in a
start value, a stop value, and a step value. The start value is 0, the
stop value is 10, and the step value is 0.1.

The plot is created using the plot function, which takes in two numpy
arrays: the x values and the y values. The x values are the numpy array
created above, and the y values are the sine of those x values.

The show method is used to display the plot.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.25)
y = np.sin(x)
plt.plot(x, y)
plt.show()
