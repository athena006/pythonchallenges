numbers = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
i = 0
j = 7
while i in range(9):
  print(((9-i)*"  "),*numbers[0:i+1],*numbers[17-i:18])
  i = i + 1

while j >= 0:
  print(((9-j)*"  "),*numbers[0:j],*numbers[16-j:18])
  j = j - 1
