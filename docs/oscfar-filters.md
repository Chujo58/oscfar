---
title: Filtering
layout: page
parent: Documentation
nav_order: 3
---

<a name="oscfar-filters"></a>
## 🅼 oscfar\.filters

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-filters-remove_baseline_peaks"></a>
### 🅵 oscfar\.filters\.remove\_baseline\_peaks

```python
def remove_baseline_peaks(data, detection_indices, noise_estimates, secondary_threshold_factor = 2.0):
```

Removes detected peaks that are too close to the baseline using a secondary amplitude threshold\.

**Parameters:**

- **data** (`np.ndarray`): The original signal data\.
- **detection_indices** (`np.ndarray`): Indices of peaks detected by OS-CFAR\.
- **noise_estimates** (`np.ndarray`): Array of noise estimates corresponding to each detection\.
- **secondary_threshold_factor** (`float`): Factor multiplied by the noise estimate
to set the secondary threshold\.

**Returns:**

- `filtered_detections (np.ndarray)`: Indices of filtered detections\.
<a name="oscfar-filters-median_filter"></a>
### 🅵 oscfar\.filters\.median\_filter

```python
def median_filter(data, kernel_size):
```

Applies a median filter to the 1D data\.

**Parameters:**

- **data** (`np.ndarray`): 1D array of input data\.
- **kernel_size** (`int`): The size of the median filter kernel\. Must be a
positive integer\. If even, it will be incremented
by 1 to ensure an odd size\.

**Returns:**

- `filtered_data (np.ndarray)`: Median-filtered data, same shape as input\.

**Raises:**

- **ValueError**: If input data is not a 1D numpy array, or if kernel\_size
is not a positive integer\.
<a name="oscfar-filters-lowpass_filter"></a>
### 🅵 oscfar\.filters\.lowpass\_filter

```python
def lowpass_filter(data, cutoff_freq, sampling_rate, order = 5):
```

Applies a low-pass Butterworth filter to the 1D data\.

This uses a zero-phase filter \('filtfilt'\) to avoid introducing phase shifts in the filtered signal\.

**Parameters:**

- **data** (`np.ndarray`): 1D array of input data \(e\.g\., time series\)\.
- **cutoff_freq** (`float`): The desired cutoff frequency in Hz\. Frequencies
above this value will be attenuated\.
- **sampling_rate** (`float`): The sampling rate of the input data in Hz\.
This is crucial for digital filter design\.
- **order** (`int`): The order of the Butterworth filter\. Higher
orders provide a steeper rolloff but can be
less stable\. Defaults to 5\.

**Returns:**

- `filtered_data (np.ndarray)`: Low-pass filtered data, same shape as input\.

**Raises:**

- **ValueError**: If input data is not a 1D numpy array, or if
cutoff\_freq or sampling\_rate are invalid\.
<a name="oscfar-filters-highpass_filter"></a>
### 🅵 oscfar\.filters\.highpass\_filter

```python
def highpass_filter(data, cutoff_freq, sampling_rate, order = 5):
```

Applies a high-pass Butterworth filter to the 1D data\.

This uses a zero-phase filter \('filtfilt'\) to avoid introducing
phase shifts in the filtered signal\.

**Parameters:**

- **data** (`np.ndarray`): 1D array of input data \(e\.g\., time series\)\.
- **cutoff_freq** (`float`): The desired cutoff frequency in Hz\. Frequencies
below this value will be attenuated\.
- **sampling_rate** (`float`): The sampling rate of the input data in Hz\.
This is crucial for digital filter design\.
- **order** (`int`): The order of the Butterworth filter\. Higher
orders provide a steeper rolloff but can be
less stable\. Defaults to 5\.

**Returns:**

- `filtered_data (np.ndarray)`: High-pass filtered data, same shape as input\.

**Raises:**

- **ValueError**: If input data is not a 1D numpy array, or if
cutoff\_freq or sampling\_rate are invalid\.
<a name="oscfar-filters-group_close_peaks"></a>
### 🅵 oscfar\.filters\.group\_close\_peaks

```python
def group_close_peaks(peak_indices, min_distance):
```

Groups peak indices that are close to each other\.

Iterates through sorted peak indices and groups any peaks that are
separated by less than or equal to 'min\_distance' samples\.

**Parameters:**

- **peak_indices** (`list or np.ndarray`): A list or array of peak indices,
assumed to be sorted or will be sorted\.
- **min_distance** (`int`): The maximum distance \(in samples\) between two
consecutive peaks for them to be considered
part of the same group\.

**Returns:**

- `groups (list[list[int]])`: Groups of close peak indices\. Returns an
empty list if no peaks are provided\.
<a name="oscfar-filters-find_representative_peaks"></a>
### 🅵 oscfar\.filters\.find\_representative\_peaks

```python
def find_representative_peaks(data, peak_indices, min_distance):
```

Groups close peaks and returns the index of the maximum peak from each group\.

First, groups peaks that are within 'min\_distance' of each other using
group\_close\_peaks\. Then, for each group, identifies the index
corresponding to the highest value in the 'data' array\.

**Parameters:**

