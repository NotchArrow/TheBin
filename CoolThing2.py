import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Cool maybe")
clock = pygame.time.Clock()

x = 0
y = 0
current_pixel_color = (0, 0, 0)
color = 0
iteration_complete = False
addition = random.randint(1, 100)


running = True
while running:

	while iteration_complete == False:
		color = random.randint(0, 2)
		addition = random.randint(1, 100)
		if current_pixel_color[color] + addition < 255:
			iteration_complete = True
			current_pixel_color = list(current_pixel_color)
			current_pixel_color[color] += addition
			current_pixel_color = tuple(current_pixel_color)

	iteration_complete = False

	pxarray = pygame.PixelArray(screen)
	pxarray[x, y] = current_pixel_color
	pxarray.close()

	x += 1

	if x >= 1820:
		y += 1
		x = 0

	if y >= 980:
		x = 0
		y = 0

	current_pixel_color = tuple(screen.get_at((x, y)))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	clock.tick(1000)

pygame.quit()