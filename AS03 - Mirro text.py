sentence = input("Please type in your sentence: ")
x = []
for i in sentence:
    x.append(i)
z = "".join(x[::-1])
print(z)
