---
title: Utilities
layout: page
parent: Documentation
nav_order: 6
---

<a name="oscfar-utils"></a>
## 🅼 oscfar\.utils

### Functions
{: .no_toc .text-delta }

1. TOC
{:toc}

<a name="oscfar-utils-plot_colormaps"></a>
### 🅵 oscfar\.utils\.plot\_colormaps

```python
def plot_colormaps(gradient, cmap_category, category_name):
```

Plots a list of colormaps\.
<a name="oscfar-utils-get_colormaps"></a>
### 🅵 oscfar\.utils\.get\_colormaps

```python
def get_colormaps():
```

Retrieves and categorizes available matplotlib colormaps, then plots them

by category for visual inspection\.

This function fetches all registered colormaps in matplotlib, categorizes
them based on common usage \(perceptually uniform, sequential, diverging,
qualitative, miscellaneous\), and then uses \`plot\_colormaps\` to display
each category in separate figure windows\.

**Returns:**

- `list[str]`: A sorted list of all available colormap names\.
<a name="oscfar-utils-make_json_serializable"></a>
### 🅵 oscfar\.utils\.make\_json\_serializable

```python
def make_json_serializable(obj):
```

Recursively converts non-JSON serializable objects \(primarily NumPy arrays\)

within a data structure to their JSON serializable equivalents\.

**Parameters:**

- **obj**: The object to convert\. This can be a NumPy array,
a dictionary, a list, or any other JSON serializable type\.

**Returns:**

- A new object with NumPy arrays converted to lists,
suitable for JSON serialization\.

### Classes

<a name="oscfar-utils-NpzReader"></a>
### 🅲 oscfar\.utils\.NpzReader

```python
class NpzReader(DataReader):
```

Class for reading \.npz files containing spectrogram data\.

Inherits from fitburst\.backend\.generic\.DataReader\.

**Attributes:**

- **metadata** (`dict`): Metadata associated with the data\.

**Functions:**

<a name="oscfar-utils-NpzReader-__init__"></a>
#### 🅵 oscfar\.utils\.NpzReader\.\_\_init\_\_

```python
def __init__(self, fname):
```

Initializes the NpzReader with the given file and downsampling factor\.

**Parameters:**

- **fname** (`str`): Path to the \.npz file\.
<a name="oscfar-utils-NpzReader-load_data"></a>
#### 🅵 oscfar\.utils\.NpzReader\.load\_data

```python
def load_data(self):
```

Load data from a generic \.npz file and close the handle promptly\.
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
class NpzWriter(NpzReader):
```

Class for writing and manipulating \.npz files containing spectrogram data\.

Inherits from NpzReader\.

**Attributes:**

- **burst_parameters** (`dict`): Parameters of the burst, such as amplitude,
dispersion measure, scattering timescale, etc\.
- **metadata** (`dict`): Metadata associated with the data\.
- **dm_index** (`int`): Index for the dispersion measure parameter\.
- **scattering_index** (`int`): Index for the scattering index parameter\.
- **spectral_index** (`int`): Index for the spectral index parameter\.
- **ref_freq** (`float`): Reference frequency for spectral index calculations\.

**Functions:**

<a name="oscfar-utils-NpzWriter-__init__"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.\_\_init\_\_

```python
def __init__(self, file_or_reader = None):
```

Initializes the NpzWriter with the given \.npz file\.

**Parameters:**

- **file_or_reader** (`str or NpzReader`): Path to the \.npz file or NpzReader made for file
<a name="oscfar-utils-NpzWriter-validate_and_format_data"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.validate\_and\_format\_data

```python
def validate_and_format_data(self, data, times, freqs):
```

Validate and format input data, times, and frequencies arrays\.

Ensures that data is a 2D numpy array, times and freqs are 1D numpy arrays,
and that the array dimensions are consistent with each other\.

**Parameters:**

- **data**: Array-like object of shape \(num\_freq, num\_time\) containing the data values\.
- **times**: Array-like object of length num\_time containing time values\.
- **freqs**: Array-like object of length num\_freq containing frequency values\.

**Returns:**

- `- data (np.ndarray)`: 2D numpy array of shape \(num\_freq, num\_time\)
- times \(np\.ndarray\): 1D numpy array of time values
- freqs \(np\.ndarray\): 1D numpy array of frequency values
- num\_freq \(int\): Number of frequencies \(rows in data\)
- num\_time \(int\): Number of time points \(columns in data\)

