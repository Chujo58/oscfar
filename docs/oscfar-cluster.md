---
title: Clustering
layout: page
parent: Documentation
nav_order: 4
---

<a name="oscfar-cluster"></a>

## 🅼 oscfar\.cluster
{: .no_toc }

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-cluster-cluster_peaks_p"></a>
### 🅵 oscfar\.cluster\.cluster\_peaks\_p

```python
def cluster_peaks_p(peak_positions, peak_heights, n, max_e = 0.7, verbose = False):
```

Cluster peak positions using DBSCAN and select the most prominent peak from each cluster\.

Parameters

**Parameters:**

- **peak_positions **: array-like, shape \(n\_samples, n\_features\)
The positions of the detected peaks to be clustered\.
- **peak_heights **: array-like, shape \(n\_samples,\)
The heights \(or intensities\) of the detected peaks, used to select the most prominent peak in each cluster\.
- **n **: int
The minimum number of samples in a neighborhood for a point to be considered as a core point in DBSCAN\.
- **max_e **: float, optional \(default=0\.7\)
The maximum distance between two samples for one to be considered as in the neighborhood of the other \(epsilon parameter for DBSCAN\)\.
- **verbose **: bool, optional \(default=False\)
If True, prints the number of clusters found by DBSCAN\.
<a name="oscfar-cluster-cluster_peaks_ph"></a>
### 🅵 oscfar\.cluster\.cluster\_peaks\_ph

```python
def cluster_peaks_ph(peak_positions, peak_heights, n, max_e = 0.7, verbose = False):
```

Clusters peaks based on their positions and heights using DBSCAN\.

**Parameters:**

- **peak_positions** (`list or np.ndarray`): Positions of the peaks\.
- **peak_heights** (`list or np.ndarray`): Heights of the peaks\.
- **n** (`int`): Minimum number of samples in a cluster\.
- **max_e** (`float`): The maximum distance between two samples for
one to be considered as in the neighborhood
of the other\. Defaults to 0\.7\.
- **verbose** (`bool`) (default: `False`): If True, print the number of clusters found\. Defaults to False\.

**Returns:**

- `list`: A list of representative peak positions, one from each cluster\.