from liveplot import *

import numpy as np
import time

if __name__ == '__main__':
    multiplotter = MultiPlotter(2)
    plotter1 = multiplotter.add_plot('plot1', labels=['line1', 'line2'], hline=1)
    plotter2 = multiplotter.add_plot(f'plot2', labels=['line1', 'line2'], hline=0)

    n = 50
    x = np.arange(n) + 1
    y11 = x ** 2 + np.random.random(n) * 15
    y12 = x ** 2.3 + np.random.random(n) * 15
    y21 = 1 / x + np.random.random(n) * 0.1
    y22 = 1 / (x ** 2) + np.random.random(n) * 0.01
    for i in range(n):
        plotter1.add_data(x[i], y11[i], label='line1')
        plotter1.add_data(x[i], y12[i], label='line2')
        plotter2.add_data(x[i], y21[i], label='line1')
        plotter2.add_data(x[i], y22[i], label='line2')