sum = 0
product = 1
def calculation(numbers):
  global list
  global sum
  global product
  for i in list:
    sum = sum + i
    product = product * i

x = input("Please input a list of numbers separated by a comma: ")
y = x.split(",")
list = [int(i) for i in y] 
calculation(list)
print("The sum of the numbers is: ", sum)
print("The product of the numbers is: ", product)
