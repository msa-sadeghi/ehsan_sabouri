from pygame.sprite import Sprite
import pygame
import math

from enemy import Enemy

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("img/bg.png")
castle_img_100 = pygame.image.load("img/castle/castle_100.png")
bullet_img = pygame.image.load("img/bullet.png")
pygame.display.set_caption("castle game")
bullet_group = pygame.sprite.Group()
fire_sound = pygame.mixer.Sound("img/jump.wav")

enemy_animations = []
enemy_types = ['knight']
enemy_health = [75]

animation_types = ['walk', 'attack', 'death']

for enemy in enemy_types:
    animation_list = []
    for animation in animation_types:
        temp_list = []
        for i in range(20):
            img = pygame.image.load(f"img/enemies/{enemy}/{animation}/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height()*0.2))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)
            
print(enemy_animations[0])        




class Castle:
    def __init__(self, image100, x, y, scale):
        self.health = 1000
        self.max_health = self.health

        self.image100 = pygame.transform.scale(image100, (image100.get_width() * scale, image100.get_height() * scale))
        self.rect = self.image100.get_rect(topleft=(x, y))
        self.fired = False
        self.last_shoot_time = pygame.time.get_ticks()

    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def shoot(self):
        mouse_position = pygame.mouse.get_pos()
        x_dist = mouse_position[0] - self.rect.midleft[0]
        y_dist = -(mouse_position[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        if pygame.mouse.get_pressed()[0] and not self.fired and pygame.time.get_ticks() - self.last_shoot_time > 400:
            self.fired = True
            fire_sound.play()
            self.last_shoot_time = pygame.time.get_ticks()
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
        


class Bullet(Sprite):
    def __init__(self, image, x, y, angle):
        super().__init__()
        self.image = pygame.transform.scale(image, (image.get_width() * 0.1, image.get_height() * 0.1))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.angle = angle
        self.speed = 10
        self.dx = self.speed * math.cos(self.angle)
        self.dy = -self.speed * math.sin(self.angle)

    def update(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        self.rect.x += self.dx
        self.rect.y += self.dy

enemy_group = pygame.sprite.Group()
enemy_1 = Enemy(enemy_health[0],enemy_animations[0], 200, SCREEN_HEIGHT-100, 1)
enemy_group.add(enemy_1)


castle = Castle(castle_img_100, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    castle.draw()
    castle.shoot()
    bullet_group.update()
    bullet_group.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update(screen, castle, bullet_group)
    pygame.display.update()
    clock.tick(FPS)
