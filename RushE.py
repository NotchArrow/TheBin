import pygame, random

pygame.init()

screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Rush E")
clock = pygame.time.Clock()

x = 10
y = 970
startingX = x
startingY = y
xChange = -1
yChange = -1
xChanged = 0
yChanged = 0
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

pygame.mixer.music.load("sounds/RushE.wav")
pygame.mixer.music.play()
bounces = 1
resets = 0

FPS = 60

running = True
while running:

	xChanged = 0
	yChanged = 0

	rec = pygame.Rect(x, y, 5, 5)
	pygame.draw.rect(screen, (r, g, b), rec)

	#x += xChange
	#y += yChange

	if xChange < 0:
		while xChange < xChanged:
			x -= 1
			xChanged -= 1
			rec = pygame.Rect(x, y, 5, 5)
			if yChange < 0:
				y -= 1
				yChanged -= 1
				rec = pygame.Rect(x, y, 5, 5)
				pygame.draw.rect(screen, (r, g, b), rec)
			elif yChange > 0:
				y += 1
				yChanged += 1
				rec = pygame.Rect(x, y, 5, 5)
				pygame.draw.rect(screen, (r, g, b), rec)
	elif xChange > 0:
		while xChange > xChanged:
			x += 1
			xChanged += 1
			rec = pygame.Rect(x, y, 5, 5)
			if yChange < 0:
				y -= 1
				yChanged -= 1
				rec = pygame.Rect(x, y, 5, 5)
				pygame.draw.rect(screen, (r, g, b), rec)
			elif yChange > 0:
				y += 1
				yChanged += 1
				rec = pygame.Rect(x, y, 5, 5)
				pygame.draw.rect(screen, (r, g, b), rec)

	if x <= 0 or x >= 1820:
		xChange = -xChange
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		if xChange < 0:
			xChange -= 3 + resets * 1.2
		else:
			xChange += 3 + resets * 1.2
		bounces += 1
		print(bounces)
		
	if y <= 0 or y >= 980:
		yChange = -yChange
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		if yChange < 0:
			yChange -= 3 + resets * 1.2
		else:
			yChange += 3 + resets * 1.2
		bounces += 1
		print(bounces)

	if x == startingX and y == startingY:
		x += 5
		startingX += 5

	if bounces % 1500 == 0 and resets == 0:
		screen.fill((0, 0, 0))
		x = 10
		y = 970
		startingX = x
		startingY = y
		xChange = -1
		yChange = -1
		xChanged = 0
		yChanged = 0
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		resets = 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				screen.fill((0, 0, 0))
				x = 10
				y = 970
				startingX = x
				startingY = y
				xChange = -1
				yChange = -1
				xChanged = 0
				yChanged = 0
				resets = 0
				bounces = 0
				pygame.mixer.music.load("sounds/RushE.wav")
				pygame.mixer.music.play()
				r = random.randint(0, 255)
				g = random.randint(0, 255)
				b = random.randint(0, 255)

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()