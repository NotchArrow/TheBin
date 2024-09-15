import shutil

startingNum = 1
endingNum = 286
i = 0

while startingNum + i <= endingNum:
	try:
		shutil.rmtree("C:/Users/hokie/AppData/Roaming/MCSRRankedLauncher/instances/MSCR/saves/Random Speedrun #" + str(startingNum + i))
	except:
		pass
	i += 1