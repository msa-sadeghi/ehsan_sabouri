#_____________________________________#/ In The Name Of God \#_____________________________________#
#____________#/Library\#___________#
import pygame
from pygame.sprite import Sprite
import math
from enemy import Enemy
from crosshair import Crosshair
pygame.init()
W_Width = 800
W_Height = 600
Dis_Sur = pygame.display.set_mode((W_Width,W_Height))
Clock = pygame.time.Clock()
FPS = 60
#____________/#/Groups\#_____________#
Enemy_Group = pygame.sprite.Group()
#____________/#/Values\#_____________#
Background_Image = pygame.image.load('img/bg.png')
Castle_Img_100 = pygame.image.load('img/castle/castle_100.png')
Castle_Img_50 = pygame.image.load('img/castle/castle_100.png')
Castle_Img_25 = pygame.image.load('img/castle/castle_100.png')
Bullet_Img = pygame.image.load('img/bullet.png')
pygame.display.set_caption('The Castle War Ages')
Bullet_Group = pygame.sprite.Group()
Enemy_Animation = []
#________________#/Knight Commons\#_________________#
Enemy_Types = ['knight']
Enemy_Health_Knight = [75]
A_Knight_Types = ['walk','attack','death']
for enemy in Enemy_Types:
    Animation_List = []
    for Animation in A_Knight_Types:
        Temp_List = []
        for i in range(20):
            Image = pygame.image.load(f'img/enemies/{enemy}/{Animation}/{i}.png')
            Image = pygame.transform.scale(Image,(Image.get_width() * 0.3,Image.get_height() * 0.3))
            Temp_List.append(Image)
        Animation_List.append(Temp_List)
    Enemy_Animation.append(Animation_List)
    print(Enemy_Animation[0])
#___________#/Sounds\#______________#
# CFire_Sound = pygame.mixer.Sound('img\Far-Single-Gunshot.mp3')
#___________#/Class\#______________#
class Bullet(Sprite):
    def __init__(self,image,x,y,angle):
        super().__init__()
        self.image = pygame.transform.scale(image,(image.get_width() * 0.1,image.get_height() * 0.1))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.angle = angle
        self.speed = 10
        self.dx = self.speed * math.cos(self.angle)
        self.dy = -self.speed * math.sin(self.angle)

    def update(self):
        if self.rect.right < 0 or self.rect.left > W_Width or self.rect.bottom < 0 or self.rect.top > W_Height:
            self.kill()
        self.rect.x += self.dx
        self.rect.y += self.dy

Enemy_Knight = Enemy(Enemy_Health_Knight[0],Enemy_Animation[0],200,W_Height - 100,1)
Enemy_Group.add(Enemy_Knight)
CroosChair = Crosshair(0.03)
class Castle:
    def __init__(self,Image100,Image50,Image25,X,Y,Scale):
        self.Health = 1000
        self.Max_Health = self.Health
        self.Coin = 0
        self.Points = 0
        self.Image100 = pygame.transform.scale(Image100,(Image100.get_width() * Scale, Image100.get_height()* Scale))     
        self.Image50 = pygame.transform.scale(Image50,(Image100.get_width() * Scale, Image100.get_height()* Scale))     
        self.Image25 = pygame.transform.scale(Image25,(Image100.get_width() * Scale, Image100.get_height()* Scale))     
        self.rect = self.Image100.get_rect(topleft = (X,Y))
        self.fired = False    
        self.last_Shoot_Time = pygame.time.get_ticks()
    def draw(self):
        if self.Health <= 250:
            self.image = self.Image25
        if self.Health <= 500:
            self.image = self.Image50
        else:
            self.image = self.Image100
        Dis_Sur.blit(self.image,self.rect)
    def Shotting(self):
        Mouse_Pos = pygame.mouse.get_pos()
        x_Dis = Mouse_Pos[0] - self.rect.midleft[0]
        y_Dis = -(Mouse_Pos[1] - self.rect.midleft[1])
        self.Angle = math.atan2(y_Dis,x_Dis)
        if pygame.mouse.get_pressed()[0] and not self.fired and pygame.time.get_ticks() - self.last_Shoot_Time > 400:
            self.fired = True
            # CFire_Sound.play()
            self.last_Shoot_Time = pygame.time.get_ticks()
            bullet = Bullet(Bullet_Img,self.rect.midleft[0],self.rect.midleft[1],self.Angle)
            Bullet_Group.add(bullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
castle = Castle(Castle_Img_100,Castle_Img_50,Castle_Img_25,W_Width - 250,W_Height - 300,0.2)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Dis_Sur.blit(Background_Image,(0,0))
    castle.draw()
    castle.Shotting()
    CroosChair.draw(Dis_Sur)
    Bullet_Group.update()
    Bullet_Group.draw(Dis_Sur)
    Enemy_Group.draw(Dis_Sur)
    Enemy_Group.update(castle,Bullet_Group)
    pygame.display.update()
    Clock.tick(FPS)