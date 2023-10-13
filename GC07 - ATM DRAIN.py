balance = 500

X = int(input("Please enter the amount that you want to withdraw: "))
while X % 5 != 0:
  print("\nThe amount you can withdraw can only be a multiple of 5") 
  X = int(input("\nPlease enter the amount that you want to withdraw: "))
  
while X + 0.5 > balance:
    print("\nInsufficient balance")
    X = int(input("\nPlease enter the amount that you want to withdraw: "))

balance = balance - X - 0.50
print("\nYour current balance is: ", balance, "dollars")

