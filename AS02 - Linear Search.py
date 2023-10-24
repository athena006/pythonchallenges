Numbers = [""]
insert = input("Please enter your data set separated by commas: ")
Numbers = insert.split(',')
length = len(Numbers)
element = input("Please enter the element that you want to find: ")
for x in range(len(Numbers)):
  if Numbers[x] == element:
    print("The element has been found! It is at position", x+1)
    break
  else:
    print("Sorry, the element has not been found in the data set.")
    break
