#!/bin/bash

python -m build > /dev/null 2> /dev/null
pip install --force-reinstall dist/dsa-0.0.1-*.whl  > /dev/null 2> /dev/null
python -m "dsa.$1"