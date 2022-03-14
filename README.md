# LivePlot

# `Plotter`
### `Plotter(title, labels=None, figure=None, ax=None)`

Constructor 
- **title**: title of the subplot
- **labels**: list of lines
- **figure**: set if add plotter to existing figure, keep `None` to create a new figure
- **ax**: if `figure` is set, also set `ax`

### `add_data(x, y, label='', smoothing=0)`

Adds single data point (x, y) to the plot
- **x**, **y**: number
- **label**: label to add data to
- **smoothing**: expnentially weighted smoothing factor

### `save(dir_name='Plots/')`

Saves a plot as `title.png`
- **dir_name**: directory for saving

### `close()`

Closes the window

# `MultiPlotter`

### `MultiPlotter(n_plots)`

Constructor
- **n_plots**: number of plots to show in the window


### `add_plot(title, labels, hline=-1)`

Adds a `Plotter` object with `title` and `labels`
- **hline**: set to anything != -1 for a horziontal line annotation

### `save(name)`

Saves the plot under `logs/name.png`

### `close()`

Closes the window