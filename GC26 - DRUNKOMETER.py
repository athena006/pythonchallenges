x = "hohellollo momyoy nonamome isos atothohenona i amom cocurrorrenontotlolyoy a sostotudodenontot anon gis anondod sostotudodyoyinongog cocomompoputoteror soscocienoncoce itot isos nonotot momyoy fofavovouroritote sosubobjojecoctot bobutot i fofinondod popyoytothohonon voveroryoy fofunon"
print("Please enter the following sentence: ", x)

i = 0
j = 0

phrase1 = input("Please enter the sentence above: ")
phrase2 = input("Please enter the same sentence again: ")
if phrase1 != x:
  while x != phrase1 and i < 3:
    phrase1 = input("You have typed something wrong, please try again: ")
    i = i + 1
  else:
    print("You have used up all your chances, YOU ARE DEFINITELY DRUNK")
elif phrase2 != x:
  while x == phrase1 and x != phrase2 and j < 3:
   phrase2 = input("You have succeeded in the first try but not the second  try, please try again: ")
   j = j + 1
  else:
   print("You have used up all your chances, YOU ARE DEFINITELY DRUNK")
else:
  print("Congratulations! You have passed the test and is MOST LIKELY not drunk!")
  



