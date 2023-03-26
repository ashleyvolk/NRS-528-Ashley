# 2. Push sys.argv to the limit
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv,
# and does something to them.

# The rules:
# Minimum of three arguments to be used.
# You must do something simple in 15 lines or fewer within the Python file.
# Print or file generated output should be produced.

import sys
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" Part02.py IamArgument
def main(arg):
    print("My argument: " + str(arg))
main(sys.argv[1])
# countdown = 100
#
# while countdown > 0:
#     print ('CountDown = ', countdown)
#     countdown = countdown - 5

