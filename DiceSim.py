import random
import time

sidesOfDice = 6
rollsToDo = 100000000

resultsList = [0]
possibleOutcomes = 1
while possibleOutcomes < sidesOfDice:
	resultsList.append(0)
	possibleOutcomes += 1

if rollsToDo <= 1000000:
	rollsDone = 0
	while rollsDone < rollsToDo:
		outcome = random.randint(0, sidesOfDice - 1)
		resultsList[outcome] += 1
		rollsDone += 1

	print(f'Results of {rollsToDo} rolls:')
	for item in resultsList:
		print(f"There were {item} {resultsList.index(item) + 1}'s rolled ({item/rollsToDo*100}%)")

else:
	start = round(time.time() * 1000)
	rollsDone = 0
	while rollsDone < rollsToDo:
		outcome = random.randint(0, sidesOfDice - 1)
		resultsList[outcome] += 1
		rollsDone += 1
		if rollsDone % 1000000 == 0:
			print(f'Results of {rollsDone} rolls:')
			for item in resultsList:
				print(f"There were {item} {resultsList.index(item) + 1}'s rolled ({item/rollsDone*100}%)")
			print(f'It took {round(time.time() * 1000) - start}ms to complete the last 1,000,000 rolls')
			start = round(time.time() * 1000)
			print()

	print(f'Results of {rollsToDo} rolls:')
	for item in resultsList:
		print(f"There were {item} {resultsList.index(item) + 1}'s rolled ({item/rollsToDo*100}%)")