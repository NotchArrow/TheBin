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
rec = pygame.Rect(1770, 930, 50, 50)

font = pygame.font.SysFont("arialblack", 10)
TEXT_COLOR = (255, 255, 255)

def draw_text(text, font, TEXT_COLOR, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))


running = True
while running:

	while iteration_complete == False:
		color = random.randint(0, 2)
		if current_pixel_color[color] < 255:
			iteration_complete = True
			current_pixel_color = list(current_pixel_color)
			current_pixel_color[color] += 5
			current_pixel_color = tuple(current_pixel_color)

		pygame.draw.rect(screen, current_pixel_color, rec)
		draw_text(str(x), font, TEXT_COLOR, 1780, 940)
		draw_text(str(y), font, TEXT_COLOR, 1780, 960)

	iteration_complete = False

	pxarray = pygame.PixelArray(screen)
	pxarray[x, y] = current_pixel_color
	pxarray.close()

	if current_pixel_color == (255, 255, 255):
		current_pixel_color = (0, 0, 0)
		x += 1

	if x > 1820:
		y += 1
		x = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
	clock.tick(60)

pygame.quit()