vowels = "AaEeIiOoUu"
sentence = input("Please type in your sentence: ")
x = 0
for char in sentence:
  if char in vowels:
    x = x + 1
print(x)
