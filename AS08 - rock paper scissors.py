print("Welcome to the game of Rock, Paper and Scissors!")
import random
c_choice = random.randint(1,3)
# computer choice 
# 1 = rock, 2 = paper, 3 = scissors
r = "you chose rock"
p = "you chose paper"
s = "you chose scissors"
player = 0
computer = 0
play_again = ""
while play_again != "n":
  choice = input("Please choose, rock, paper or scissors? (r,p,s): ")
  if choice == "r":
    if c_choice == 1:
      print(r+ ", computer chose rock. It's a tie!")
    elif c_choice == 2:
      print(r+ ", computer chose paper. You lose!")
      computer += 1
    elif c_choice == 3:
      print(r+ ", computer chose scissors. You win!")
      player += 1
  elif choice == "p":
    if c_choice == 1:
      print(p+ ", computer chose rock. You Win!")
      player += 1
    elif c_choice == 2:
      print(p+ ", computer chose paper. It's a tie!")
    elif c_choice == 3:
      print(p+ ", computer chose scissors. You lose!")
      computer += 1
  elif choice == "s":
    if c_choice == 1:
      print(s+ ", computer chose rock. You lose!")
      computer += 1
    elif c_choice == 2:
      print(s+ ", computer chose paper. You win!")
      player += 1
    elif c_choice == 3:
      print(s+ ", computer chose scissors. It's a tie!")
  play_again = input("Do you want to play again? (y/n)")
  c_choice = random.randint(1,3)
  
print("Thank you for playing!")
print("You have scored a total of", player,"points")
print("The computer has scored a total of", computer,"points")

if player > computer:
  print("Congratulations! You have won against the computer!")
elif player < computer:
  print("Sorry, the computer has won :<")
elif player == computer:
  print("The game ended in a tie!")
