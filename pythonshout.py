fileinp = input('Enter a file name: ')
fhand = open(fileinp)
for line in fhand:
    sline = line.rstrip()
    print(sline.upper())