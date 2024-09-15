import pygame, random, PauseButtons

pygame.init()

#CONSTANTS
SCREEN_WIDTH = 1820 #1820
SCREEN_HEIGHT = 980 #980

#VARIABLES
xVelocity = 0
yVelocity = 0
xPrevious = 0
yPrevious = 0
score = 0

#SETUP
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Pygame")
clock = pygame.time.Clock()
game_paused = False
pausemenu_state = "main"

player = pygame.Rect((50, 50, 50, 50))
rec2 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
rec3 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
rec4 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
rec5 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
rec6 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
rec7 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
object_list = [rec2, rec3, rec4, rec5, rec6, rec7]
goal = pygame.Rect((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 20, 20))

#text setup
font = pygame.font.SysFont("arialblack", 40)
TEXT_COLOR = (255, 255, 255)

def draw_text(text, font, TEXT_COLOR, x, y):
	img = font.render(text, True, TEXT_COLOR)
	screen.blit(img, (x, y))

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load("images/button_video.png").convert_alpha()
audio_img = pygame.image.load("images/button_audio.png").convert_alpha()
keys_img = pygame.image.load("images/button_keys.png").convert_alpha()
back_img = pygame.image.load("images/button_back.png").convert_alpha()

#create button instances
resume_button = PauseButtons.Button(100, 125, resume_img, 1)
options_button = PauseButtons.Button(100, 250, options_img, 1)
quit_button = PauseButtons.Button(100, 375, quit_img, 1)
video_button = PauseButtons.Button(304, 125, video_img, 1)
audio_button = PauseButtons.Button(304, 250, audio_img, 1)
keys_button = PauseButtons.Button(304, 375, keys_img, 1)
back_button = PauseButtons.Button(304, 500, back_img, 1)

#game loop
run = True
while run:

	screen.fill((0, 0, 0))

  #key events
	xVelocity = 0
	yVelocity = 0
	key = pygame.key.get_pressed()
	if key[pygame.K_a] and player.left != 0:
		xVelocity = -10
	if key[pygame.K_d] and player.right != SCREEN_WIDTH:
		xVelocity = 10
	if key[pygame.K_w] and player.bottom != 0:
		yVelocity = -10
	if key[pygame.K_s] and player.bottom != SCREEN_HEIGHT:
		yVelocity = 10

	#pause menu
	if key[pygame.K_ESCAPE] and game_paused == False:
		game_paused = True

	if game_paused:
		if pausemenu_state == "main":
			if resume_button.draw(screen):
				game_paused = False
			if options_button.draw(screen):
				pausemenu_state = "options"
			if quit_button.draw(screen):
				run = False
		
		elif pausemenu_state == "options":
			if video_button.draw(screen):
				print("Video Settings")
			if audio_button.draw(screen):
				print("Audio Settings")
			if keys_button.draw(screen):
				print("Key bindings")
			if back_button.draw(screen):
				pausemenu_state = "main"

	else:
		draw_text("Press ESCAPE to pause", font, TEXT_COLOR, 50, 50)
		draw_text("Score: " + str(score), font, TEXT_COLOR, 700, 50)

  #game quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

  #movement and collision check
	xPrevious = player.x
	yPrevious = player.y

	player.x += xVelocity
	player.y += yVelocity

	if player.collidelist(object_list) != -1:
		player.x = xPrevious
		player.y = yPrevious
	if player.colliderect(goal):
		score += 1
		rec2 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		rec3 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		rec4 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		rec5 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		rec6 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		rec7 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
		object_list = [rec2, rec3, rec4, rec5, rec6, rec7]
		while player.collidelist(object_list) != -1:
			print("collided")
			rec2 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			rec3 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			rec4 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			rec5 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			rec6 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			rec7 = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(10, 300), random.randint(10, 300)))
			object_list = [rec2, rec3, rec4, rec5, rec6, rec7]
		goal = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), 20, 20))
	while goal.collidelist(object_list) != -1:
		goal = pygame.Rect((random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), 20, 20))

	#drawing rectangles
	pygame.draw.rect(screen, (125, 125, 250), player)
	pygame.draw.rect(screen, (125, 125, 125), rec2)
	pygame.draw.rect(screen, (125, 125, 125), rec3)
	pygame.draw.rect(screen, (125, 125, 125), rec4)
	pygame.draw.rect(screen, (125, 125, 125), rec5)
	pygame.draw.rect(screen, (125, 125, 125), rec6)
	pygame.draw.rect(screen, (125, 125, 125), rec7)
	pygame.draw.rect(screen, (0, 125, 0), goal)

  #FPS and display refresh
	clock.tick(60)
	pygame.display.update()

pygame.quit()