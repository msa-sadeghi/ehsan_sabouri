from constants import *
import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, x,y, move_x, move_y):
        super().__init__()
        image = pygame.image.load("assets/platform.png")
        self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = move_x
        self.move_y = move_y
        self.direction = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.direction * self.move_x
        self.rect.y += self.direction * self.move_y
        self.counter += 1
        if self.counter > TILE_SIZE:
            self.direction *= -1
            self.counter *= -1

