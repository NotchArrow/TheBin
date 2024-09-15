import pygame, random

pygame.init()

#CONSTANTS
SCREEN_WIDTH = 500 #1820
SCREEN_HEIGHT = 500 #980
GRAVITY = 1
SPEED = 10
ACCELERATION = 5
DEACCELERATION = 2

#VARIABLES
xVelocity = 0
yVelocity = 0
colorChange = False
red = 0
blue = 0
green = 0
canJump = True

#SETUP
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = pygame.Rect((300, 250, 50, 50))
rec2 = pygame.Rect((400, SCREEN_HEIGHT - 10, 50, 50))
rec3 = pygame.Rect((0, SCREEN_HEIGHT - 400, 10, 400))

#INTITIALIZATION
run = True
while run:

	#Drawing rectangles and screen fill
	screen.fill((0, 0, 0))
	
	pygame.draw.rect(screen, (red, blue, green), player)
	pygame.draw.rect(screen, (red, blue, green), rec2)
	pygame.draw.rect(screen, (red, blue, green), rec3)
	
	if xVelocity < 0:
		xVelocity += DEACCELERATION
	elif xVelocity > 0:
		xVelocity -= DEACCELERATION

	#Key events
	key = pygame.key.get_pressed()
	if key[pygame.K_a] and player.left > 0:
		xVelocity -= ACCELERATION
	if key[pygame.K_d] and player.right < SCREEN_WIDTH:
		xVelocity += ACCELERATION
	if key[pygame.K_w] and canJump:
		yVelocity = -25
		canJump = False
	
	if xVelocity > SPEED:
		xVelocity = SPEED
	elif xVelocity < -SPEED:
		xVelocity = -SPEED
	
	yVelocity += GRAVITY
	
	if key[pygame.K_a] and player.left == 0:
		xVelocity = 0
		yVelocity = 0
		canJump = True
	elif key[pygame.K_d] and player.right == SCREEN_WIDTH:
		xVelocity = 0
		yVelocity = 0
		canJump = True
		
	#Ceiling
	if player.top + yVelocity < 0:
		player.top = 0
		yVelocity = 0
		canJump = True
	
	#Floor
	if player.bottom != SCREEN_HEIGHT:
		colorChange = True

	if player.bottom + yVelocity > SCREEN_HEIGHT:
		player.bottom = SCREEN_HEIGHT
		yVelocity = 0

	if player.bottom == SCREEN_HEIGHT and colorChange == True:
		red = random.randint(0, 255)
		blue = random.randint(0, 255)
		green = random.randint(0, 255)
		colorChange = False
		canJump = True

	#Trampoline
	if pygame.Rect.colliderect(player, rec2):
		yVelocity = -30
	
	#Slide
	if pygame.Rect.colliderect(player, rec3) and player.bottom != SCREEN_HEIGHT:
		yVelocity = 1
		CanJump = True

	#Wall Collision Check
	if player.left + xVelocity < 0:
		player.left = 0
		xVelocity = 0
	elif player.right + xVelocity > SCREEN_WIDTH:
		player.right = SCREEN_WIDTH
		xVelocity = 0
	
	#Movement
	player.move_ip(xVelocity, yVelocity)

	#Game quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#FPS and display refresh
	clock.tick(60)
	pygame.display.update()

pygame.quit()