---
title: Clustering
layout: page
nav_order: 4
---

<a name="oscfar-cluster"></a>

## 🅼 oscfar\.cluster

-   **Functions:**
    -   🅵 [cluster_peaks](#oscfar-cluster-cluster_peaks)

### Functions

<a name="oscfar-cluster-cluster_peaks"></a>

### 🅵 oscfar\.cluster\.cluster_peaks

```python
def cluster_peaks(peak_positions, peak_heights, n, max_e = 0.7):
```

Clusters peaks based on their positions and heights using DBSCAN\.

**Parameters:**

-   **peak_positions** (`list or np.ndarray`): Positions of the peaks\.
-   **peak_heights** (`list or np.ndarray`): Heights of the peaks\.
-   **n** (`int`): Minimum number of samples in a cluster\.
-   **max_e** (`float`): The maximum distance between two samples for
    one to be considered as in the neighborhood
    of the other\. Defaults to 0\.7\.

**Returns:**

-   `list`: A list of representative peak positions, one from each cluster\.
