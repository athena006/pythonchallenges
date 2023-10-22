import random

number = []
floor = y = int(input("Please enter the number of floors that the building has: "))
while floor > 0:
  x = random.randint(1, y)
  while x in number:
    x = random.randint(1, y)
  print("The guard should visit floor", x, ".")
  floor = floor - 1
  number.append(x)



 
