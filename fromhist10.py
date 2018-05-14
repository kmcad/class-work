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
t = list()
for key, val in fromcount.items():
    t.append( (val,key) )
t.sort(reverse=True)
print(t[0])
