print("This is a programme which will encode your text using Caesar Cipher")

offset = int(input("By how many characters do you want to shift your sentence? "))
sentence = input("Please type in your sentence: ")

alphabets = ["a","b","c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new = ""

for char in sentence:
  if char in alphabets:
    index = alphabets.index(char)
    new = new + alphabets[(index+offset)%26]
  else:
    new = new + char

print("Your encoded sentence is:", new)
