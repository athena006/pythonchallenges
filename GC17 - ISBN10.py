ISBN = input("Please type in the ISBN number ")
while len(ISBN) != 10:
  ISBN = input("\nThe ISBN number should be 10 digits long! ")
  
a = int(ISBN[0]) * 10 
b = int(ISBN[1]) * 9
c = int(ISBN[2]) * 8
d = int(ISBN[3]) * 7
e = int(ISBN[4]) * 6
f = int(ISBN[5]) * 5
g = int(ISBN[6]) * 4
h = int(ISBN[7]) * 3
i = int(ISBN[8]) * 2

x = a+b+c+d+e+f+g+h+i
y = 11 - (x % 11)

if y == int(ISBN[9]):
  print("The ISBN number is valid")
else:
  print("The ISBN number is not valid!")