**Raises:**

- **ValueError**: If data is not 2D, or if times or freqs are not 1D arrays\.
- **AssertionError**: If the length of times does not match data's time dimension,
or if the length of freqs does not match data's frequency dimension\.
<a name="oscfar-utils-NpzWriter-set_data"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.set\_data

```python
def set_data(self, data, times, freqs, time_res, freq_res, bad_chans = []):
```

Sets the data and metadata for a new \.npz file\.

**Parameters:**

- **data** (`np.ndarray`): The spectrogram data \(frequency x time\)\.
- **times** (`np.ndarray`): Array of time values for each time sample\.
- **freqs** (`np.ndarray`): Array of frequency values for each channel\.
- **time_res** (`float`): Time resolution of the data\.
- **freq_res** (`float`): Frequency resolution of the data\.
- **bad_chans** (`list`): List of indices of bad frequency channels\.
Defaults to \[\]\.
<a name="oscfar-utils-NpzWriter-update_data"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.update\_data

```python
def update_data(self, data, times = None, freqs = None, time_res = None, freq_res = None, bad_chans = None):
```

Updates data and metadata for an existing \.npz-backed instance\.

This method is similar to \`\`set\_data\`\` but is only valid when the
writer was initialized from an existing file\.

**Parameters:**

- **data** (`np.ndarray`): The spectrogram data \(frequency x time\)\.
- **times** (`np.ndarray`): Array of time values for each time
sample\. Defaults to existing \`\`self\.times\`\`\.
- **freqs** (`np.ndarray`): Array of frequency values for each
channel\. Defaults to existing \`\`self\.freqs\`\`\.
- **time_res** (`float`): Time resolution\. Defaults to existing
\`\`self\.res\_time\`\`\.
- **freq_res** (`float`): Frequency resolution\. Defaults to
existing \`\`self\.res\_freq\`\`\.
- **bad_chans** (`list`): List of bad channel indices\. Defaults
to existing \`\`self\.metadata\['bad\_chans'\]\`\`\.
<a name="oscfar-utils-NpzWriter-remove_baseline"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.remove\_baseline

```python
def remove_baseline(self, percent, step = 0.05, verbose = False, cutoff = 0.3):
```

Removes baseline from the start and end of the data based on SNR\.

Iteratively reduces the percentage of data considered from the start
and end until the SNR in those regions falls below a cutoff threshold\.
The arrival time parameter in burst\_parameters is adjusted accordingly\.

**Parameters:**

- **percent** (`float`): Initial percentage of data from the start and end
to consider for baseline removal \(between 0 and 1\)\.
- **step** (`float`): The step size by which the percentage is
reduced in each iteration\. Defaults to 0\.05\.
- **verbose** (`bool`): If True, prints intermediate SNR values
and percentages during the process\.
Defaults to False\.
- **cutoff** (`float`): The SNR threshold below which a region
is considered baseline and removed\.
Defaults to 0\.3\.

**Raises:**

- **RuntimeError**: If the NpzWriter is set to create a new file but
data has not been loaded using \.set\_data\(\)\.
<a name="oscfar-utils-NpzWriter-update_burst_parameters"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.update\_burst\_parameters

```python
def update_burst_parameters(self, **kwargs):
```

Updates the burst parameters with the provided keyword arguments\.

**Parameters:**

- ****kwargs**: Keyword arguments representing burst parameters to update\.
Possible keys include:
- 'amplitude': Amplitude of the burst\.
- 'dm': Dispersion measure of the burst\.
- 'scattering\_timescale': Scattering timescale of the burst\.
- 'arrival\_time': Arrival time of the burst\.
- 'burst\_width': Intrinsic width of the burst\.
- 'spectral\_running': Spectral index of the burst\.
<a name="oscfar-utils-NpzWriter-save"></a>
#### 🅵 oscfar\.utils\.NpzWriter\.save

```python
def save(self, new_filepath: str):
```

Saves the processed data and burst parameters to a new \.npz file\.

**Parameters:**

- **new_filepath** (`str`): Path to the new \.npz file where the data
will be saved\.
<a name="oscfar-utils-Peaks"></a>
### 🅲 oscfar\.utils\.Peaks

```python
class Peaks:
```

Class to hold results from OS-CFAR\.

**Attributes:**

- **peaks** (`np.array`): First half of the OS-CFAR results containing the peaks resulting from the algorithm\.
- **threshold** (`np.array`): Second half of the OS-CFAR results containing the threshold used by the algorithm\.

**Functions:**

<a name="oscfar-utils-Peaks-__init__"></a>
#### 🅵 oscfar\.utils\.Peaks\.\_\_init\_\_

```python
def __init__(self, oscfar_result):
```

Initializes the Peaks object with the result from OS-CFAR\.

**Parameters:**

- **oscfar_result** (`tuple`): A tuple containing the detected peak indices
and the threshold array\.
<a name="oscfar-utils-WaterFallImage"></a>
### 🅲 oscfar\.utils\.WaterFallImage

```python
class WaterFallImage:
```

Base class for creating matplotlib figures and axes for waterfall plots\.

Provides basic functionality for changing figure size, showing, and saving plots\.
Intended to be inherited by classes that create specific plot layouts\.

**Attributes:**

- **cmap** (`str`): The default colormap to use for the spectrogram image\.
Defaults to 'gist\_yarg'\.

**Functions:**

<a name="oscfar-utils-WaterFallImage-__init__"></a>
#### 🅵 oscfar\.utils\.WaterFallImage\.\_\_init\_\_

```python
def __init__(self):
```
<a name="oscfar-utils-WaterFallImage-change_size"></a>
#### 🅵 oscfar\.utils\.WaterFallImage\.change\_size

```python
def change_size(self, width, height):
```

Changes the size of the figure containing the axes\.

**Parameters:**

- **width** (`float`): The new width of the figure in inches\.
- **height** (`float`): The new height of the figure in inches\.
<a name="oscfar-utils-WaterFallImage-show"></a>
#### 🅵 oscfar\.utils\.WaterFallImage\.show

```python
def show(self, block = None):
```

Displays the plot\.

**Parameters:**

- **block** (`bool`): Whether to block the execution until the
plot window is closed\. Defaults to None,
which uses the matplotlib default\.
<a name="oscfar-utils-WaterFallImage-save"></a>
#### 🅵 oscfar\.utils\.WaterFallImage\.save

```python
def save(self, fname):
```

Saves the current plot to a file\.

**Parameters:**

- **fname** (`str`): The filename \(including path and extension\) to save the plot to\.
<a name="oscfar-utils-WaterFallAxes"></a>
### 🅲 oscfar\.utils\.WaterFallAxes

```python
class WaterFallAxes(WaterFallImage):
```

Class to create matplotlib axes for a single waterfall plot, including

optional time series and spectrum plots\.

Inherits from WaterFallImage\.

**Attributes:**

- **im** (`matplotlib.axes.Axes`): Axes object for the main spectrogram image\.
- **ts** (`matplotlib.axes.Axes or None`): Axes object for the time series plot,
or None if show\_ts is False\.
- **spec** (`matplotlib.axes.Axes or None`): Axes object for the spectrum plot,
or None if show\_spec is False\.
- **show_ts** (`bool`): Whether the time series plot is included\.
- **show_spec** (`bool`): Whether the spectrum plot is included\.
- **_data** (`NpzReader or None`): Stores the data reader object after plotting\.
- **_time_series** (`np.ndarray or None`): Stores the summed time series after plotting\.
- **_freq_series** (`np.ndarray or None`): Stores the summed frequency series after plotting\.

**Functions:**

<a name="oscfar-utils-WaterFallAxes-__init__"></a>
#### 🅵 oscfar\.utils\.WaterFallAxes\.\_\_init\_\_

```python
def __init__(self, width: float = 0.75, height: float = 0.75, bottom: float = 0.1, left: float = None, hratio: float = 1, vratio: float = 1, show_ts = True, show_spec = True, labels_on = [True, True]):
```

Initializes the WaterFallAxes object\.

**Parameters:**

- **width** (`float`) (default: `0.75`): Width of the main spectrogram plot\. Defaults to 0\.75\.
- **height** (`float`) (default: `0.75`): Height of the main spectrogram plot\. Defaults to 0\.75\.
- **bottom** (`float`): Bottom position of the main spectrogram plot\.
- **left** (`float`): Left position of the main spectrogram plot\.
Defaults to the value of 'bottom'\.
- **hratio** (`float`) (default: `1`): Horizontal ratio for plot dimensions\. Defaults to 1\.
- **vratio** (`float`) (default: `1`): Vertical ratio for plot dimensions\. Defaults to 1\.
- **show_ts** (`bool`) (default: `True`): Whether to show the time series plot\. Defaults to True\.
- **show_spec** (`bool`) (default: `True`): Whether to show the spectrum plot\. Defaults to True\.
- **labels_on** (`list`): List of two booleans indicating whether to
show labels on the x and y axes, respectively\.
Defaults to \[True, True\]\.
<a name="oscfar-utils-WaterFallAxes-plot"></a>
#### 🅵 oscfar\.utils\.WaterFallAxes\.plot

```python
def plot(self, data: NpzReader, title = '', readjust_title = 0):
```

Plots the spectrogram, time series, and spectrum on the created axes\.

**Parameters:**

- **data** (`NpzReader`): DataReader object containing the spectrogram data\.
- **title** (`str`) (default: `""`): Title of the plot\. Defaults to ""\.
- **readjust_title** (`int`) (default: `0`): Vertical adjustment for the title position\. Defaults to 0\.
<a name="oscfar-utils-WaterFallAxes-plot_time_peaks"></a>
#### 🅵 oscfar\.utils\.WaterFallAxes\.plot\_time\_peaks

```python
def plot_time_peaks(self, peaks: Peaks, color, show_thres = False):
```

Plots vertical lines on the spectrogram at the time indices of the detected peaks\.

Also plots the peaks on the time series plot if it is shown\.

**Parameters:**

- **peaks** (`Peaks`): An object containing the peak indices and threshold\.
- **color** (`str`): Color for the vertical lines and scatter points\.
- **show_thres** (`bool`): Whether to show the threshold on the time series plot\.
<a name="oscfar-utils-WaterFallGrid"></a>
### 🅲 oscfar\.utils\.WaterFallGrid

```python
class WaterFallGrid(WaterFallImage):
```

Class to create a grid of waterfall plots \(spectrograms\) with associated time series and spectra\.

Inherits from WaterFallImage\.

**Attributes:**

- **nrows** (`int`): Number of rows in the grid\.
- **ncols** (`int`): Number of columns in the grid\.
- **axes** (`np.ndarray`): A 2D array of WaterFallAxes objects, representing
each subplot in the grid\.
- **vs** (`float`): Vertical spacing between plots\.
- **hs** (`float`): Horizontal spacing between plots\.

**Functions:**

<a name="oscfar-utils-WaterFallGrid-__init__"></a>
#### 🅵 oscfar\.utils\.WaterFallGrid\.\_\_init\_\_

```python
def __init__(self, nrows: int, ncols: int, vspacing = 0.1, hspacing = 0.1):
```

Initializes the WaterFallGrid object\.

**Parameters:**

- **nrows** (`int`): Number of rows in the grid\.
- **ncols** (`int`): Number of columns in the grid\.
- **vspacing** (`float`) (default: `0.1`): Vertical spacing between plots\. Defaults to 0\.1\.
- **hspacing** (`float`) (default: `0.1`): Horizontal spacing between plots\. Defaults to 0\.1\.
<a name="oscfar-utils-WaterFallGrid-plot"></a>
#### 🅵 oscfar\.utils\.WaterFallGrid\.plot

```python
def plot(self, data: list, peaks: list, titles: list, color, labels = [True, False], adjust_t = 0, show_thres = False):
```

Plots the waterfall grid with the provided data, peaks, and titles\.

**Parameters:**

- **data** (`list`): List of DataReader objects, one for each subplot\.
- **peaks** (`list`): List of Peaks objects, one for each subplot\.
- **titles** (`list`): List of titles for each subplot\.
- **color** (`str`): Color for the peak markers\.
- **labels** (`list`): List of two booleans indicating whether to
show labels on the x and y axes, respectively\.
Defaults to \[True, False\]\.
- **adjust_t** (`int`) (default: `0`): Vertical adjustment for the title position\. Defaults to 0\.
- **show_thres** (`bool`): Whether to show the threshold on the time series plot\.
<a name="oscfar-utils-WaterFallGrid-add_info"></a>
#### 🅵 oscfar\.utils\.WaterFallGrid\.add\_info

```python
def add_info(self, info: pd.DataFrame):
```

Adds a table with additional information below the grid\.

**Parameters:**

- **info** (`pd.DataFrame`): DataFrame containing the information to be displayed\.
<a name="oscfar-utils-FitburstResultsReader"></a>
### 🅲 oscfar\.utils\.FitburstResultsReader

```python
class FitburstResultsReader:
```

Class to read and access results from a fitburst JSON output file\.

**Attributes:**

- **filepath** (`str`): Path to the fitburst JSON results file\.
- **results** (`dict`): Dictionary containing the loaded JSON data\.
- **initial_dm** (`float`): Initial DM used in the fit\.
- **initial_time** (`float`): Initial time used in the fit\.
- **(various attributes)**: Attributes corresponding to keys in the
'fit\_statistics' section of the JSON,
including best-fit parameters and their
uncertainties as \`uncertainties\.ufloat\` objects\.

**Functions:**

<a name="oscfar-utils-FitburstResultsReader-__init__"></a>
#### 🅵 oscfar\.utils\.FitburstResultsReader\.\_\_init\_\_

```python
def __init__(self, filepath: str):
```

Initializes the FitburstResultsReader with the path to the JSON results file\.

**Parameters:**

- **filepath** (`str`): Path to the JSON file containing fitburst results\.
<a name="oscfar-utils-FitburstResultsReader-get_fit_statistics"></a>
#### 🅵 oscfar\.utils\.FitburstResultsReader\.get\_fit\_statistics

```python
def get_fit_statistics(self):
```

Returns the 'fit\_statistics' section of the fitburst results\.

**Returns:**

- `dict`: A dictionary containing fit statistics\.
<a name="oscfar-utils-FitburstResultsReader-get_model_parameters"></a>
#### 🅵 oscfar\.utils\.FitburstResultsReader\.get\_model\_parameters

```python
def get_model_parameters(self):
```

Returns the 'model\_parameters' section of the fitburst results\.

**Returns:**

- `dict`: A dictionary containing model parameters\.
<a name="oscfar-utils-FitburstResultsReader-get_fit_logistics"></a>
#### 🅵 oscfar\.utils\.FitburstResultsReader\.get\_fit\_logistics

```python
def get_fit_logistics(self):
```

Returns the 'fit\_logistics' section of the fitburst results\.

**Returns:**

- `dict`: A dictionary containing fit logistics\.
<a name="oscfar-utils-FitburstResultsWriter"></a>
### 🅲 oscfar\.utils\.FitburstResultsWriter

```python
class FitburstResultsWriter:
```

Class to write and save results from a fitburst LSFitter object to a JSON file\.

**Attributes:**

- **info** (`LSFitter`): The LSFitter object containing the fit results\.

**Functions:**

<a name="oscfar-utils-FitburstResultsWriter-__init__"></a>
#### 🅵 oscfar\.utils\.FitburstResultsWriter\.\_\_init\_\_

```python
def __init__(self, info: LSFitter):
```

Initializes the FitburstResultsWriter with an LSFitter object\.

**Parameters:**

- **info** (`LSFitter`): An instance of the LSFitter class containing the
results of a fitburst analysis\.
<a name="oscfar-utils-FitburstResultsWriter-get_fit_statistics"></a>
#### 🅵 oscfar\.utils\.FitburstResultsWriter\.get\_fit\_statistics

```python
def get_fit_statistics(self):
```

Returns the 'fit\_statistics' section from the LSFitter object\.

**Returns:**

- `dict`: A dictionary containing fit statistics\.
<a name="oscfar-utils-FitburstResultsWriter-get_model_parameters"></a>
#### 🅵 oscfar\.utils\.FitburstResultsWriter\.get\_model\_parameters

```python
def get_model_parameters(self):
```

Returns the 'model\_parameters' section from the LSFitter object's model\.

**Returns:**

- `dict`: A dictionary containing model parameters\.
<a name="oscfar-utils-FitburstResultsWriter-get_fit_logistics"></a>
#### 🅵 oscfar\.utils\.FitburstResultsWriter\.get\_fit\_logistics

```python
def get_fit_logistics(self):
```

Returns the 'fit\_logistics' section from the LSFitter object\.

**Returns:**

- `dict`: A dictionary containing fit logistics\.
<a name="oscfar-utils-FitburstResultsWriter-save"></a>
#### 🅵 oscfar\.utils\.FitburstResultsWriter\.save

```python
def save(self, filepath: str):
```

Saves the fitburst results to a JSON file\.

**Parameters:**

- **filepath** (`str`): The path to the JSON file where the results will be saved\.
