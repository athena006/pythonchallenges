while True:
  number = input("Please enter a whole number: ")
  try:
    x = int(number)
    print("That is a whole number!")
    break
  except ValueError:
    number = input("That is not a whole number! Please enter a whole number: ")
