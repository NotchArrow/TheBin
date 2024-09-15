num = 100

while num != 1:
	print(num)
	
	if num % 2 == 0:
		num = int(num / 2)
	elif num % 2 == 1:
		num = int(num * 3 + 1)