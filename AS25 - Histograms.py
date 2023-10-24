def histogram(value):
  for length in value:
    print ("*" * length)

stats = input("Please enter your histogram statistics, with each number indicating the length of the bar and each bar value separated by commas: ")
length = [int(i) for i in stats.split(',')]

histogram(length)
 





