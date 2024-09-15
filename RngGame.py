import pygame
import time
import random
from fractions import Fraction

pygame.init()

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

TEXT_COLOR = (255, 255, 255)
font = pygame.font.SysFont("arialblack", 40)
def draw_text(text, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))

bestFound = 1
start = int(time.time())

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			num = random.randint(1, 4096)
			print(num)
			if num >= 2048:
				if bestFound > 1/2:
					bestFound = 1/2
			elif num >= 1024:
				if bestFound > 1/4:
					bestFound = 1/4
			elif num >= 512:
				if bestFound > 1/8:
					bestFound = 1/8
			elif num >= 256:
				if bestFound > 1/16:
					bestFound = 1/16
			elif num >= 128:
				if bestFound > 1/32:
					bestFound = 1/32
			elif num >= 64:
				if bestFound > 1/64:
					bestFound = 1/64
			elif num >= 32:
				if bestFound > 1/128:
					bestFound = 1/128
			elif num >= 16:
				if bestFound > 1/256:
					bestFound = 1/256
			elif num >= 8:
				if bestFound > 1/512:
					bestFound = 1/512
			elif num >= 4:
				if bestFound > 1/1024:
					bestFound = 1/1024
			elif num >= 2:
				if bestFound > 1/2048:
					bestFound = 1/2048
			elif num >= 1:
				if bestFound > 1/4096:
					bestFound = 1/4096

	screen.fill((0, 0, 0))

	draw_text(f"You've been playing for {int(time.time()) - start} seconds", 50, 50)
	draw_text(f"The best you have found is {Fraction(bestFound)}", 50, 300)

	pygame.display.update()
	clock.tick(60)

pygame.quit()