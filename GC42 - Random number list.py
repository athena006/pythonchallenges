import random
numbers = []
for i in range (50):
  numbers.append(random.randint(0,200))

print("The list of numbers are:\n", *numbers)
print("\nThe minimum value is:", min(numbers))
print("\nThe maximum value is:", max(numbers))
print("\nThe mean average is:", sum(numbers)/len(numbers))
