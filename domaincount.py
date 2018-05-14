fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
domaincount = dict()
for line in fhand:
    lines = line.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    else:
        atspot = words[1].find('@')
        domain = words[1][atspot+1:]
        if domain not in domaincount:
            domaincount[domain] = 1
        else:
            domaincount[domain] += 1
print(domaincount)