print("Roman numerals from 1 to 100:")
a = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
for i in range (10):
  print(i+1, a[i])
for i in range (10):
  print(i+11, "X" + a[i])
for i in range (10):
  print(i+21, "XX" + a[i])
for i in range (9):
  print(i+31, "XXX" + a[i])
print(40, "XL")
for i in range (9):
  print(i+41, "XL" + a[i])
print(50, "L")
for i in range (10):
  print(i+51, "L" + a[i])
for i in range (10):
  print(i+61, "LX" + a[i])
for i in range (10):
  print(i+71, "LXX" + a[i])
for i in range (9):
  print(i+81, "LXXX" + a[i])
print(90, "XC")
for i in range (9):
  print(i+91, "XC" + a[i])
print(100, "C")
