count = 0
total = 0
largest = None
smallest = None
while True:
    line = input('Number: ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    try:
        number = float(line)
    except:
        print('Invalid input')
        continue
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number
    count = count + 1
    total = total + number
print(total,count,largest,smallest)
