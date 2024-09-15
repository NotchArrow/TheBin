import time

while True:
	print("1. Add Data")
	print("2. View Data")
	print("3. Exit")
	choice = input("What would you like to do? ")
	print("\n")
	if choice == "1":
		print("1. Pullups")
		print("2. Pushups")
		exercise = input("What did you do? ")
		if exercise == "1":
			exercise = "Pullups"
		elif exercise == "2":
			exercise = "Pushups"
		else:
			print("Invalid Input.")
		quantity = input("How many? ")
		if quantity.isnumeric():
			file = open("Log.txt", "a")
			file.write(f"{quantity} {exercise} | {time.asctime()}")
			file.write("\n")
			file.close()
		else:
			print("Invalid Input.")
	elif choice == "2":
		pushup_total = 0
		pullup_total = 0
		file = open("Log.txt", "r")
		for line in file.readlines():
			print(line)
			data = line.split()
			if data[1] == "Pullups":
				pullup_total += int(data[0])
			elif data[1] == "Pushups":
				pushup_total += int(data[0])
		print("\n")
		print(f"{pullup_total} Total Pullups")
		print(f"{pushup_total} Total Pushups")

	elif choice == "3":
		break
	else:
		print("Invalid Input.")
	print("\n")