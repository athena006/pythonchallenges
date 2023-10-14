sentence = input("Please input your sentence and this programme will check whether the characters 'qwerty' have been used.")

if sentence.count('qwerty') > 0:
  print("\nThe string 'qwerty' has been used",sentence.count('qwerty'),"times in this sentence.")
else: 
  print("\nThe string 'qwerty' has not been used in this sentence!")
