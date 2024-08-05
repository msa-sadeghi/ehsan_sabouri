import pygame
import os
from soldier import Solider
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()
bullet_group = pygame.sprite.Group()
player = Solider("player", 100, 300, 20, 10)
moving_left = False
moving_right = False
shoot = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
                player.idle = False
            if event.key == pygame.K_RIGHT:
                moving_right = True
                player.idle = False
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_s:
                shoot = True
                  
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
                player.idle = True
            if event.key == pygame.K_RIGHT:
                moving_right = False
                player.idle = True
            if event.key == pygame.K_SPACE:
                player.jump = False
            if event.key == pygame.K_s:
                shoot = False
        
    screen.fill((0,0,0))
    player.draw(screen) 
    player.move(moving_left, moving_right)  
    if shoot:
        player.shoot(bullet_group)
        shoot = False
    if moving_left or moving_right:
        player.set_action(1)
   
        
    else:
        player.set_action(0)
    bullet_group.update()
    bullet_group.draw(screen)
    player.animation()    
    pygame.display.update()
    clock.tick(FPS)

os.system("cls")