import random
P1 = input("What is player 1's name?")
P2 = input("What is player 2's name?")
print("Great! Now let's start the game")
cont = ""
scoreA = 0
scoreB = 0
while cont != "yes":
  X = random.randint(1,12)
  Y = random.randint(1,12)
  print(P1,"What is the answer to",X,"x",Y,"?")
  A = int(input("Answer: "))
  if A == X * Y:
    print("Correct!")
    scoreA = scoreA + 1
  else:
    print("Sorry, your answer is wrong. The correct answer is", X*Y)
  X = random.randint(1,12)
  Y = random.randint(1,12)
  print(P2,"What is the answer to",X,"x",Y,"?")
  B = int(input("Answer: "))
  if B == X * Y:
    print("Correct!")
    scoreB = scoreB + 1
  else:
    print("Sorry, your answer is wrong. The correct answer is", X*Y)
  cont = input("Do you want to end the game?")

print(P1,"scored a total of",scoreA,"points")
print(P2,"scored a total of",scoreB,"points")

if scoreA > scoreB:
  print(P1,"won the game!")
elif scoreB > scoreA:
  print(P2,"won the game!")
else:
  print("You are both tied!")
