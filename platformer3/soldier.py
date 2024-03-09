from pygame.sprite import Sprite
import pygame

class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale, speed):
        super().__init__()
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        animation_types = 
        img = pygame.image.load(f"assets/images/{self.char_type}/Idle/0.png")
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height()* scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx -= self.speed
            self.direction = -1
            self.flip = True
            
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False
            
        self.rect.x += dx
        self.rect.y += dy