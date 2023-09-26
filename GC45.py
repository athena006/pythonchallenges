user_input = ''

while True:
    user_input = input('Enter a single character: ')

    if len(user_input) == 1:
        print(user_input)
        break

    else:
        print('Enter a single character to continue.')
        continue
