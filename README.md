# PythonHelpers
Often needed things with python3

- replace.py 
  In the current directory and all its subdirectories, in files ending in any of the suffixes: replace stringOld by stringNew.
  
  Example:
  ```python
  python3 ~/Dropbox/Apu/replace.py --stringOld ".example" --stringNew ".tinyYolo3lFloat32" --suffixes [".py", ".md"]
  ```
  1) Repalcement is done in all files in the current directory and its subdirectories ending with .py or .md.
  2) In all files defined in 1) replace all accurances of ".example" by ".tinyYolo3lFloat32".
  
  
