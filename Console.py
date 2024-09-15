import string
import random
choice = 0
chars = 0
loops = 0
charLoops = 0
repeat = ""
thething = input('Write A Word. (Less Than 10 Letters)\n')
while repeat != thething:
    chars = random.randint(0,9)
    choice = random.choice(string.ascii_letters)
    while charLoops < chars:
        choice = choice + random.choice(string.ascii_letters)
        charLoops = charLoops + 1
    print(choice)
    repeat = choice
    charLoops = 0
    choice = ""
    chars = 0
    