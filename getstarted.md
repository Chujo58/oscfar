---
title: Getting Started
layout: page
nav_order: 2
---

# Getting Started
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Installing with `pip`
### With `conda` environments
To get started with the OSCFAR implementation, you'll need to set up your environment. We recommend using Conda for managing dependencies.

#### **1. Create a Conda Environment:**
{: .no_toc }

```bash
conda create -n myenv python=3.9  # Or your preferred Python version above 3.9
conda activate myenv
```

#### **2. Install OSCFAR Package:**
{: .no_toc }

```bash
pip install oscfar
```

### With a local python distribution
If you are using your default python installation to install this package, you first need to verify the Python version installed:
```bash
python --version #or python3
```

If the version printed out is greater or equal to Python 3.8, you can do the next step to pip install the package.

```bash
pip install oscfar
```

### Testing the installation
This is valid for either a conda or a local Python installation. 
```bash
python #or python3
>>> import oscfar
```
If you get an error mentioning the `DataReader` object from `fitburst`, you are missing one last dependency that needs to be installed by hand.

## Installing `fitburst`
To install `fitburst`, follow installation instructions on [GitHub](https://github.com/CHIMEFRB/fitburst).

## Upgrading the package
Since this package isn't final, you may run into issues (which can be reported on [GitHub](https://github.com/chujo58/oscfar/issues)). We will try to fix them as soon as possible. If you notice a version change between your installation and the PyPI distribution, you can upgrade the package with:
```bash
pip install oscfar --upgrade
```

To verify your local installation, run:
```bash
python
>>> import oscfar
>>> oscfar.__version__
```