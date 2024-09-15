file = open("C:/Users/hokie/curseforge/minecraft/Instances/PvP/logs/latest.log", "r")
file_lines = file.readlines()

for file_line in file_lines:
	if "was NotchArrow's final " in file_line:
		file_line = file_line.split("was NotchArrow's final ")
		user = file_line[0].split("[CHAT] ")
		num = file_line[1].split(".")
		print(f"{user[1]} | {num[0]}")