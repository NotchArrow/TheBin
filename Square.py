import pygame, random

pygame.init()

def randomColor():
	global r
	r = random.randint(50, 205)
	global g
	g = random.randint(50, 205)
	global b
	b = random.randint(50, 205)

xLimit = random.randint(100, 1820)
yLimit = random.randint(100, 980)

resets = 0

screen = pygame.display.set_mode((xLimit, yLimit))
pygame.display.set_caption("Square " + str(resets + 1))
clock = pygame.time.Clock()

x = random.randint(0, xLimit - 50)
y = random.randint(0, yLimit - 50)
xChange = -1
yChange = -1
randomColor()
recList = []
tempList = []
beenOut = 0
trailTime = 0
trailLifespan = 0

running = True
while running:

	screen.fill((0, 0, 0))

	rec = pygame.Rect(x, y, 50, 50)

	i = 0
	while i < 10:
		x += xChange/10
		y += yChange/10
		i += 1
		rec2 = pygame.Rect(x + 25, y + 25, 5, 5)
		trailTime = 0
		trailLifespan = random.randint(0, 500)
		tempList = [rec2, r + random.randint(-50, 50), g + random.randint(-50, 50), b + random.randint(-50, 50), trailTime, trailLifespan]
		recList.append(tempList)

	if x <= 0 or x >= xLimit - 50:
		xChange = -xChange
		randomColor()
		xChange *= 1.05
		yChange *= 1.05
		beenOut += 1

	elif y <= 0 or y >= yLimit - 50:
		yChange = -yChange
		randomColor()
		xChange *= 1.05
		yChange *= 1.05
		beenOut += 1

	elif beenOut > 0:
		beenOut -= 1

	if beenOut >= 10:

		xLimit = random.randint(100, 1820)
		yLimit = random.randint(100, 980)

		resets += 1

		screen = pygame.display.set_mode((xLimit, yLimit))
		pygame.display.set_caption("Square " + str(resets + 1))

		x = random.randint(0, xLimit - 50)
		y = random.randint(0, yLimit - 50)
		xChange = -1
		yChange = -1
		randomColor()
		recList = []
		beenOut = 0

	for item in recList:
		pygame.draw.rect(screen, (item[1], item[2], item[3]), item[0])
		item[4] += 1
		if item[4] >= item[5]:
			recList.remove(item)

	pygame.draw.rect(screen, (r, g, b), rec)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	clock.tick(144)

pygame.quit()