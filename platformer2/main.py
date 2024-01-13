import pygame
import os
import pickle
from constants import *
from world import World
from button import Button

from player import Player

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
level_number = 1
max_level = 2
game_font48 = pygame.font.Font("assets/AttackGraffiti.ttf", 48)


if os.path.exists(f"levels/level{level_number}"):
    with open(f"levels/level{level_number}", 'rb') as f:
        world_data = pickle.load(f)




clock = pygame.time.Clock()

exit_btn_image = pygame.image.load("assets/exit_btn.png")
exit_btn_image = pygame.transform.scale(exit_btn_image, (120,42))
restart_btn_image = pygame.image.load("assets/restart_btn.png")
start_btn_image = pygame.image.load("assets/start_btn.png")
start_btn_image = pygame.transform.scale(start_btn_image, (120,42))


exit_button = Button(screen_width/2 - exit_btn_image.get_width(),screen_height/2, exit_btn_image)
start_button = Button(screen_width/2 + restart_btn_image.get_width(),screen_height/2, start_btn_image)
restart_button = Button(screen_width/2 + restart_btn_image.get_width(),screen_height/2, restart_btn_image)

enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
player = Player(100,screen_height-100, enemy_group, lava_group)
world = World(world_data,enemy_group, lava_group, door_group, coin_group, platform_group)



bg_img = pygame.image.load("assets/sky.png")
sun_img = pygame.image.load("assets/sun.png")

def draw_grid():
    for i in range(14):
        pygame.draw.line(screen,(255,10,170), (0,i*50), (screen_width,i*50))
    for i in range(20):
        pygame.draw.line(screen,(255,10,170), (i*50,0), (i*50,screen_height))


def draw_text(text):
    text = game_font48.render(text, True, (190,10,240))
    rect = text.get_rect(center = (screen_width/2, screen_height/2))
    screen.blit(text, rect)


def reset_level(level):
    enemy_group.empty()
    lava_group.empty()
    door_group.empty()
    coin_group.empty()
    platform_group.empty()
    player.reset(100,screen_height-100, enemy_group, lava_group)
    if os.path.exists(f"levels/level{level}"):
        level_file = open(f"levels/level{level}", "rb")
        world_data = pickle.load(level_file)
    world = World(world_data,enemy_group, lava_group, door_group, coin_group,platform_group)
    return world




game_status = "playing"
player_hidden = False
main_menu = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    
    if main_menu:
        if exit_button.draw(screen):
            running = False
        if start_button.draw(screen):
            main_menu = False

    else:
        if pygame.time.get_ticks() - start_button.last_clicked_time > 2000:

            world.draw(screen)
            screen.blit(sun_img, (100,100))
            game_status,player_hidden = player.update(world.tile_list,game_status,player_hidden, door_group, platform_group)
            if not player_hidden:
                player.draw(screen)
            if game_status == "gameover":
                if player_hidden:
                    if restart_button.draw(screen):
                        player.reset(100,screen_height-100, enemy_group, lava_group)
                        player_hidden = False
                        game_status = "playing"
                    if exit_button.draw(screen) and player_hidden:
                        running = False

            elif game_status == "next_level":
                level_number += 1
                if level_number <= max_level:

                    game_status = "playing"
                    world_data = []
                    world = reset_level(level_number)

                else:
                    draw_text("You Win!")
                    if restart_button.draw(screen):
                        level_number = 1
                        world_data = []
                        world = reset_level(level_number)
                        game_status = "playing"
                        score = 0 



            
            elif game_status == "playing":
                enemy_group.update()
            enemy_group.draw(screen)
            lava_group.update()
            lava_group.draw(screen)
            door_group.draw(screen)
            coin_group.draw(screen)
            platform_group.update()
            platform_group.draw(screen)
        else:
            draw_text(f"Welcome to level {level_number}")


    pygame.display.update()
    clock.tick(FPS)

