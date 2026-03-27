print("Hello, World!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
try:
    age = float(input("How old are you? "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number for your age.")
favorite_color = input("What is your favorite color? ")
print(f"{favorite_color} is a great color!")