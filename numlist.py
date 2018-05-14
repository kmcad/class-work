numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        print(max(numlist))
        print(min(numlist))
        exit()
    value = float(inp)
    numlist.append(value)
