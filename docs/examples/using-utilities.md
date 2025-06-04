---
title: Plotting the data quickly
layout: page
parent: How to use oscfar
nav_order: 2
---

## Plotting the data quickly
If your data is saved under a `.npz` format like [fitburst](https://github.com/CHIMEFRB/fitburst) uses, the data can be plotted quickly.

There are two main plotting functions, one to create a single image of the data and another to create a grid view of multiple datasets at once.

### oscfar.waterfall_axes
```python
import oscfar as ocf

filepath = ... #Path to the .npz file
down = ... #Downsampling factor of the .npz file
reader = ocf.reader(filepath, down)

ax = ocf.waterfall_axes()
ax.plot(reader, title="Title", readjust_title=0.1)
# If you have a ocf.peaks object:
ax.plot_time_peaks(peaks, 'red', show_thres=False)
```

### oscfar.waterfall_grid
```python
import oscfar as ocf

filepaths = [...] #Paths to `.npz` files
downs = [...] #Downsampling factors of the `.npz` files
readers = [ocf.reader(filepath, down) for filepath, down in zip(filepaths, downs)]
peaks = [...] #ocf.peaks object for each reader above
titles = [...] #Titles for each reader above

grid = ocf.waterfall_grid(nrow, ncol)
grid.plot(readers, peaks, titles, 'red', adjust_t=0.1, show_thres=False)
# If you want to add a table with interesting information at the bottom of the grid view:
grid.add_info(pd.DataFrame(interesting_data: dict))
```