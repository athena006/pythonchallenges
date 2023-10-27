import random
print("Welcome to the Hex and Binary quiz machine!")
end = "no"
points = 0
y = ""
while end != "yes":
  x = ''.join(str(random.randint(0, 1)) for i in range(8))
  q = input(f"What is the Hex number for Binary number {x}? (start with 0x) ")
  z = int(x, 2)
  if q == hex(z):
    print("Correct! You are rewarded one mark!")
    points = points + 1
  else:
    print("Sorry, your answer is wrong. The correct answer is", hex(z))
  end = input("Do you want to end the game? (yes/no) ")
print("Your finals poins is", points, "points")
