import secrets
import string

charactersToUse = string.ascii_letters + string.digits + string.punctuation

def generator(length):
	password = ''

	while len(password) < length:
		password += secrets.choice(charactersToUse)

	return password

while True:
	print('Type anything non-numeric to exit')
	desiredLength = input('Type the desired password length: ')
	if desiredLength.isnumeric():
		password = generator(int(desiredLength))
		print(password)

	else:
		break