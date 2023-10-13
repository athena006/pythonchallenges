number = 49
j = 1
i = 1
print(j)
while number <= 49 and number > 0:
  print(j)
  x = i + j
  print(x)
  i = i + j
  j = j + x
  number = number - 1
print(x + j - i)


