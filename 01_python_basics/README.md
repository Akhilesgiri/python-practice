# 01 Python Basics

This directory contains introductory examples covering the fundamental building blocks of Python programming. Below is a comprehensive guide to all the concepts covered in this module, complete with definitions, examples, and expected outputs.

---

## 1. Hello World (`01_hello_world.py`)
**Definition:** The `print()` function is used to output text or data to the console. It is typically the first thing you learn in any programming language.
**Example:**
```python
print("Hello, World!")
```
**Output:**
```text
Hello, World!
```

---

## 2. Variables (`02_variables.py`)
**Definition:** Variables are containers for storing data values. In Python, a variable is created the moment you first assign a value to it.
**Example:**
```python
name = "Akhil"
age = 24
print(name, "is", age, "years old.")
```
**Output:**
```text
Akhil is 24 years old.
```

---

## 3. Data Types (`03_datatypes.py`)
**Definition:** Data types define the type of data a variable can hold. Common built-in types are:
- `int` (Integer): Whole numbers.
- `float` (Floating point): Numbers with a decimal point.
- `str` (String): Text enclosed in quotes.
- `bool` (Boolean): Represents `True` or `False`.
**Example:**
```python
my_age = 24       # int
my_height = 5.7   # float
is_developer = True # bool
```

---

## 4. Type Conversion (`04_type_conversion.py`)
**Definition:** Also known as type casting, this is the process of converting a variable from one data type to another using functions like `int()`, `float()`, `str()`, and `bool()`.
**Example:**
```python
age_str = "25"
age_int = int(age_str)
print(type(age_int))
```
**Output:**
```text
<class 'int'>
```

---

## 5. Input and Output (`05_input_output.py`)
**Definition:** `input()` allows you to take input from the user via the console. It always returns a string, so you often need to combine it with type conversion.
**Example:**
```python
name = input("Enter your name: ") # user types "Akhil"
print("Hello, " + name + "!")
```
**Output:**
```text
Enter your name: Akhil
Hello, Akhil!
```

---

## 6. Comments (`06_comments.py`)
**Definition:** Comments are notes in the code that the Python interpreter ignores. They explain what the code does. Single-line comments use `#`.
**Example:**
```python
# This is a single line comment
print("Code runs!") # This also works
```

---

## 7. Keywords (`07_keywords.py`)
**Definition:** Keywords are reserved words in Python that have special meanings and cannot be used as variable names (e.g., `if`, `else`, `True`, `False`, `None`).
**Example:**
```python
is_active = True
if is_active:
    print("User is active")
```
**Output:**
```text
User is active
```

---

## 8. Indentation (`08_indentation.py`)
**Definition:** Unlike languages that use curly braces `{}`, Python uses indentation (whitespace/spaces at the beginning of a line) to define blocks of code (like inside `if` statements or loops).
**Example:**
```python
x = 5
if x > 0:
    print("x is positive") # Indented by 4 spaces
```

---

## 9. Naming Conventions (`09_naming_conventions.py`)
**Definition:** Standard ways to name things to make code readable.
- **Variables/Functions:** `snake_case` (all lowercase with underscores).
- **Constants:** `UPPER_CASE_WITH_UNDERSCORES`.
**Example:**
```python
first_name = "Akhil"
MAX_COUNT = 10
```

---

## 10. Multiple Assignment (`10_multiple_assignment.py`)
**Definition:** Python allows you to assign values to multiple variables in one line.
**Example:**
```python
x, y, z = 1, 2, 3
a = b = 10
name, age = "Akhil", 25
print(x, y, z)
```
**Output:**
```text
1 2 3
```

---

## 11. Constants (`11_constants.py`)
**Definition:** Python does not have a built-in constant type, but by convention, variables whose values should not change are named in all uppercase letters.
**Example:**
```python
PI = 3.14159
DEFAULT_LANGUAGE = "Python"
```

---

## 12. Docstrings (`12_docstrings.py`)
**Definition:** Documentation strings (docstrings) are string literals that appear right after the definition of a function, method, class, or module. They are enclosed in triple quotes `"""`.
**Example:**
```python
def say_hello():
    """Return a simple greeting."""
    return "Hello"

print(say_hello.__doc__)
```
**Output:**
```text
Return a simple greeting.
```

---

## 13. Type Annotations (`13_type_annotations.py`)
**Definition:** Type hints allow you to explicitly state the expected data types for variables, function arguments, and return values. They help with readability and IDE autocomplete.
**Example:**
```python
name: str = "Akhil"
def greet(person: str) -> str:
    return "Hello, " + person
```

---

## 14. Mutable vs Immutable (`14_mutable_vs_immutable.py`)
**Definition:** 
- **Mutable:** Objects that can be changed after they are created (e.g., `list`, `dict`).
- **Immutable:** Objects that cannot be changed after creation (e.g., `int`, `float`, `str`, `tuple`). If you modify them, a new object is created in memory.
**Example:**
```python
# Mutable (List)
numbers = [1, 2, 3]
numbers.append(4) # [1, 2, 3, 4]

# Immutable (String)
text = "hello"
text_upper = text.upper() # returns a new string "HELLO", 'text' remains "hello"
```

---

## 15. Truthy and Falsy (`15_truthy_falsy.py`)
**Definition:** When evaluated in a boolean context (like an `if` statement), some values evaluate to `True` (truthy) and others to `False` (falsy). 
- **Falsy values:** `0`, `0.0`, `""` (empty string), `[]`, `{}`, `None`, `False`.
- **Truthy values:** Almost everything else (e.g., `"Python"`, `[1, 2]`, `10`).
**Example:**
```python
if "":
    print("This won't print because empty strings are falsy")
if "Python":
    print("Non-empty strings are truthy!")
```
**Output:**
```text
Non-empty strings are truthy!
```

---

## 16. None (`16_none.py`)
**Definition:** `None` is a special constant in Python that represents the absence of a value or a null value. You should always use the `is` keyword to compare against `None`.
**Example:**
```python
user = None
if user is None:
    print("No user is logged in.")
```
**Output:**
```text
No user is logged in.
```
