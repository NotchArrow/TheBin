import pygame
import pyautogui

pygame.init()

screen = pygame.display.set_mode((800, 150))
clock = pygame.time.Clock()

TEXT_COLOR = (255, 255, 255)
font = pygame.font.SysFont("arialblack", 40)
def draw_text(text, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))

pixelsMoved = 0

prevX = pyautogui.position()[0]
prevY = pyautogui.position()[1]

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0, 0, 0))

	X = pyautogui.position()[0]
	Y = pyautogui.position()[1]

	pixelsMoved += abs(X - prevX) + abs(Y - prevY)

	prevX = X
	prevY = Y

	draw_text("Pixels Moved: " + str(pixelsMoved), 50, 50)

	pygame.display.update()
	clock.tick(60)

pygame.quit()