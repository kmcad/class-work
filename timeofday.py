fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
hourcount = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' :
        continue
    else:
        colon = words[5].find(':')
        hour = words[5][:colon]
        if hour not in hourcount:
            hourcount[hour[1]] = 1
        else:
            hourcount[hour[1]] += 1
t = list()
for key, val in hourcount.items():
    t.append( (val,key) )
t.sort(reverse=True)
print(t)
