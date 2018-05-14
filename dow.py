fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
datecount = dict()
for line in fhand:
    lines = line.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    else:
        if words[2] not in datecount:
            datecount[words[2]] = 1
        else:
            datecount[words[2]] += 1
print(datecount)