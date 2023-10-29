def reverse(sentence):
  sentence = sentence[::-1]
  return sentence

sentence = input("Please type in the sentence that you want to reverse: ")
new = reverse(sentence)
print(new)
