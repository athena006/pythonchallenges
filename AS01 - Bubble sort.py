import random
TestArray = [random.randint(0,10) for i in range(9)]
n = len(TestArray)
temp = ""
def bubble_sort(TestArray):
  for i in range(0,n-1):
    for j in range(n-1):
      if TestArray[j] > TestArray[j+1]:
        global temp
        temp = TestArray[j]
        TestArray[j] = TestArray[j+1]
        TestArray[j+1] = temp
  return TestArray

print("The original list is", TestArray)
print("The new list is", bubble_sort(TestArray))
