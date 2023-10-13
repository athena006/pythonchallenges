sentence = input("Please input your original sentence ")
alphabet = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
new = ["bob","coc","dod", "fof", "gog", "hoh", "joj", "kok", "lol", "mom", "non", "pop", "qoq", "ror", "sos", "tot", "vov", "wow", "xox", "yoy", "zoz"]
x = ["bobbob","coccoc","doddod","foffof", "goggog", "hohhoh", "jojjoj", "kokkok", "lollol", "mommom", "nonnon", "poppop", "qoqqoo", "rorror", "sossos", "tottot", "vovvov", "wowwow", "xoxxox", "yoyyoy", "zozzoz"]
y = ["bbobb","ccocc","ddodd", "ffoff", "ggogg", "hhohh", "jjojj", "kkokk","lloll", "mmomm", "nnonn", "ppopp", "qqoqq", "rrorr", "ssoss","ttott","vvovv","wwoww","xxoxx","yyoyy","zzozz"]

for i in range(21):
  sentence = sentence.replace(alphabet[i],new[i])
  sentence = sentence.replace(x[i],y[i])
print(sentence)

next = input("\nNow input a sentence in Rövarspråket ")
for i in range(21):
  next = next.replace(y[i],x[i])
  next = next.replace(new[i],alphabet[i])
print(next)
