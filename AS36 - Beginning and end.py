list = []
new = []
a = input('Please enter your list of numbers separated by commas: ')
for i in a.split(','):
  list.append(i)

new.append(list[0])
new.append(list[len(list)-1])
print(new)
