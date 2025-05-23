---
title: Using CFAR Algorithms
layout: page
parent: How to use oscfar
nav_order: 1
---

## Using CFAR Algorithms
### oscfar.do_os_cfar
```python
import oscfar as ocf
data = ... #A numpy 2D array (frequency vs time).

results = ocf.do_os_cfar(**{
    'data': data,
    'guard_cells': 1,
    'train_cells': 10,
    'rank_k': 0.75,
    'threshold_factor': 1.05,
    'averaging': 2,
    'min_dist': 5,
    'min_snr': 2,
    'baseline': 0.15,
}) #Output: ocf.peaks
# Note you can also do the following to use the best_params dictionary:
results = ocf.do_os_cfar(data, **ocf.best_params, min_dist=5) #Output: ocf.peaks
```

### oscfar.os_cfar
```python
import oscfar as ocf
data = ... #A numpy !D array (time series).

results = ocf.os_cfar(**{
    'data': data,
    'guard_cells': 1,
    'train_cells': 10,
    'rank_k': 0.75,
    'threshold_factor': 1.05,
}) #Output: tuple(peaks indices, threshold)
```

### oscfar.vwindow_os_cfar
```python
import oscfar as ocf
data = ... #A numpy !D array (time series).

results = ocf.vwindow_os_cfar(**{
    'data': data,
    'guard_cells': 1,
    'min_window': 2, #Minimum train cell window
    'max_window': 10, #Maximum train cell window
    'homogeneity_threshold': 1.05
}) #Output: boolean array where detections are True and non-detections are False.
```