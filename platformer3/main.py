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
grenade_group = pygame.sprite.Group()
player = Solider("player", 100, 300, 20, 10)
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False
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
            if event.key == pygame.K_g:
                grenade = True
                
                
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
            if event.key == pygame.K_g:
                grenade = False
                grenade_thrown = False
        
    screen.fill((0,0,0))
    player.draw(screen) 
    player.move(moving_left, moving_right)  
    if shoot:
        player.shoot("bullet", bullet_group)
        shoot = False
    elif grenade and not grenade_thrown:
        player.shoot("grenade", grenade_group)
        grenade_thrown = True
    if moving_left or moving_right:
        player.set_action(1)
    elif player.in_air:
        player.set_action(2)
        
    else:
        player.set_action(0)
    bullet_group.update()
    bullet_group.draw(screen)
    grenade_group.update()
    grenade_group.draw(screen)
    player.animation()    
    pygame.display.update()
    clock.tick(FPS)

os.system("cls")