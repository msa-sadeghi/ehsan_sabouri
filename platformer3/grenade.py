from pygame.sprite import Sprite
from constants import grenade_image, SCREEN_WIDTH
class Grenade(Sprite):
    def __init__(self, x,y, direction):
        super().__init__()
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grenade_image
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        
    def update(self):
        self.vel_y += 1
        dx = self.direction * self.speed
        dy = self.vel_y
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0
            
        if self.rect.left + dx <0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed
        self.rect.x += dx
        self.rect.y += dy
        