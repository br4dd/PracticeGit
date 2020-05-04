#add dash on every letter

word = input()
for letter in word:

    print(letter,end='')
    
    if letter != word[-1]:
        print("-",end='')