fileinp = input('Enter a file name: ')
count = 0
total = 0.0
try:
    fhand = open(fileinp)
except:
    if fileinp == 'no':
        print('Why not?')
    else:
        print('File cannot be opened: ', fileinp)
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        conf = float(line[20:])
        total = total + conf
        count = count + 1
print('Average spam confidence: ', total/count)