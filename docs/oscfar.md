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
def do_os_cfar(data: np.ndarray, guard_cells, train_cells, rank_k, threshold_factor, averaging, min_dist, min_snr, baseline, smoothing = 'mean', lowess_frac = 0.01, clustering = False):
```

Performs OS-CFAR detection on 2D data \(spectrogram\), typically summed along

the frequency axis to get a time series, and applies various filtering steps\.

**Parameters:**

- **data** (`np.ndarray`): 2D array of input data \(e\.g\., spectrogram, frequency x time\)\.
Assumed to be in linear power\.
- **guard_cells** (`int`): Number of guard cells on EACH side of the CUT for OS-CFAR\.
- **train_cells** (`int`): Number of training cells on EACH side of the CUT for OS-CFAR\.
- **rank_k** (`float`): The rank \(as a fraction of total training cells\) for OS-CFAR\.
E\.g\., 0\.75 for the 75th percentile\.
- **threshold_factor** (`float`): The scaling factor \(alpha\) for the OS-CFAR threshold\.
- **averaging** (`int`): Window size for the initial smoothing filter \(mean or median\)\.
- **min_dist** (`int`): Minimum distance \(in samples\) between final detected peaks\.
- **min_snr** (`float`): Minimum local SNR required for a peak to be kept\.
- **baseline** (`float`): Secondary threshold factor applied to the mean time series
to remove peaks too close to the baseline\.
- **smoothing** (`str`): Type of initial smoothing to apply to the summed
time series \('mean', 'median', 'lowess', or None\)\.
Defaults to 'mean'\.
- **lowess_frac** (`float`): Fraction of data used for LOWESS smoothing
if smoothing='lowess'\. Defaults to 0\.01\.
- **clustering** (`int or bool`): If an integer \> 0, applies DBSCAN clustering
to the final peaks using this integer as
the 'min\_samples' parameter\. If False or 0,
no clustering is applied\. Defaults to False\.

**Returns:**

- `Peaks`: A Peaks object containing the final detected peak indices and the
original OS-CFAR threshold array\.

**Raises:**

- **TypeError**: If input data is not a 2D NumPy array\.