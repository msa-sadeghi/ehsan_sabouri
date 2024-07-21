from pygame.sprite import Sprite
import pygame
import os

class Solider(Sprite):
    def __init__(self, type, x,y, ammo, grenade):
        super().__init__()
        self.animation_types = ("Idle", "Run", "Jump", "Death")
        self.all_images = []
        for anim in self.animation_types:
            temp = []
            n = len(os.listdir(f"assets/images/{type}/{anim}"))
            for i in range(n):
                img = pygame.image.load(f"assets/images/{type}/{anim}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 3, img_h * 3))
                temp.append(img)
            self.all_images.append(temp)
            
        self.action = 0
        self.image_number = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.health = 100
        self.max_health = 100
        self.ammo = ammo
        self.grenade = grenade
        self.last_update = 0
        self.jump = False
        self.flip = False
        self.vel_y = 0
        
    def draw(self, screen):
        self.image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image, self.rect)
        
    def move(self, moving_left, moving_right):
        print(self.jump)
        dx = 0
        dy = 0
        if moving_left:
            dx -= 5
            self.flip = True
            
        if moving_right:
            dx += 5
            self.flip = False
        if self.jump:
            
            self.vel_y = -13
        dy += self.vel_y
        self.vel_y += 1  
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.vel_y = 0 
        self.rect.x += dx
        self.rect.y += dy
    def animation(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_update > 100:
            self.last_update = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images):
                self.image_number = 0
                
    def set_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0
        
        
            