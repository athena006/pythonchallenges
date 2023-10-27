sentence = input("Please input your sentence, and the programme will help check if the number of brackets is balanced: ")
a = 0
b = 0
c = 0
d = 0
for char in sentence:
  if char == "(":
    a = a + 1
  elif char == ")":
    a = a - 1
  elif char == "[":
    b = b + 1
  elif char == "]":
    b = b - 1
  elif char == "{":
    c = c + 1
  elif char == "}":
    c = c - 1
  elif char == "<":
    d = d + 1
  elif char == ">":
    d = d - 1
if a == 0 and b == 0 and c == 0:
  print("The number of brackets is balanced.")
else:
  if a != 0:
    print("The number of round brackets are not balanced!")
  if b != 0:
    print("The number of square brackets are not balanced!")
  if c != 0:
    print("The number of curly brackets are not balanced!")
  if d != 0:
    print(f"The number of angle brackets are not balanced!")
