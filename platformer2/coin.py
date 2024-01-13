from constants import *
import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self, x,y):
        super().__init__()
        image = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale(image, (TILE_SIZE/3, (TILE_SIZE/3) * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y