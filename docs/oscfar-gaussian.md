---
title: Fitting
layout: page
parent: Documentation
nav_order: 5
---

<a name="oscfar-gaussian_fit"></a>
## 🅼 oscfar\.gaussian\_fit

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-gaussian_fit-sum_of_gaussians"></a>
### 🅵 oscfar\.gaussian\_fit\.sum\_of\_gaussians

```python
def sum_of_gaussians(x, *params):
```

Calculates the sum of multiple Gaussian functions\.

Each Gaussian is defined by its amplitude, mean, and standard deviation\.
The parameters for the Gaussians are provided in a flat list:
\[amp1, mean1, stddev1, amp2, mean2, stddev2, \.\.\., ampN, meanN, stddevN\]

**Parameters:**

- **x** (`np.array`): The independent variable where the functions are calculated\.
- ***params** (`list or np.array`): A variable number of arguments representing the parameters\.
The total number of parameters must be a multiple of 3\.
- amp: Amplitude of the Gaussian\.
- mean: Mean \(center\) of the Gaussian\.
- stddev: Standard deviation \(width\) of the Gaussian\.

**Returns:**

- `y (np.ndarray)`: The sum of the Gaussian functions evaluated at x\.

**Raises:**

- **ValueError**: If the number of parameters in \`params\` is not a multiple of 3\.
<a name="oscfar-gaussian_fit-sum_of_scattered_gaussians"></a>
### 🅵 oscfar\.gaussian\_fit\.sum\_of\_scattered\_gaussians

```python
def sum_of_scattered_gaussians(x, *params):
```

Calculates the sum of multiple scattered Gaussian functions\.

Each scattered Gaussian is defined by its amplitude, mean, standard deviation,
and scattering timescale\. The parameters for the scattered Gaussians are
provided in a flat list:
\[amp1, mean1, sigma1, tau1, amp2, mean2, sigma2, tau2, \.\.\., ampN, meanN, sigmaN, tauN\]

**Parameters:**

- **x** (`np.array`): The independent variable where the functions are calculated\.
- ***params** (`list or np.array`): A variable number of arguments representing the parameters\.
The total number of parameters must be a multiple of 4\.
- amp: Amplitude of the scattered Gaussian\.
- mean: Mean \(center\) of the scattered Gaussian\.
- sigma: Standard deviation \(width\) of the Gaussian before scattering\.
- tau: Scattering timescale\.

**Returns:**

- `y (np.ndarray)`: The sum of the scattered Gaussian functions evaluated at x\.

**Raises:**

- **ValueError**: If the number of parameters in \`params\` is not a multiple of 4\.
<a name="oscfar-gaussian_fit-find_best_multi_gaussian_fit"></a>
### 🅵 oscfar\.gaussian\_fit\.find\_best\_multi\_gaussian\_fit

```python
def find_best_multi_gaussian_fit(x_data, y_data, initial_flat_params, max_n_gaussians = None, y_err = None):
```

Finds the best fit to the data using a sum of Gaussian functions\.

This function attempts to fit the data with a varying number of Gaussian
components, up to a specified maximum\. The best fit is determined by
comparing the Bayesian Information Criterion \(BIC\) for each fit\.

**Parameters:**

- **x_data** (`np.array`): The independent variable where the data is measured\.
- **y_data** (`np.array`): The dependent data to be fitted\.
- **initial_flat_params** (`list or np.array`): A flat list of initial
parameters for Gaussian
components, ordered as
\[amp1, mean1, sigma1, amp2, mean2, sigma2, \.\.\.\]\.
Amplitudes can be positive or negative\.
- **max_n_gaussians** (`int`): The maximum number of Gaussian
components to try\. If None, it defaults
to the number of components implied by
\`initial\_flat\_params\`\.
- **y_err** (`list or np.array`): Error on y\_data\. If provided, it's used in
\`curve\_fit\` for weighted least squares\.

**Returns:**

- `fit_results (dict)`: Fitting results with keys:
- 'best\_fit': Results for the best model \(lowest BIC\), including
    'n\_components', 'popt', 'pcov', 'bic', and 'rss'\.
- 'all\_fits': Results for all attempted component counts\.

**Raises:**

- **ValueError**: If \`initial\_flat\_params\` is invalid \(empty or not a multiple of 3\), if \`x\_data\` and \`y\_data\` are empty or have different lengths\.
<a name="oscfar-gaussian_fit-find_best_multi_gaussian_fit_combinatorial"></a>
### 🅵 oscfar\.gaussian\_fit\.find\_best\_multi\_gaussian\_fit\_combinatorial

```python
def find_best_multi_gaussian_fit_combinatorial(x_data, y_data, initial_flat_params, max_n_gaussians = None, y_err = None, max_initial_components_for_pool = None, model_to_test = 'gaussian', default_initial_tau = 0.0001, max_tau_bound_factor = 1.0, use_multiprocessing = True, num_processes = None):
```

Performs a grid search to find the best multi-component fit by trying

different numbers of components, different combinations of initial peak
guesses, and optionally different model types \(Gaussian or Scattered Gaussian\)\.

This version supports multiprocessing to speed up the fitting process\.

Args:
    \(Same as the single-process version, plus the following:\)
    use\_multiprocessing \(bool, optional\):
        Whether to use multiprocessing\. Defaults to True\.
    num\_processes \(int, optional\):
        The number of processes to use\. If None, uses the number of CPU cores\.

Returns:
    fit\_results \(dict\): Same structure as \`\_process\_model\_fit\`, containing
        best-fit and all-fit results for the selected model\(s\)\.

Raises:
    \(Same as the single-process version\)
<a name="oscfar-generate_docs"></a>
## 🅼 oscfar\.generate\_docs

- **Constants:**
  - 🆅 [MODULE\_ORDER](#oscfar-generate_docs-MODULE_ORDER)
  - 🆅 [DOC\_TARGETS](#oscfar-generate_docs-DOC_TARGETS)
- **Functions:**
  - 🅵 [parse\_args](#oscfar-generate_docs-parse_args)
  - 🅵 [find\_anchor\_block](#oscfar-generate_docs-find_anchor_block)
  - 🅵 [normalize\_module\_block](#oscfar-generate_docs-normalize_module_block)
  - 🅵 [get\_existing\_front\_matter](#oscfar-generate_docs-get_existing_front_matter)
  - 🅵 [default\_front\_matter](#oscfar-generate_docs-default_front_matter)
  - 🅵 [write\_module\_docs](#oscfar-generate_docs-write_module_docs)
  - 🅵 [main](#oscfar-generate_docs-main)

### Constants

<a name="oscfar-generate_docs-MODULE_ORDER"></a>
### 🆅 oscfar\.generate\_docs\.MODULE\_ORDER

```python
MODULE_ORDER = ['oscfar', 'oscfar-cfar', 'oscfar-cluster', 'oscfar-filters', 'oscfar-gaussian_fit', 'oscfar-reload', 'oscfar-setup', 'oscfar-utils']
```
<a name="oscfar-generate_docs-DOC_TARGETS"></a>
### 🆅 oscfar\.generate\_docs\.DOC\_TARGETS

```python
DOC_TARGETS = {'oscfar': {'file': 'oscfar.md', 'title': 'General functions', 'nav_order': 1}, 'oscfar-cfar': {'file': 'oscfar-cfar.md', 'title': 'CFAR Algorithms', 'nav_order': 2}, 'oscfar-filters': {'file': 'oscfar-filters.md', 'title': 'Filtering', 'nav_order': 3}, 'oscfar-cluster': {'file': 'oscfar-cluster.md', 'title': 'Clustering', 'nav_order': 4}, 'oscfar-gaussian_fit': {'file': 'oscfar-gaussian.md', 'title': 'Fitting', 'nav_order': 5}, 'oscfar-utils': {'file': 'oscfar-utils.md', 'title': 'Utilities', 'nav_order': 6}}
```

### Functions

<a name="oscfar-generate_docs-parse_args"></a>
### 🅵 oscfar\.generate\_docs\.parse\_args

```python
def parse_args() -> argparse.Namespace:
```
<a name="oscfar-generate_docs-find_anchor_block"></a>
### 🅵 oscfar\.generate\_docs\.find\_anchor\_block

```python
def find_anchor_block(content: str, anchor: str, anchor_positions: dict[str, int]) -> str:
```
<a name="oscfar-generate_docs-normalize_module_block"></a>
### 🅵 oscfar\.generate\_docs\.normalize\_module\_block

```python
def normalize_module_block(block: str) -> str:
```
<a name="oscfar-generate_docs-get_existing_front_matter"></a>
### 🅵 oscfar\.generate\_docs\.get\_existing\_front\_matter

```python
def get_existing_front_matter(path: Path) -> str | None:
```
<a name="oscfar-generate_docs-default_front_matter"></a>
### 🅵 oscfar\.generate\_docs\.default\_front\_matter

```python
def default_front_matter(title: str, nav_order: int) -> str:
```
<a name="oscfar-generate_docs-write_module_docs"></a>
### 🅵 oscfar\.generate\_docs\.write\_module\_docs

```python
def write_module_docs(content: str, docs_dir: Path) -> None:
```
<a name="oscfar-generate_docs-main"></a>
### 🅵 oscfar\.generate\_docs\.main

```python
def main() -> None:
```
