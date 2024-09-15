import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((300, 150))
pygame.display.set_caption("Stopwatch")
clock = pygame.time.Clock()

TEXT_COLOR = (255, 255, 255)
font = pygame.font.SysFont("arialblack", 40)
def draw_text(text, font, TEXT_COLOR, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))


minutes = 0
seconds = 0
miliseconds = 0
secondsStr = "0"
minutesStr = "0"
paused = False
startTime = round(time.time() * 1000)

running = True
while running:
	if paused == False:
		miliseconds = (round(time.time() * 1000) - startTime) % 1000
		if miliseconds < 10:
			milisecondsStr = "00" + str(miliseconds)
		elif miliseconds < 100:
			milisecondsStr = "0" + str(miliseconds)
		else:
			milisecondsStr = str(miliseconds)

		seconds = math.floor((round(time.time() * 1000) - startTime) / 1000 % 60)
		if seconds == 60:
			seconds = 0
		if seconds < 10:
			secondsStr = "0" + str(seconds)
		else:
			secondsStr = str(seconds)

		minutes = math.floor(((time.time() * 1000) - startTime) / 60000)
		if minutes < 10:
			minutesStr = "0" + str(minutes)
		else:
			minutesStr = str(minutes)

	screen.fill((0, 0, 0))
	draw_text(minutesStr + ":" + secondsStr + "." + milisecondsStr, font, TEXT_COLOR, 50, 50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if paused == True:
					paused = False
					startTime = startTime + round(time.time() * 1000) - pauseStart
				elif paused == False:
					paused = True
					pauseStart = round(time.time() * 1000)

	pygame.display.update()
	clock.tick(60)

pygame.quit()