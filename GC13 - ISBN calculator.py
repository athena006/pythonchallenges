ISBN = input("Please enter the ISBN number: ")
a = int(ISBN[0]) * 1 
b = int(ISBN[1]) * 3
c = int(ISBN[2]) * 1
d = int(ISBN[3]) * 3
e = int(ISBN[4]) * 1
f = int(ISBN[5]) * 3
g = int(ISBN[6]) * 1
h = int(ISBN[7]) * 3
i = int(ISBN[8]) * 1
j = int(ISBN[9]) * 3
k = int(ISBN[10]) * 1
l = int(ISBN[11]) * 3

x = int(a+b+c+d+e+f+g+h+i+j+k+l)
y = x % 10
if y != 0:
  print("/nThe check digit is", 10 - int(y),)
else:
  print("/nThis is a valid ISBN!")


