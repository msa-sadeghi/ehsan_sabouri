from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        self.speed = 7
        self.vel_y = -11
        self.timer = 100
        group.add(self)
        
    def update(self):
        dx = self.direction * self.speed
        dy = self.vel_y
        
        self.vel_y += 1
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            dx = 0
        if self.rect.left + dx < 0 or self.rect.right + dx > 800:
            self.direction *= -1
        
        self.rect.x += dx
        self.rect.y += dy
        self.timer -= 1