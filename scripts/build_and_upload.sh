#!/bin/bash

python3 -m pip install --upgrade build twine

# Build the package
python3 -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

