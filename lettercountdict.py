import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
counts = 0
lettercounts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in lettercounts:
                lettercounts[letter] = 1
            else:
                lettercounts[letter] += 1
lc_list = list()
for key, val in list(lettercounts.items()):
    lc_list.append((val, key))
lc_list.sort(reverse=True)
for key, val in lc_list:
    print(key,val)