import pygame


WIDTH = 800
HEIGHT = 640
SIDE_MARGIN = 300
LOWER_MATGIN = 100
ROWS = 16
MAX_COLS = 150
TILE_SIZE = HEIGHT // ROWS
TILE_TYPES = 21
level = 0
scroll = 0
scroll_speed = 1
scroll_left, scroll_right = (False, False)

pine1_image = pygame.image.load("./assets/images/background/pine1.png")
pine2_image = pygame.image.load("./assets/images/background/pine2.png")
mountain_image = pygame.image.load("./assets/images/background/mountain.png")
sky_image = pygame.image.load("./assets/images/background/sky_cloud.png")

image_list = [
    pygame.transform.scale(
        pygame.image.load(f"./assets/images/tile/{i}.png") ,
        (TILE_SIZE, TILE_SIZE)
    )
    for i in range(21)
]

def draw_bg():
    screen.fill("green")
    width = sky_image.get_width()
    for i in range(4):
        screen.blit(sky_image, (i * width - scroll * 0.4, 0))
        screen.blit(mountain_image, (i * width - scroll * 0.5, HEIGHT - mountain_image.get_height() - 300))
        screen.blit(pine1_image, (i * width - scroll * 0.6, HEIGHT - pine1_image.get_height() - 150))
        screen.blit(pine2_image, (i * width - scroll * 0.7, HEIGHT - pine2_image.get_height() ))

screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MATGIN))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True  
            if event.key == pygame.K_RIGHT:
                scroll_right = True  
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False  
            if event.key == pygame.K_RIGHT:
                scroll_right = False  
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1 
    draw_bg()
    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right:
        scroll += 5 * scroll_speed
    pygame.display.update()
    clock.tick(FPS)