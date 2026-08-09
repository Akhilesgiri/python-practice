name = input("Please enter your name: ")
print("Hello, " + name + "!")

age = int(input("Please enter your age: "))
print("You are " + str(age) + " years old.")

height = float(input("Please enter your height in meters: "))
print("Your height is " + str(height) + " meters.")

boolean_input = input("Are you a developer? (yes/no): ")
is_developer = boolean_input.strip().lower() == "yes"

print("Is Developer:", is_developer)