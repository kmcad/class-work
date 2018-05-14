fhand = open('data\copyromeo.txt')
finallist = []
for line in fhand:
    words = line.split()
    for x in words:
        if x in finallist: continue
        finallist.append(x)
finallist.sort()
print(finallist)