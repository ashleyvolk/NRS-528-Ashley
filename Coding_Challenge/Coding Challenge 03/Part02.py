# 2. Push sys.argv to the limit
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv,
# and does something to them.

# The rules:
# Minimum of three arguments to be used.
# You must do something simple in 15 lines or fewer within the Python file.
# Print or file generated output should be produced.

import sys

# Get command-line arguments
args = sys.argv[1:]

# Convert arguments to numbers
numbers = [int(arg) for arg in args]

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted numbers
print("Sorted numbers:", sorted_numbers)

# C:\Users\Ashley>C:\Users\Ashley\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe C:\NRS_528\Assignment\CodingChallege03\Part02.py
# Sorted numbers: []