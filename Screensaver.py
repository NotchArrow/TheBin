import pygame, random

pygame.init()

screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Satisfying")
clock = pygame.time.Clock()

x = random.randint(0, 1820)
y = random.randint(0, 980)
xChange = -1
yChange = -1
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

running = True
while running:

	rec = pygame.Rect(x, y, 5, 5)
	pygame.draw.rect(screen, (r, g, b), rec)

	x += xChange
	y += yChange

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

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	clock.tick(6000)

pygame.quit()