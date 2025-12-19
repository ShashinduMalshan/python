# STEP 1: Importing full modules (older, longer method)
# import my_calculator.addition as addition
# import my_calculator.subtraction as subtraction
# This means: use addition.add() and subtraction.subtract()

# STEP 2: Importing modules directly from the package
# from my_calculator import addition, subtraction
# This means: use addition.add() and subtraction.subtract()

# STEP 3: Importing only the functions from each module
# from my_calculator.addition import add
# from my_calculator.subtraction import subtract
# This means: call add() and subtract() directly

# STEP 4: Best method — import functions directly from the package (__init__.py handles this)
from my_calculator import add, subtract
# Now add() and subtract() can be used directly

# Using the functions
result = add(5, 7)
print(f"sum: {result}")

sub = subtract(10, 4)
print(f"subtraction: {sub}")
