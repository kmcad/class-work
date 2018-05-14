fileinp = input('Enter a file name: ')
fhand = open(fileinp)
count = 0
total = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        conf = float(line[20:])
        total = total + conf
        count = count + 1
print('Average spam confidence: ', total/count)