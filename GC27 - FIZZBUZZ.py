import time
i = 1
while i < 21:
  if i % 3 == 0 and i % 5 == 0:
    time.sleep(1)
    print("FizzBuzz")
  elif i % 3 == 0:
    time.sleep(1)
    print("Fizz")
  elif i % 5 == 0:
    time.sleep(1)
    print("Buzz")
  else:
    time.sleep(1)
    print(i)
  i = i + 1
