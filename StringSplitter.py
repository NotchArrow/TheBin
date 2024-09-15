import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

string_1 = ""
string_2 = ""
string_3 = ""

for char in chars:
	rand = random.randint(1, 3)
	if rand == 1:
		string_1 += char
	elif rand == 2:
		string_2 += char
	elif rand == 3:
		string_3 += char

print(string_1)
print(string_2)
print(string_3)