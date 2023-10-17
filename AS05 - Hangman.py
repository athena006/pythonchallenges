import random

words = ["hub", "switch", "router", "modem", "node", "packet", "bus", "star", "mesh", "hybrid", "cloud", "bluetooth", "cable", "gateway", "repeater", "bridge", "ethernet", "buferring", "streaming", "protocol"]

guess = words[random.randint(0,19)]
dash = ["_"] * len(guess)
print(" ".join(dash))

x = len(guess)
print("This word has a total of", x, "characters")
print("You can start guessing now and you have 5 lives in total. ")
life = 5

while life > 0:
  ans = input("Please type in your guess: ")
  if ans == guess:
    print("Congratulations, you have won the game! The word was:", guess)
    break
  if ans in guess:
    for i in range(x):
      if guess[i] == ans:
        dash[i] = ans
    print(" ".join(dash))
  else:
    print("Sorry, that letter is not included in the word and you lose one life :<")
    life = life - 1
    print("You have", life, "lives left")
  if '_' not in dash:
    print("Congratulations, you have won the game! The word was:", guess)
    break
if life <= 0:
  print("Sorry, you have run out of lives and have lost the game! The word was", guess)
