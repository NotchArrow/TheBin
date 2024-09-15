list_of_nums = []

while True:
	if len(list_of_nums) > 0:
		list_of_nums.sort()
		for item in list_of_nums:
			print(item, end = " | ")
		print(len(list_of_nums))
		print(f"Average: {sum(list_of_nums)/ len(list_of_nums)}")
	user_input = input("Enter a number to add to the dataset: ")
	try:
		list_of_nums.append(float(user_input))
		print(f"{user_input} added successfully!")
	except:
		print(f"{user_input} is not a number!")
	print("\n")