import pygame, random

pygame.init()

screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Satisfying")
clock = pygame.time.Clock()

x = random.randint(0, 1820)
y = random.randint(0, 980)
startingX = x
startingY = y
xChange = -1
yChange = -1
xChanged = 0
yChanged = 0
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

FPS = 1000

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
		
	if y <= 0 or y >= 980:
		yChange = -yChange
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

	if x == startingX and y == startingY:
		x += 5
		startingX += 5

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				screen.fill((0, 0, 0))
				x = random.randint(0, 1820)
				y = random.randint(0, 980)
				startingX = x
				startingY = y
				r = random.randint(0, 255)
				g = random.randint(0, 255)
				b = random.randint(0, 255)

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()