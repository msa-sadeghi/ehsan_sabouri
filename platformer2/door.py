from constants import *
import pygame
from pygame.sprite import Sprite
class Door(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("assets/exit.png")
        self.rect = self.image.get_rect(topleft = (x,y))