# Multiple assignment examples

# Assign the same value to multiple variables.
a = b = 10
print("a:", a, "b:", b)

# Assign different values in one statement.
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

# Swap two variables without a temporary variable.
x, y = y, x
print("swapped x:", x, "swapped y:", y)

# Multiple assignment with unpacking.
name, age = "Akhil", 25
print(name, age)
