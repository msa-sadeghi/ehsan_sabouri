from pygame.sprite import Sprite
import pygame
import os

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
        animation_types = ('Idle', 'Run', 'Jump', 'Death')
        for animation in animation_types:
            for_any_animation_type = []
            number_of_images = len(os.listdir(f'./assets/images/{self.char_type}/{animation}'))
            for i in range(number_of_images):
                img = pygame.image.load(f"./assets/images/{self.char_type}/{animation}/0.png")
                img = pygame.transform.scale(img, (img.get_width()* scale, img.get_height()* scale))
                for_any_animation_type.append(img)
            self.animation_list.append(for_any_animation_type)
            
            
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def move(self, moving_left, moving_right):
        #TODO add jump and animations
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