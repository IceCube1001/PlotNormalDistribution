# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:38:34 2020
Plot Normal Distribution
@author: ROY.ZHOU
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-10, 10, 0.001)
plt.grid()
# Mean = 0, SD = 3.5
plt.plot(x_axis, norm.pdf(x_axis,0,3.5))
plt.show()