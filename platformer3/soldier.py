from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet

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
        self.shoot_cooldown = 20
        self.ammo = 10
        self.health = 100
        self.update_time = pygame.time.get_ticks()
        animation_types = ('Idle', 'Run', 'Jump', 'Death')
        for animation in animation_types:
            for_any_animation_type = []
            number_of_images = len(os.listdir(f'./assets/images/{self.char_type}/{animation}'))
            for i in range(number_of_images):
                img = pygame.image.load(f"./assets/images/{self.char_type}/{animation}/{i}.png")
                img = pygame.transform.scale(img, (img.get_width()* scale, img.get_height()* scale))
                for_any_animation_type.append(img)
            self.animation_list.append(for_any_animation_type)
            
            
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.frame_index = 0
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
        self.check_alive()
    
    def update_action(self, new_action)   :
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
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
            
        if self.jump and not self.in_air:
            self.vel_y = -12
            self.jump = False
            self.in_air = True
        dy += self.vel_y
        self.vel_y += 1   
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False 
            
        self.rect.x += dx
        self.rect.y += dy
    def check_alive(self)    :
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)
    def shoot(self, group)  :
        if self.ammo>0 and self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            
            self.ammo -= 1
            Bullet(self.rect.centerx + 0.6 * self.rect.size[0] * self.direction, self.rect.centery,\
                self.direction, group)
            