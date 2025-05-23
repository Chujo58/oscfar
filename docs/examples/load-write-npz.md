---
title: Loading and writing npz files
layout: page
parent: How to use oscfar
nav_order: 3
---

## Loading and writing npz files
### Format of npz files
[`fitburst`](https://github.com/CHIMEFRB/fitburst) comes with a `DataReader` class which is used to load `.npz` files saved using `numpy`.

The data saved in the `.npz` file needs to be formatted with the following information:
- `data_full`: a `numpy` 2D array containing the dynamic spectrum (frequency vs time) of the data;
- `metadata`: some useful information like number of frequency channels, number of time bins, etc;
- `burst_parameters`: the burst information.

For more information about the formatting of `.npz` files, please read [Format of Input Data](https://chimefrb.github.io/fitburst/usage/formatting_data_generic/).

### Loading npz files
To load `.npz` files using `oscfar`, you need to provide two informations: the filepath and the downsampling factor of the data.

For example:
```python
import oscfar as ocf
reader = ocf.npz_reader(filepath, downsampling_factor)
```
The data will automatically be loaded using the `DataReader.load_data()` method.

### Writing npz files
To write `.npz` files using `oscfar`, you can either provide a filepath linking to the original data you want to modify or an `oscfar.npz_reader` object.