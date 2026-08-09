# Mutable vs immutable types in Python

# Lists are mutable: their contents can change.
numbers = [1, 2, 3]
numbers.append(4)
print("numbers:", numbers)

# Dictionaries are mutable too.
settings = {"theme": "light"}
settings["theme"] = "dark"
print("settings:", settings)

# Tuples are immutable: you cannot change their elements.
point = (10, 20)
print("point:", point)

# Strings are also immutable.
text = "hello"
print("upper text:", text.upper())
print("original text:", text)
