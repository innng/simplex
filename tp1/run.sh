#!/bin/bash

if [ -f pivoting.txt ]; then
    rm pivoting.txt;
fi
if [ -f conclusao.txt ]; then
    rm pivoting.txt;
fi
python3 src/main.py src/tableau.py src/simplex.py src/utils.py $1
rm -r src/__pycache__/
