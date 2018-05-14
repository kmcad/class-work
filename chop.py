def chop(t):
    del t[0]
    del t[-1]
letters = ['a', 'b', 'c', 'd', 'e']
chop(letters)
print(letters)
