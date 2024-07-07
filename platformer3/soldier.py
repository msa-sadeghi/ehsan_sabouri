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
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx -= 5
        if moving_right:
            dx += 5
            
        self.rect.x += dx
        self.rect.y += dy
                
            