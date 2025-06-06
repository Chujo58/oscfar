#!/bin/bash
# Define the name of your Conda environment
CONDA_ENV_NAME="base" 

# Attempt to source Conda's shell functions to make 'conda activate' available
_CONDA_ROOT=$(conda info --base)
if [ -f "${_CONDA_ROOT}/etc/profile.d/conda.sh" ]; then
    # shellcheck source=/dev/null
    source "${_CONDA_ROOT}/etc/profile.d/conda.sh"
else
    echo "Error: Conda environment could not be initialized."
    echo "Make sure Conda is installed and 'conda init' has been run for your shell,"
    echo "or that '${_CONDA_ROOT}/etc/profile.d/conda.sh' exists."
    exit 1
fi

# Activate the Conda environment
conda activate "$CONDA_ENV_NAME"
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate Conda environment '$CONDA_ENV_NAME'."
    exit 1
fi
echo "Successfully activated Conda environment: $CONDA_DEFAULT_ENV"
echo "Running commands in Conda environment: $CONDA_DEFAULT_ENV"

cd ..
python -m python_docstring_markdown oscfar oscfar/temp.txt

# Deactivate the environment at the end of the script (good practice)
echo "Deactivating Conda environment: $CONDA_DEFAULT_ENV"
conda deactivate