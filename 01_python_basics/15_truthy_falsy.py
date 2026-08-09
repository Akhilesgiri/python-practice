# Truthy and falsy values in Python

values = [0, 1, "", "Python", [], [1, 2], None, {}]

for item in values:
    print(repr(item), "->", bool(item))

# Common falsy values:
# 0, 0.0, "", [], {}, set(), None, False

if "Python":
    print("Non-empty string is truthy")

if not "":
    print("Empty string is falsy")

if not 0:
    print("Zero is falsy")
