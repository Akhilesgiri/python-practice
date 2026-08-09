# None is a special value that means "no value" or "missing value".

user = None
print("user is None?", user is None)

if user is None:
    print("No user is logged in.")

user = "Akhil"
print("user is None?", user is None)
print("Logged in user:", user)

# Use "is" to compare with None, not ==.
