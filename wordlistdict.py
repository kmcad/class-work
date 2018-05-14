wordsdict = dict()
count = 0
fhand = open('data\words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1
        if word in wordsdict : continue
        wordsdict[word] = count
inp = input('Enter a word: ')
if inp in wordsdict:
    print(wordsdict[inp])
else:
    print('%s is not in the dictionary' % inp)