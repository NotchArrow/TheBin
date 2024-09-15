import pygame

pygame.init()

screen = pygame.display.set_mode((800, 150))
clock = pygame.time.Clock()

TEXT_COLOR = (255, 255, 255)
font = pygame.font.SysFont("arialblack", 40)
def draw_text(text, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))

i = 1
fps = 144

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0, 0, 0))

	draw_text(str(int(i)), 50, 50)

	i *= 1.001

	pygame.display.update()
	clock.tick(fps)

pygame.quit()