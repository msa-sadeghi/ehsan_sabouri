import pygame
from soldier import Soldier
from constants import *
pygame.init()

clock = pygame.time.Clock()
moving_left = False
moving_right = False


def draw_bg():
    screen.fill((144, 201, 120))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer3")
player = Soldier('player',200, 200, 3, 5)
s2 = Soldier('enemy',400, 200, 3, 5)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
        
                
    player.move(moving_left, moving_right)
    draw_bg()
    player.draw(screen)        
    s2.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)
    