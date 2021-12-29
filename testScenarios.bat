@echo off
#!/bin/bash
type initDone.txt

find "false" initDone.txt && (
  echo requirements have not been installed yet
  pip install requirements
  echo requirements installed
  echo true > initDone.txt
  python calculate_test.py
) || (
  python calculate_test.py
)
pause