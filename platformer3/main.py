import pygame
from soldier import Soldier
from grenade import Grenade
from constants import *
pygame.init()

clock = pygame.time.Clock()
moving_left = False
moving_right = False

bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()

def draw_bg():
    screen.fill((144, 201, 120))
    pygame.draw.line(screen, (255,10,10), (0,300), (SCREEN_WIDTH, 300))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer3")
player = Soldier('player',200, 200, 3, 5, 10, 5)
enemy = Soldier('enemy',400, 200, 3, 5, 10, 5)
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
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_w:
                player.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_g:
                grenade = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade = False  
                grenade_thrown = False 
                   
    draw_bg()
    player.update_animation()            
    player.draw(screen)
    bullet_group.update(player, enemy)
    bullet_group.draw(screen)
    grenade_group.update()
    grenade_group.draw(screen)
    print("shoot********************************", len(bullet_group))
    if player.alive:
        if shoot:
            player.shoot(bullet_group)
        elif grenade and player.grenades > 0 and not grenade_thrown:
            grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction), player.rect.top, player.direction)
            grenade_group.add(grenade)
            player.grenades -= 1
            grenade_thrown = True
            
        if player.in_air:
            player.update_action(2)
        elif moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)        
        player.move(moving_left, moving_right)
    enemy.draw(screen) 
    enemy.update_animation()       
    pygame.display.update()
    clock.tick(FPS)
    