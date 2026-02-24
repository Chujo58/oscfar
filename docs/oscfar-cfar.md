---
title: CFAR Algorithms
layout: page
parent: Documentation
nav_order: 2
---

<a name="oscfar-cfar"></a>
## 🅼 oscfar\.cfar

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-cfar-os_cfar_1d"></a>
### 🅵 oscfar\.cfar\.os\_cfar\_1d

```python
def os_cfar_1d(data, guard_cells, train_cells, rank_k, threshold_factor):
```

Performs 1D Ordered Statistic Constant False Alarm Rate \(OS-CFAR\) detection\.

**Parameters:**

- **data** (`np.ndarray`): 1D array of input data \(must be in linear power,
not dB\)\.
- **guard_cells** (`int`): Number of guard cells on EACH side of the CUT\.
- **train_cells** (`int`): Number of training cells on EACH side of the CUT\.
- **rank_k** (`int`): The rank \(1-based index\) of the sorted training cell
values to use for noise estimation \(1 \<= rank\_k \<= N\)\.
N = 2 \* train\_cells is the total number of training cells\.
A common choice is around 0\.75 \* N\.
- **threshold_factor** (`float`): The scaling factor \(alpha\) to multiply the
noise estimate by to get the threshold\.

**Returns:**

- `detected_peaks_indices (np.ndarray)`: Indices where peaks were detected\.
threshold \(np\.ndarray\): Threshold for each input cell \(NaN at edges
where CFAR is not computed\)\.
<a name="oscfar-cfar-variable_window_cfar"></a>
### 🅵 oscfar\.cfar\.variable\_window\_cfar

```python
def variable_window_cfar(data, guard_cells, min_window, max_window, homogeneity_threshold):
```

A basic implementation of a Variable Window CFAR detector using a split-window approach\.

**Parameters:**

- **data** (`np.ndarray`): The input signal data \(1D\)\.
- **guard_cells** (`int`): The number of guard cells on each side of the CUT\.
- **min_window** (`int`): The minimum number of reference cells on each side\.
- **max_window** (`int`): The maximum number of reference cells on each side\.
- **homogeneity_threshold** (`float`): A threshold to determine if the reference
windows are considered homogeneous\.

**Returns:**

- `detections (np.ndarray)`: Boolean array of detections \(True\) and
non-detections \(False\)\.
<a name="oscfar-cfar-variable_window_os_cfar_indices"></a>
### 🅵 oscfar\.cfar\.variable\_window\_os\_cfar\_indices

```python
def variable_window_os_cfar_indices(data, guard_cells, min_window, max_window, k_rank, homogeneity_threshold, threshold_factor):
```

A basic implementation of a Variable Window OS-CFAR detector returning detection indices\.

**Parameters:**

- **data** (`np.ndarray`): The input signal data \(1D\)\.
- **guard_cells** (`int`): The number of guard cells on each side of the CUT\.
- **min_window** (`int`): The minimum number of reference cells on each side\.
- **max_window** (`int`): The maximum number of reference cells on each side\.
- **k_rank** (`int`): The rank of the order statistic to use for noise estimation\.
- **homogeneity_threshold** (`float`): A threshold to determine if the reference
windows are considered homogeneous\.
- **threshold_factor** (`float`): Factor multiplied by the noise estimate for the threshold\.

**Returns:**

- `detection_indices (np.ndarray)`: Indices where detections occurred\.
