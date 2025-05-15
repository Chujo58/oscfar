---
title: Utilities
layout: page
nav_order: 7
---

<a name="oscfar-utils"></a>

## 🅼 oscfar\.utils

-   **Classes:**
    -   🅲 [NpzReader](#oscfar-utils-NpzReader)
    -   🅲 [NpzWriter](#oscfar-utils-NpzWriter)
    -   🅲 [Peaks](#oscfar-utils-Peaks)
    -   🅲 [WaterFallAxes](#oscfar-utils-WaterFallAxes)
    -   🅲 [WaterFallGrid](#oscfar-utils-WaterFallGrid)

### Classes

<a name="oscfar-utils-NpzReader"></a>

### 🅲 oscfar\.utils\.NpzReader

```python
class NpzReader(DataReader):
```

Class for reading \.npz files containing spectrogram data\.

Inherits from fitburst\.backend\.generic\.DataReader\.

**Attributes:**

-   **metadata** (`dict`): Metadata associated with the data\.
-   **downsampling_factor** (`int`): Factor by which the data has been downsampled\.

**Functions:**

<a name="oscfar-utils-NpzReader-__init__"></a>

#### 🅵 oscfar\.utils\.NpzReader\.\_\_init\_\_

```python
def __init__(self, fname, factor):
```

Initializes the NpzReader with the given file and downsampling factor\.

**Parameters:**

-   **fname** (`str`): Path to the \.npz file\.
-   **factor** (`int`): Downsampling factor applied to the data\.
    <a name="oscfar-utils-NpzReader-__repr__"></a>

#### 🅵 oscfar\.utils\.NpzReader\.\_\_repr\_\_

```python
def __repr__(self):
```

Returns a string representation of the NpzReader object\.
<a name="oscfar-utils-NpzReader-__str__"></a>

#### 🅵 oscfar\.utils\.NpzReader\.\_\_str\_\_

```python
def __str__(self):
```

Returns a string representation of the NpzReader object\.
<a name="oscfar-utils-NpzWriter"></a>

### 🅲 oscfar\.utils\.NpzWriter

```python
class NpzWriter:
```

Class for writing data to \.npz files, typically after processing\.

**Attributes:**

-   **reader** (`NpzReader`): An instance of NpzReader containing the original data\.
-   **burst_parameters** (`dict`): Dictionary of burst parameters to be saved\.

**Functions:**

<a name="oscfar-utils-NpzWriter-__init__"></a>

#### 🅵 oscfar\.utils\.NpzWriter\.\_\_init\_\_

```python
def __init__(self, original_data: NpzReader):
```

Initializes the NpzWriter with the given NpzReader instance\.

**Parameters:**

-   **original_data** (`NpzReader`): An instance of NpzReader containing the
    original data to be processed and saved\.
    <a name="oscfar-utils-NpzWriter-update_burst_parameters"></a>

#### 🅵 oscfar\.utils\.NpzWriter\.update_burst_parameters

```python
def update_burst_parameters(self, **kwargs):
```

Updates the burst parameters with the provided keyword arguments\.

**Parameters:**

-   \***\*kwargs**: Keyword arguments representing burst parameters to update\.
    Possible keys include:
-   'amplitude': Amplitude of the burst\.
-   'dm': Dispersion measure of the burst\.
-   'scattering_timescale': Scattering timescale of the burst\.
-   'arrival_time': Arrival time of the burst\.
-   'burst_width': Intrinsic width of the burst\.
-   'spectral_running': Spectral index of the burst\.
    <a name="oscfar-utils-NpzWriter-save"></a>

#### 🅵 oscfar\.utils\.NpzWriter\.save

```python
def save(self, new_filepath: str):
```

Saves the processed data and burst parameters to a new \.npz file\.

**Parameters:**

-   **new_filepath** (`str`): Path to the new \.npz file where the data
    will be saved\.
    <a name="oscfar-utils-Peaks"></a>

### 🅲 oscfar\.utils\.Peaks

```python
class Peaks:
```

Class to hold results from OS-CFAR\.

**Attributes:**

-   **peaks** (`np.array`): First half of the OS-CFAR results containing the peaks resulting from the algorithm\.
-   **threshold** (`np.array`): Second half of the OS-CFAR results containing the threshold used by the algorithm\.

**Functions:**

<a name="oscfar-utils-Peaks-__init__"></a>

#### 🅵 oscfar\.utils\.Peaks\.\_\_init\_\_

```python
def __init__(self, oscfar_result):
```

Initializes the Peaks object with the result from OS-CFAR\.

**Parameters:**

-   **oscfar_result** (`tuple`): A tuple containing the detected peak indices
    and the threshold array\.
    <a name="oscfar-utils-WaterFallAxes"></a>

### 🅲 oscfar\.utils\.WaterFallAxes

```python
class WaterFallAxes:
```

Class to create axes for waterfall plots \(spectrograms\)\.

**Attributes:**

-   **\_data** (`DataReader`): DataReader object containing the spectrogram data\.
-   **show_ts** (`bool`): Whether to show the time series plot\.
-   **show_spec** (`bool`): Whether to show the spectrum plot\.
-   **im** (`matplotlib.axes._subplots.AxesSubplot`): Axes for the spectrogram\.
-   **ts** (`matplotlib.axes._subplots.AxesSubplot`): Axes for the time series plot\.
-   **spec** (`matplotlib.axes._subplots.AxesSubplot`): Axes for the spectrum plot\.
-   **time_series** (`np.ndarray`): Time series data \(sum over frequencies\)\.
-   **freq_series** (`np.ndarray`): Frequency series data \(sum over time\)\.

**Functions:**

<a name="oscfar-utils-WaterFallAxes-__init__"></a>

#### 🅵 oscfar\.utils\.WaterFallAxes\.\_\_init\_\_

```python
def __init__(self, data: DataReader, width: float, height: float, bottom: float, left: float = None, hratio: float = 1, vratio: float = 1, show_ts = True, show_spec = True, labels_on = [True, True], title = '', readjust_title = 0):
```

Initializes the WaterFallAxes object\.

**Parameters:**

-   **data** (`DataReader`): DataReader object containing the spectrogram data\.
-   **width** (`float`): Width of the main spectrogram plot\.
-   **height** (`float`): Height of the main spectrogram plot\.
-   **bottom** (`float`): Bottom position of the main spectrogram plot\.
-   **left** (`float`): Left position of the main spectrogram plot\.
    Defaults to the value of 'bottom'\.
-   **hratio** (`float`) (default: `1`): Horizontal ratio for plot dimensions\. Defaults to 1\.
-   **vratio** (`float`) (default: `1`): Vertical ratio for plot dimensions\. Defaults to 1\.
-   **show_ts** (`bool`) (default: `True`): Whether to show the time series plot\. Defaults to True\.
-   **show_spec** (`bool`) (default: `True`): Whether to show the spectrum plot\. Defaults to True\.
-   **labels_on** (`list`): List of two booleans indicating whether to
    show labels on the x and y axes, respectively\.
    Defaults to \[True, True\]\.
-   **title** (`str`) (default: `""`): Title of the plot\. Defaults to ""\.
-   **readjust_title** (`int`) (default: `0`): Vertical adjustment for the title position\. Defaults to 0\.
    <a name="oscfar-utils-WaterFallAxes-plot"></a>

#### 🅵 oscfar\.utils\.WaterFallAxes\.plot

```python
def plot(self):
```

Plots the spectrogram\.
<a name="oscfar-utils-WaterFallAxes-plot_time_peaks"></a>

#### 🅵 oscfar\.utils\.WaterFallAxes\.plot_time_peaks

```python
def plot_time_peaks(self, peaks: Peaks, color, show_thres = False):
```

Plots vertical lines on the spectrogram at the time indices of the detected peaks\.

Also plots the peaks on the time series plot if it is shown\.

**Parameters:**

-   **peaks** (`Peaks`): An object containing the peak indices and threshold\.
-   **color** (`str`): Color for the vertical lines and scatter points\.
-   **show_thres** (`bool`): Whether to show the threshold on the time series plot\.
    <a name="oscfar-utils-WaterFallGrid"></a>

### 🅲 oscfar\.utils\.WaterFallGrid

```python
class WaterFallGrid:
```

Class to create a grid of waterfall plots \(spectrograms\)\.

**Attributes:**

-   **nrows** (`int`): Number of rows in the grid\.
-   **ncols** (`int`): Number of columns in the grid\.
-   **axes** (`np.ndarray`): 2D array of WaterFallAxes objects representing the grid\.
-   **vs** (`float`): Vertical spacing between plots\.
-   **hs** (`float`): Horizontal spacing between plots\.

**Functions:**

<a name="oscfar-utils-WaterFallGrid-__init__"></a>

#### 🅵 oscfar\.utils\.WaterFallGrid\.\_\_init\_\_

```python
def __init__(self, nrows: int, ncols: int, vspacing = 0.1, hspacing = 0.1):
```

Initializes the WaterFallGrid object\.

**Parameters:**

-   **nrows** (`int`): Number of rows in the grid\.
-   **ncols** (`int`): Number of columns in the grid\.
-   **vspacing** (`float`) (default: `0.1`): Vertical spacing between plots\. Defaults to 0\.1\.
-   **hspacing** (`float`) (default: `0.1`): Horizontal spacing between plots\. Defaults to 0\.1\.
    <a name="oscfar-utils-WaterFallGrid-plot"></a>

#### 🅵 oscfar\.utils\.WaterFallGrid\.plot

```python
def plot(self, data: list, peaks: list, titles: list, color, labels = [True, False], adjust_t = 0, show_thres = False):
```

Plots the waterfall grid with the provided data, peaks, and titles\.

**Parameters:**

-   **data** (`list`): List of DataReader objects, one for each subplot\.
-   **peaks** (`list`): List of Peaks objects, one for each subplot\.
-   **titles** (`list`): List of titles for each subplot\.
-   **color** (`str`): Color for the peak markers\.
-   **labels** (`list`): List of two booleans indicating whether to
    show labels on the x and y axes, respectively\.
    Defaults to \[True, False\]\.
-   **adjust_t** (`int`) (default: `0`): Vertical adjustment for the title position\. Defaults to 0\.
-   **show_thres** (`bool`): Whether to show the threshold on the time series plot\.
    <a name="oscfar-utils-WaterFallGrid-add_info"></a>

#### 🅵 oscfar\.utils\.WaterFallGrid\.add_info

```python
def add_info(self, info: pd.DataFrame):
```

Adds a table with additional information below the grid\.

**Parameters:**

-   **info** (`pd.DataFrame`): DataFrame containing the information to be displayed\.
