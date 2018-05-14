def count(word,character):
    total = 0
    for letter in word:
        if letter == character:
            total = total + 1
    return total

inpword = input('Please enter a word: ')
inpletter = input('Please enter the letter you would like to count: ')
total = count(inpword, inpletter)
print(total)