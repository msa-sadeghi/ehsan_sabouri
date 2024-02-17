#_____________________________________#/ In The Name Of God \#_____________________________________#
from pygame.sprite import Sprite
import pygame
#_______________________________
class Enemy(Sprite):
    def __init__(self,Health,Animation_List,X,Y,speed):
        super().__init__()
        self.Alive = True
        self.speed = speed
        self.Health = Health
        self.Last_Attack = pygame.time.get_ticks()
        self.Animation_List = Animation_List
        self.Frame_Index = 0
        self.Action = 0
        self.Attack_Cooldown = 1000
        self.Update_Time = pygame.time.get_ticks()
        self.image = self.Animation_List[self.Action][self.Frame_Index]
        self.rect = self.image.get_rect()
        self.rect.center = (X,Y)
    def update(self,target,Bullet_Group):
        if self.Alive:
            if pygame.sprite.spritecollide(self,Bullet_Group,True):
                self.Health -= 25
            if self.rect.right > target.rect.left:
                self.update_Animation(1)
            if self.Action == 0:
                self.rect.x +=self.speed
            if self.Action == 1:
                if pygame.time.get_ticks()-self.Last_Attack > 200:
                    target.Health -= 25
                    if target.Health < 0:
                        target.Health = 0
                    self.Last_Attack = pygame.time.get_ticks()
            if self.Health <= 0:
                target.Coin += 100
                target.Points += 100
                # self.update_action(2)
                self.Alive = False

        self.update_Animation()
    def update_Animation(self):
        self.image = self.Animation_List[self.Action][self.Frame_Index]
        if pygame.time.get_ticks() - self.Update_Time > 50:
            self.Update_Time = pygame.time.get_ticks()
            self.Frame_Index += 1
        if self.Frame_Index >= len(self.Animation_List[self.Action]):
            if self.Action == 2:
                self.Frame_Index = len(self.Animation_List[self.Action])

            else:
                self.Frame_Index = 0