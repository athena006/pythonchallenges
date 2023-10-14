user_input = input("Please enter a number: ")
try:
  user_input = float(user_input)
except ValueError:
  print("Invalid input. ARE YOU SURE THAT'S A NUMBER?")
else:
  print("Yes that is a number indeed.")
