#!/bin/bash

version=$1
if [ -n "$version" ]; then
    echo "Version provided: $version"
else
    echo "Error: No version provided"
    exit 1
fi

python reload.py $version
python -m build
twine upload dist/*