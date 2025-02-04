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



screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MATGIN))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
    pygame.display.update()
    clock.tick(FPS)