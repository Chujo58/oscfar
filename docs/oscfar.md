---
title: General functions
layout: page
parent: Documentation
nav_order: 1
---

<a name="oscfar"></a>

## 🅼 oscfar
{: .no_toc }

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}


<a name="oscfar-do_os_cfar"></a>
### 🅵 oscfar\.do\_os\_cfar

```python
def do_os_cfar(data: np.ndarray, guard_cells, train_cells, rank_k, threshold_factor, averaging, min_dist, min_snr, baseline, smoothing = 'mean', lowess_frac = 0.01, clustering = False, clustering_cutoff = 0.7):
```

Perform OS-CFAR detection and post-processing on 2D array data\.

This function applies Ordered Statistics CFAR \(OS-CFAR\) detection to a 2D input array
\(e\.g\., a spectrogram\), typically by summing along one axis to produce a 1D time series\.
It then applies smoothing, peak detection, SNR filtering, baseline removal, and optional clustering\.

**Parameters:**

- **data** (`np.ndarray`): 2D input array \(e\.g\., frequency x time\), assumed to be linear power\.
- **guard_cells** (`int`): Number of guard cells on each side of the cell under test \(CUT\)\.
- **train_cells** (`int`): Number of training cells on each side of the CUT\.
- **rank_k** (`float`): Fraction \(0-1\) of training cells to use for the OS-CFAR rank \(e\.g\., 0\.75 for 75th percentile\)\.
- **threshold_factor** (`float`): Scaling factor \(alpha\) for the OS-CFAR threshold\.
- **averaging** (`int`): Window size for initial smoothing \(mean or median\)\.
- **min_dist** (`int`): Minimum distance \(in samples\) between detected peaks\.
- **min_snr** (`float`): Minimum SNR required for a peak to be kept\.
- **baseline** (`float`): Threshold factor for removing peaks close to the baseline\.
- **smoothing** (`str`): Smoothing method for the time series \('mean', 'median', 'lowess', or None\)\. Default is 'mean'\.
- **lowess_frac** (`float`): Fraction of data for LOWESS smoothing if used\. Default is 0\.01\.
- **clustering** (`int or bool`): If int \> 0, applies DBSCAN clustering to peaks with this as min\_samples\. Default is False\.
- **clustering_cutoff** (`float`): Cutoff value for clustering\. Default is 0\.7\.

**Returns:**

- `Peaks`: Peaks object containing detected peak indices and the OS-CFAR threshold array\.

**Raises:**

- **TypeError**: If input data is not a 2D NumPy array\.