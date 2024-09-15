import pygame, random

pygame.init()

screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Mouse Trail")
clock = pygame.time.Clock()

recList = []

running = True
while running:

	screen.fill((0, 0, 0))

	for item in recList:
		item[4] += item[8]
		item[5] += 1

		rec = pygame.Rect(item[3], item[4], item[7], item[7])
		pygame.draw.rect(screen, (item[0], item[1], item[2]), rec)

		if item[5] >= item[6]:
			recList.remove(item)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEMOTION:
			i = 0
			while i < random.randint(1, 10):
				x = pygame.mouse.get_pos()[0] + random.randint(-20, 20)
				y = pygame.mouse.get_pos()[1] + random.randint(-20, 20)

				r = random.randint(150, 250)
				g = random.randint(150, 250)
				b = random.randint(0, 50)

				time = 0
				timeAllowed = random.randint(0, 300)
				size = random.randint(0, 10)
				fallSpeed = random.uniform(1, 2)

				rec = pygame.Rect(x, y, size, size)
				
				tempList = [r, g, b, x, y, time, timeAllowed, size, fallSpeed]
				recList.append(tempList)

				i += 1

	'''
	if pygame.mouse.get_pressed()[0]:
		for item in recList:
			if pygame.mouse.get_pos()[0] > item[3]:
				item[3] += random.uniform(1, 2)
			elif pygame.mouse.get_pos()[0] < item[3]:
				item[3] -= random.uniform(1, 2)

			item[4] -= 1

			if pygame.mouse.get_pos()[1] > item[4]:
				item[4] += random.uniform(1, 2)
			elif pygame.mouse.get_pos()[1] < item[4]:
				item[4] -= random.uniform(1, 2)

			item[5] -= 1
	'''

	pygame.display.update()
	clock.tick(144)

pygame.quit()