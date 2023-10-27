"""Can you create a randomly generated password based off a favorite color, place and animal? And also add special characters to the end of it."""

import random
password = ""
x = random.randint(1,6)
if x == 1:
  password = "#$%"
elif x == 2:
  password = "$%#"
elif x == 3:
  password = "#%$"
elif x == 4:
  password = "$#%"
elif x == 5:
  password = "%#$"
else:
  password == "%$#"
special = ["!","@", "#", "&", "*", "^", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "<"]
z = random.randint(0,len(special))
color = input("What is your favourite colour? ")
password = password.replace("#",color)
place = input("What is your favourite place? ")
password = password.replace("$",place)
animal = input("What is your favourite animal? ")
password = password.replace("%",animal)
print("Your randomly generated password is: ", password+special[z-1]+special[z-1-(random.randint(1,len(special)-z))]+special[z-5])
