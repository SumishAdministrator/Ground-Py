"""
Walrus Operator allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
Walrus Operator is represented by the `:=` syntax and can be used in a variety of contexts including while loops and if statements.

"""

d = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True}
]

print("With Python 3.8 Walrus Operator:")
for entry in d:
    if name := entry.get("name"):
        print(name)

print("Without Walrus operator:")
for entry in d:
    name = entry.get("name")
    #print(f"Name is", name)
    if name:
        print(name)


food = []
food_input = input ("Please enter a food name")
if food_input == "quit":
    break
food.append(food_input)
