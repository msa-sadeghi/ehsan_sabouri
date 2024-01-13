import pygame
from coin import Coin
from constants import *
from enemy import Enemy
from lava import Lava
from door import Door
from platform_ import Platform

class World:
    def __init__(self, data, enemy_group, lava_group, door_group, coin_group,platform_group):
        self.tile_list = []
        dirt_img = pygame.image.load("assets/dirt.png")
        grass_img = pygame.image.load("assets/grass.png")
        self.enemy_group = enemy_group
        self.lava_group = lava_group
        self.door_group = door_group
        self.coin_group = coin_group
        self.platform_group = platform_group

        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 1:
                    img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.topleft = (col * TILE_SIZE, row * TILE_SIZE)
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 2:
                    img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.topleft = (col * TILE_SIZE, row * TILE_SIZE)
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 3:
                    enemy = Enemy(col * TILE_SIZE, row * TILE_SIZE + 15)
                    self.enemy_group.add(enemy)
                if data[row][col] == 4:
                    door = Door(col * TILE_SIZE, row * TILE_SIZE + 20)
                    self.door_group.add(door)
                if data[row][col] == 5:
                    coin = Coin(col * TILE_SIZE, row * TILE_SIZE + 20)
                    self.coin_group.add(coin)
                if data[row][col] == 6:
                    lava = Lava(col * TILE_SIZE, (row+1) * TILE_SIZE)
                    self.lava_group.add(lava)
                if data[row][col] == 7:
                    platform = Platform(col * TILE_SIZE, row * TILE_SIZE, 1, 0)
                    self.platform_group.add(platform)
                if data[row][col] == 8:
                    platform = Platform(col * TILE_SIZE, row * TILE_SIZE, 0, 1)
                    self.platform_group.add(platform)

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        
