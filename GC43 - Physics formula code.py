print("Equation 1: v = u + at")
print("Equation 2: s = ut + 1/2at^2")
print("Equation 3: s = vt - 1/2at^2")
print("Equation 4: v^2 = u^2 + 2as")
print("Equation 5: s = 1/2 * (u+v) * t")
choice = int(input("Please choose which equation do you want to use: "))

if choice == 1:
  u = float(input("Please enter the value of u: "))
  a = float(input("Please enter the value of a: "))
  t = float(input("Please enter the value of t: "))
  v = u + a * t
  print("The value of v is: ", v)
elif choice == 2:
  u = float(input("Please enter the value of u: "))
  a = float(input("Please enter the value of a: "))
  t = float(input("Please enter the value of t: "))
  s = u * t + 0.5 * a * t ** 2
  print("The value of s is: ", s) 
elif choice == 3:
  s = float(input("Please enter the value of s: "))
  a = float(input("Please enter the value of a: "))
  t = float(input("Please enter the value of t: "))
  v = s / t - 0.5 * a * t ** 2
  print("The value of v is: ", v)
elif choice == 4:
  u = float(input("Please enter the value of u: "))
  a = float(input("Please enter the value of a: "))
  s = float(input("Please enter the value of s: "))
  v = (u ** 2 + 2 * a * s) ** 0.5
  print("The value of v is: ", v)
elif choice == 5:
  u = float(input("Please enter the value of u: "))
  v = float(input("Please enter the value of v: "))
  t = float(input("Please enter the value of t: "))
  s = 0.5 * (u + v) * t
  print("The value of s is: ", s)
  
