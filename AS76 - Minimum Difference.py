list = input("Please enter a list of numbers separated by commas: ")
array = [int(num) for num in list.split(',')]
diff = 0
min = 100
array.sort()
print(array)
for i in range(1, len(array)):
  diff = array[i] - array[i-1]
  if diff < min:
    min = diff
print("minimum difference: ", min)
