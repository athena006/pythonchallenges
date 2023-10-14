import random

print("You are prisoner A, and this programme is designed to be prisoner B")

confess1 = input("Do you want to confess? (y/n) ")
confess2 = random.choice(["y", "n"])

while confess1 != "y" and confess1 != "n":
  confess1 = input("Please enter a valid input (y/n)")

if confess2 == "y":
  print("Prisoner B has chosen to confess")
else:
  print("Prisoner B has chosen to not confess")

if confess1 == "y" and confess2 == "y":
  print("You have both chosen to confess and will be stay in prison for 5 years")
elif confess1 == "y" and confess2 == "n":
  print("Prisoner B has chosen not to confess and will stay in prison for 20 years! You are free to go.")
elif confess1 == "n" and confess2 == "y":
  print("You has chosen not to confess and will stay in prison for 20 years! Prisoner B is free to go.")
else: 
  print("You have both chosen not to confess and will only stay in prison for 1 year each.")
  
