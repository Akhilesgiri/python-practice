# Type annotations in Python

name: str = "Akhil"
age: int = 25
height: float = 1.75
is_student: bool = False


def greet(person: str) -> str:
    return "Hello, " + person

print(greet(name))
