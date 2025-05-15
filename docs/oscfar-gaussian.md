---
title: Fitting
layout: page
parent: Documentation
nav_order: 5
---

<a name="oscfar-gaussian_fit"></a>

## 🅼 oscfar\.gaussian_fit
{: .no_toc }

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-gaussian_fit-sum_of_gaussians"></a>

### 🅵 oscfar\.gaussian_fit\.sum_of_gaussians

```python
def sum_of_gaussians(x, *params):
```

Calculates the sum of multiple Gaussian functions\.

Each Gaussian is defined by its amplitude, mean, and standard deviation\.
The parameters for the Gaussians are provided in a flat list:
\[amp1, mean1, stddev1, amp2, mean2, stddev2, \.\.\., ampN, meanN, stddevN\]

**Parameters:**

-   **x** (`np.array`): The independent variable where the functions are calculated\.
-   **\*params** (`list or np.array`): A variable number of arguments representing the parameters\.
    The total number of parameters must be a multiple of 3\.
-   amp: Amplitude of the Gaussian\.
-   mean: Mean \(center\) of the Gaussian\.
-   stddev: Standard deviation \(width\) of the Gaussian\.

**Returns:**

-   `y (np.array)`: The sum of the Gaussian functions evaluated at x\.

**Raises:**

-   **ValueError**: If the number of parameters in \`params\` is not a multiple of 3\.
    <a name="oscfar-gaussian_fit-sum_of_scattered_gaussians"></a>

### 🅵 oscfar\.gaussian_fit\.sum_of_scattered_gaussians

```python
def sum_of_scattered_gaussians(x, *params):
```

Calculates the sum of multiple scattered Gaussian functions\.

Each scattered Gaussian is defined by its amplitude, mean, standard deviation,
and scattering timescale\. The parameters for the scattered Gaussians are
provided in a flat list:
\[amp1, mean1, sigma1, tau1, amp2, mean2, sigma2, tau2, \.\.\., ampN, meanN, sigmaN, tauN\]

**Parameters:**

-   **x** (`np.array`): The independent variable where the functions are calculated\.
-   **\*params** (`list or np.array`): A variable number of arguments representing the parameters\.
    The total number of parameters must be a multiple of 4\.
-   amp: Amplitude of the scattered Gaussian\.
-   mean: Mean \(center\) of the scattered Gaussian\.
-   sigma: Standard deviation \(width\) of the Gaussian before scattering\.
-   tau: Scattering timescale\.

**Returns:**

-   `y (np.array)`: The sum of the scattered Gaussian functions evaluated at x\.

**Raises:**

-   **ValueError**: If the number of parameters in \`params\` is not a multiple of 4\.
    <a name="oscfar-gaussian_fit-find_best_multi_gaussian_fit"></a>

### 🅵 oscfar\.gaussian_fit\.find_best_multi_gaussian_fit

```python
def find_best_multi_gaussian_fit(x_data, y_data, initial_flat_params, max_n_gaussians = None, y_err = None):
```

Finds the best fit to the data using a sum of Gaussian functions\.

This function attempts to fit the data with a varying number of Gaussian
components, up to a specified maximum\. The best fit is determined by
comparing the Bayesian Information Criterion \(BIC\) for each fit\.

**Parameters:**

-   **x_data** (`np.array`): The independent variable where the data is measured\.
-   **y_data** (`np.array`): The dependent data to be fitted\.
-   **initial_flat_params** (`list or np.array`): A flat list of initial
    parameters for Gaussian
    components, ordered as
    \[amp1, mean1, sigma1, amp2, mean2, sigma2, \.\.\.\]\.
    Amplitudes can be positive or negative\.
-   **max_n_gaussians** (`int`): The maximum number of Gaussian
    components to try\. If None, it defaults
    to the number of components implied by
    \`initial_flat_params\`\.
-   **y_err** (`list or np.array`): Error on y_data\. If provided, it's used in
    \`curve_fit\` for weighted least squares\.

**Returns:**

-   `dict`: A dictionary containing the results of the fitting process\.
    The dictionary has two keys:
-   'best_fit': A dictionary containing the results of the best fit
    found \(lowest BIC\)\. It includes: - 'n_components': The number of Gaussian components
    in the best fit\. - 'popt': The optimized parameters for the best fit\. - 'pcov': The estimated covariance of popt\. - 'bic': The Bayesian Information Criterion \(BIC\) for
    the best fit\. - 'rss': The Residual Sum of Squares for the best fit\.
-   'all_fits': A list of dictionaries, each containing the results
    for a fit with a specific number of components\.
    Each dictionary in the list has the same structure
    as 'best_fit', but for a different number of components\.

**Raises:**

-   **ValueError**: If \`initial_flat_params\` is invalid \(empty or not a multiple of 3\), if \`x_data\` and \`y_data\` are empty or have different lengths\.
    <a name="oscfar-gaussian_fit-find_best_multi_gaussian_fit_combinatorial"></a>

### 🅵 oscfar\.gaussian_fit\.find_best_multi_gaussian_fit_combinatorial

```python
def find_best_multi_gaussian_fit_combinatorial(x_data, y_data, initial_flat_params, max_n_gaussians = None, y_err = None, max_initial_components_for_pool = None, model_to_test = 'gaussian', default_initial_tau = 0.0001, max_tau_bound_factor = 1.0, use_multiprocessing = True, num_processes = None):
```

Performs a grid search to find the best multi-component fit by trying

different numbers of components, different combinations of initial peak
guesses, and optionally different model types \(Gaussian or Scattered Gaussian\)\.

This version supports multiprocessing to speed up the fitting process\.

Args:
\(Same as the single-process version, plus the following:\)
use_multiprocessing \(bool, optional\):
Whether to use multiprocessing\. Defaults to True\.
num_processes \(int, optional\):
The number of processes to use\. If None, uses the number of CPU cores\.

Returns:
\(Same as the single-process version\)

Raises:
\(Same as the single-process version\)
