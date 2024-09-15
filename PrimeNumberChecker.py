NumToCheck = 7
prime = True

i = 2
while i < NumToCheck:
	if NumToCheck / i == int(NumToCheck / i):
		print(f'{i} is a factor of {NumToCheck}')
		prime = False
	i += 1

if prime == True:
	print(f'{NumToCheck} is prime!')