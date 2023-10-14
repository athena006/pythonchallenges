print("Rugby scoring system:")
team1 = input("\nWhat is the first team's name? ")
team2 = input("\nWhat is the seconds team's name? ")

try1 = int(input("\nHow many times did the first team score try points?"))
conv1 = int(input("How many times did the first team score conversion points? "))
pen1 = int(input("How many times did the first team score penalty points? "))

try2 = int(input("\nHow many times did the second team score try points?"))
conv2 = int(input("How many times did the second team score conversion points? "))
pen2 = int(input("How many times did the second team score penalty points? "))

a = try1*5
b = conv1*2
c = pen1*3
d = try2*5
e = conv2*2
f = pen2*3

total1 = a + b + c
total2 = d + e + f

print("\n",team1, "has scored a total of", total1, "points.", a, "of these points are from try kicks", b, "of these points are from conversion kicks and", c, "points are from penalty kicks.")
print("\n",team2, "has scored a total of", total2, "points.", d, "of these points are from try kicks", e, "of these points are from conversion kicks and", f, "points are from penalty kicks.")
