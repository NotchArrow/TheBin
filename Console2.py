import string
import random
string = ""
nextone = ""
word = input('Type What The Infinite Monkey Theorem Should Find. (lowercase)\n')
found = False
while found == False:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nextone = random.choice(letters)
    string = string + nextone
    print(str(nextone), end='')
    if word in string:
        found = True