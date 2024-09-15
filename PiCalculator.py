sequence_len = 1000000
num = 3

for i in range(sequence_len):
	fac1 = i * 2 + 2
	fac2 = i * 2 + 3
	fac3 = i * 2 + 4
	total = fac1 * fac2 * fac3
	change = 4/total
	if i % 2 == 0:
		num += change
	elif i % 2 == 1:
		num -= change

print(num)