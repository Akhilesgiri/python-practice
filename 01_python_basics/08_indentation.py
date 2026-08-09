# Indentation is required in Python.
# Blocks are defined by indentation, not braces.

x = 5
if x > 0:
    print("x is positive")
    for i in range(3):
        print("  loop index:", i)
else:
    print("x is not positive")

# Incorrect indentation will raise an IndentationError.