- **data** (`np.ndarray`): The 1D data array \(e\.g\., time series\) where
peak values are found\. Used to determine the max peak\.
- **peak_indices** (`list or np.ndarray`): A list or array of peak indices
to be grouped and processed\.
- **min_distance** (`int`): The maximum distance \(in samples\) between two
consecutive peaks for them to be considered
part of the same group\.

**Returns:**

- `representative_peaks (list[int])`: Index of the maximum peak from each
identified group\. Returns an empty list if no peaks are provided\.
<a name="oscfar-filters-verify_peaks_snr"></a>
### 🅵 oscfar\.filters\.verify\_peaks\_snr

```python
def verify_peaks_snr(data, peak_indices, noise_window_factor = 3, min_snr = 3.0):
```

Verifies peaks based on their local Signal-to-Noise Ratio \(SNR\)\.

Calculates SNR for each peak relative to the noise estimated in
adjacent windows\.

**Parameters:**

- **data** (`np.ndarray`): The 1D data array \(e\.g\., time series\) where
peaks were detected\.
- **peak_indices** (`list or np.ndarray`): Indices of the detected peaks\.
- **noise_window_factor** (`int`): Determines the size and offset
of the noise estimation windows
relative to a conceptual 'peak width'\.
A simple proxy for peak width \(e\.g\., 5 samples\)
is used internally\. The noise windows will
be roughly this size and offset by
this amount from the peak center\.
Defaults to 3\.
- **min_snr** (`float`): The minimum acceptable local SNR for a
peak to be considered verified\. Defaults to 3\.0\.

**Returns:**

- `verified_peaks (list[int])`: Indices corresponding to verified peaks\.

**Raises:**

- **ValueError**: If input data is not a 1D numpy array\.
<a name="oscfar-filters-enforce_min_distance"></a>
### 🅵 oscfar\.filters\.enforce\_min\_distance

```python
def enforce_min_distance(raw_peak_indices, data_values, min_distance):
```

Refines CFAR detections to enforce a minimum distance between peaks\.

**Parameters:**

- **raw_peak_indices**: List of indices where CFAR detected a peak\.
- **data_values**: The original data array \(or SNR array\) used for sorting\.
- **min_distance**: The minimum allowed separation between final peaks \(in indices\)\.

**Returns:**

- `final_peaks_indices (list[int])`: Indices of the final refined peaks\.
<a name="oscfar-filters-filter_peaks_by_extent_1d"></a>
### 🅵 oscfar\.filters\.filter\_peaks\_by\_extent\_1d

```python
def filter_peaks_by_extent_1d(peak_indices, min_extent, max_extent):
```

Filters a list of 1D peak indices, removing peaks that belong to consecutive groups larger than max\_extent\.

**Parameters:**

- **peak_indices** (`list or np.ndarray`): A list or array of integer indices
where peaks were detected by CFAR\.
Assumed to be along a single dimension\.
- **max_extent** (`int`): The maximum allowed number of consecutive indices
for a valid peak group\. Groups larger than this
are considered extended clutter/scattering and removed\.

**Returns:**

- `filtered_peaks (list[int])`: Filtered peak indices belonging to groups
with extent \<= max\_extent\.
<a name="oscfar-filters-moving_average_filter"></a>
### 🅵 oscfar\.filters\.moving\_average\_filter

```python
def moving_average_filter(data, window_size):
```

Applies a simple moving average filter to the 1D data\.

Each point in the output is the average of the 'window\_size' neighboring
points in the input data \(including the point itself\)\. Uses 'same' mode
for convolution, meaning the output array has the same size as the input,
but edge effects might be present where the window doesn't fully overlap\.

**Parameters:**

- **data** (`np.ndarray`): 1D array of input data\.
- **window_size** (`int`): The number of points to include in the averaging
window\. Should be an odd number for a centered average,
but works with even numbers too\. Must be positive\.

**Returns:**

- `filtered_data (np.ndarray)`: Smoothed data array, same shape as input\.

**Raises:**

- **ValueError**: If input data is not a 1D numpy array or if window\_size
is not a positive integer\.
<a name="oscfar-filters-lowess_filter"></a>
### 🅵 oscfar\.filters\.lowess\_filter

```python
def lowess_filter(xdata, ydata, smoothing_factor):
```

Applies a Locally Weighted Scatterplot Smoothing \(LOWESS\) filter to the data\.

LOWESS is a non-parametric regression method that fits simple models to
localized subsets of the data to build up a function that describes the
deterministic part of the variation in the data, point by point\.

**Parameters:**

- **xdata** (`np.ndarray`): 1D array of independent variable values \(e\.g\., time\)\.
- **ydata** (`np.ndarray`): 1D array of dependent variable values \(e\.g\., signal\)\.
Must have the same length as xdata\.
- **smoothing_factor** (`float`): The fraction of the data to use when
estimating the local regression\. Should be
between 0 and 1\. Larger values result in
smoother curves\.

**Returns:**

- `y_smooth (np.ndarray)`: Smoothed y-values corresponding to xdata\.

**Raises:**

- **ValueError**: If xdata or ydata are not 1D numpy arrays, if they have
different lengths, or if smoothing\_factor is not between 0 and 1\.
