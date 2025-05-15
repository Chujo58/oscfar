# `oscfar`

<p align=center>
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.8-green.svg"></a>
<a target="_blank" href="https://pypi.org/project/oscfar/" title="PyPI version"><img src="https://img.shields.io/pypi/v/oscfar?logo=pypi"></a>
</p>

OSCFAR (Order Statistic Constant False Alarm Rate) is a radar signal processing technique used for target detection. It adaptively estimates the noise or clutter power in the vicinity of a potential target and sets a detection threshold accordingly, maintaining a constant false alarm rate regardless of the background noise characteristics.

## Getting Started

To get started with the OSCFAR implementation, you'll need to set up your environment. We recommend using Conda for managing dependencies.

### **1. Create a Conda Environment:**

```bash
conda create -n myenv python=3.9  # Or your preferred Python version above 3.9
conda activate myenv
```

### **2. Install OSCFAR Package:**

```bash
pip install oscfar
```

You may need to manually install some packages like `fitburst`. For `fitburst` follow installation instructions on [GitHub](https://github.com/CHIMEFRB/fitburst).
