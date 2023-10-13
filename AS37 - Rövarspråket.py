sentence = input("Please input your original sentence ")
alphabet = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
new = ["bob","coc","dod", "fof", "gog", "hoh", "joj", "kok", "lol", "mom", "non", "pop", "qoq", "ror", "sos", "tot", "vov", "wow", "xox", "yoy", "zoz"]

for i in range(20):
  sentence = sentence.replace(alphabet[i],new[i])
print(sentence)

next = input("\nNow input a sentence in Rövarspråket ")
for i in range(20):
  next = next.replace(new[i],alphabet[i])
print(next)
