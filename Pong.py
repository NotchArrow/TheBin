import pygame
import random

pygame.init()

clock = pygame.time.Clock()
delta = 0

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Pong 0 | 0")

gamemode = "2player" #  "1player", "2player"

paddleOneY = 250
paddleOneScore = 0
paddle1 = pygame.Rect(0, paddleOneY, 25, 100)

paddleTwoY = 250
paddleTwoScore = 0
paddle2 = pygame.Rect(1175, paddleTwoY, 25, 100)

ballX = 575
ballY = 275
ball = pygame.Rect(ballX, ballY, 50, 50)

ballSpeedX = -3
ballSpeedY = -3

def draw_rect(rect):
	pygame.draw.rect(screen, (255, 255, 255), rect)

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0, 0, 0))

	# paddle one stuff
	key = pygame.key.get_pressed()
	if key[pygame.K_w]:
		paddleOneY -= 600 * delta
		if paddleOneY <= 0:
			paddleOneY = 0

	if key[pygame.K_s]:
		paddleOneY += 600 * delta
		if paddleOneY >= 500:
			paddleOneY = 500

	paddle1 = pygame.Rect(0, paddleOneY, 25, 100)
	draw_rect(paddle1)


	# ball stuff
	ballX += ballSpeedX
	ballY += ballSpeedY

	if ball.top < 0 and ballSpeedY < 0:
		ballSpeedY = -ballSpeedY
		ballSpeedX *= random.uniform(1, 1.2)
		ballSpeedY *= random.uniform(1, 1.2)
	if ball.bottom > 600 and ballSpeedY > 0:
		ballSpeedY = -ballSpeedY
		ballSpeedX *= random.uniform(1, 1.2)
		ballSpeedY *= random.uniform(1, 1.2)

	if pygame.Rect.colliderect(ball, paddle1) and ballSpeedX < 0:
		ballSpeedX = -ballSpeedX
		ballSpeedX *= random.uniform(1, 1.2)
		ballSpeedY *= random.uniform(1, 1.2)
		ballX = 25
	if pygame.Rect.colliderect(ball, paddle2) and ballSpeedX > 0:
		ballSpeedX = -ballSpeedX
		ballSpeedX *= random.uniform(1, 1.2)
		ballSpeedY *= random.uniform(1, 1.2)
		ballX = 1125

	ball = pygame.Rect(ballX, ballY, 50, 50)

	if ball.left < 0:
		ballSpeedX = 3
		ballSpeedY = 3
		ballX = 575
		ballY = 275
		paddleTwoScore += 1
		pygame.display.set_caption("Pong " + str(paddleOneScore) + " | " + str(paddleTwoScore))
	if ball.right > 1200:
		ballSpeedX = -3
		ballSpeedY = -3
		ballX = 575
		ballY = 275
		paddleOneScore += 1
		pygame.display.set_caption("Pong " + str(paddleOneScore) + " | " + str(paddleTwoScore))

	ball = pygame.Rect(ballX, ballY, 50, 50)
	draw_rect(ball)


	# paddle two stuff

	if gamemode == "1player":
		if paddleTwoY + 10 < ballY:
			paddleTwoY += 6
		elif paddleTwoY - 10 > ballY:
			paddleTwoY -= 6

		paddle2 = pygame.Rect(1175, paddleTwoY, 25, 100)

		if paddle2.top - 5 < 0:
			paddleTwoY = 0
		if paddle2.bottom + 5 > 600:
			paddleTwoY = 500
	elif gamemode == "2player":
		key = pygame.key.get_pressed()
		if key[pygame.K_UP]:
			paddleTwoY -= 600 * delta
			if paddleTwoY <= 0:
				paddleTwoY = 0

		if key[pygame.K_DOWN]:
			paddleTwoY += 600 * delta
			if paddleTwoY >= 500:
				paddleTwoY = 500

	paddle2 = pygame.Rect(1175, paddleTwoY, 25, 100)
	draw_rect(paddle2)


	# display update
	pygame.display.update()
	delta = clock.tick(60) / 1000

pygame.quit()