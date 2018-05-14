fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
fromcount = dict()
for line in fhand:
    lines = line.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    else:
        if words[1] not in fromcount:
            fromcount[words[1]] = 1
        else:
            fromcount[words[1]] += 1
maximum = 0
for person in fromcount:
    if fromcount[person] > maximum:
        maximum = fromcount[person]
        maxfrom = person
print(maxfrom, maximum)