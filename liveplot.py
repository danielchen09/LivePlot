import pylab as plt
import matplotlib
import math

matplotlib.use('Qt5agg')
plt.ion()

class MultiPlotter:
    def __init__(self, n_plots):
        self.plotters = []
        self.figure = plt.figure(figsize=(10, 4))
        self.n_plots = n_plots

    def add_plot(self, title, labels, hline=-1):
        ax = self.figure.add_subplot(int(f'1{self.n_plots}{len(self.plotters) + 1}'))
        if hline != -1:
            ax.axhline(hline, color='black', linestyle='--')
        self.plotters.append(Plotter(title, labels, self.figure, ax))
        return self.plotters[-1]

    def save(self, name):
        plt.savefig(f'logs/{name}.png')

    def close(self):
        plt.close(self.figure)


class Plotter:
    def __init__(self, title, labels=None, figure=None, ax=None):

        self.title = title
        if not labels:
            labels = ['']
        self.xs = {label: [] for label in labels}
        self.ys = {label: [] for label in labels}
        self.figure = figure
        self.ax = ax
        if not figure:
            self.figure = plt.figure()
            self.ax = self.figure.add_subplot(111)
        self.labels = labels
        self.lines = {label: self.ax.plot(self.xs[label], self.ys[label], label=label)[0] for label in labels}
        self.ax.set_title(self.title)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlabel('epochs')
        self.maxy = 0
        self.miny = 10

    def add_data(self, x, y, label='', smoothing=0):
        if math.isnan(y):
            return
        self.maxy = max(y, self.maxy)
        self.miny = min(y, self.miny)
        self.xs[label].append(x)
        self.ys[label].append(y)

        smoothed = []
        last = self.ys[label][0]
        for y in self.ys[label]:
            smoothed.append(last * smoothing + (1 - smoothing) * y)
            last = y

        self.lines[label].set_xdata(self.xs[label])
        self.lines[label].set_ydata(smoothed)

        midy = (self.maxy + self.miny) / 2
        yrange = max((self.maxy - self.miny) * 2, 0.1)
        self.ax.set_xlim(0, max(max(self.xs[label]), 1))
        self.ax.set_ylim(midy - yrange / 2, midy + yrange / 2)
        plt.legend()
        plt.draw()
        plt.pause(0.01)

    def save(self, dir_name='Plots/'):
        plt.draw()
        plt.savefig(f'{dir_name}{self.title}.png')

    def close(self):
        plt.close(self.figure)