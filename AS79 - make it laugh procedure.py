new = ""
def make_it_laugh(sentence):
  vowel = "aeiou"
  global new 
  for i in sentence:
    if i in vowel:
      new = new + "haha"
    else:
      new = new + i
  
sentence = input("Please type in your sentence: ")
make_it_laugh(sentence)
print(new)
