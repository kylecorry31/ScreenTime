#!/bin/bash

# This archives the file
while [[ true ]]; do
  python3 same_week.py $(head -n1 test.txt) $@
done
