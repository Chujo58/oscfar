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
### 🅵 oscfar\.do_os_cfar

```python
def do_os_cfar(data: np.array, guard_cells, train_cells, rank_k, threshold_factor, averaging, min_dist, min_snr, baseline):
```

Performs OS-CFAR detection on a 2D data array \(e\.g\., spectrogram\) by summing

along the frequency axis to create a 1D time series\. Applies filtering,
peak refinement, and baseline removal\.

**Parameters:**

-   **data** (`np.ndarray`): 2D array of input data \(frequency vs\. time\)\.
-   **guard_cells** (`int`): Number of guard cells on each side of the CUT\.
-   **train_cells** (`int`): Number of training cells on each side of the CUT\.
-   **rank_k** (`float`): Rank \(as a fraction of total training cells\) for OS\.
-   **threshold_factor** (`float`): Scaling factor for the threshold\.
-   **averaging** (`int`): Window size for moving average smoothing\.
-   **min_dist** (`int`): Minimum distance between peaks \(in samples\)\.
-   **min_snr** (`float`): Minimum SNR for peak verification\.
-   **baseline** (`float`): Factor for removing baseline peaks\.

**Returns:**

-   `utils.Peaks`: An object containing the refined peak indices and the
    threshold array from OS-CFAR\.
