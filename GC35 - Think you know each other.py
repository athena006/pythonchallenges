"""Create a program that allows users to create a question about themselves and provide an answer for it.Then the program asks questions from the first user for the next user to answer. Record if the user answers the questions correctly and at the end print each users score."""

X = int(input("How many players are there? "))
print("There are", X, "players and each person will ask a question and attempt to answer the previous player's question.")
cont = ""
score = []
j = 0
while cont != "no":
  for i in range(X):
    Q = input("What is one question about yourself? ")
    A = input("What is your answer for your question? ")
    print("Now is the next player's turn.")
    y = input("What is your answer to the previous player's question?")
    if y == A:
      print("Congrats! You have the correct answer!")
      score.append(j+1)
    else:
      print("sorry, you have the wrong answer.")
      score.append(0)
    j = j + 1
  j = 0
  cont = input("Do you want to continue for another round? (yes/no): ")
print("\nFinal marks: ")
j = 0
z = 1
while X > 0:
  print("Player", z, "has", score.count(j+1), "correct answers.")
  X = X - 1
  z = z + 1
  j = j + 1
  
