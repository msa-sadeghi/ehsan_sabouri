from pygame.sprite import Sprite
import pygame
import math
from random import randint
from enemy import Enemy
from crosshair import Crosshair
from button import Button
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

level = 1
level_difficulty = 0
target_difficulty = 1000
ENEMY_TIMER = 1000
DIFFICULTY_MULTIPLIER = 1.1
game_over = False
next_level = False


max_towers = 4
TOWER_COST = 100

tower_positions = [
    (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 200),
    (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 150),
    (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 150),
    (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150),
]


last_enemy = pygame.time.get_ticks()
level_reset_time = pygame.time.get_ticks()
enemies_alive = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("img/bg.png")
castle_img_100 = pygame.image.load("img/castle/castle_100.png")
castle_width = castle_img_100.get_width()
castle_height = castle_img_100.get_height()
castle_img_50 = pygame.transform.scale(pygame.image.load("img/castle/castle_50.png"), (castle_width, castle_height))
castle_img_25 = pygame.transform.scale(pygame.image.load("img/castle/castle_25.png"), (castle_width, castle_height))

tower_img_100 = pygame.image.load("img/tower/tower_100.png")
tower_width = tower_img_100.get_width()
tower_height = tower_img_100.get_height()
tower_img_50 = pygame.transform.scale(pygame.image.load("img/tower/tower_50.png"), (tower_width, tower_height))
tower_img_25 = pygame.transform.scale(pygame.image.load("img/tower/tower_25.png"), (tower_width, tower_height))

bullet_img = pygame.image.load("img/bullet.png")
pygame.display.set_caption("castle game")
bullet_group = pygame.sprite.Group()
fire_sound = pygame.mixer.Sound("img/jump.wav")

enemy_animations = []
enemy_types = ['knight', 'goblin', 'purple_goblin', 'red_goblin']
enemy_health = [75, 100, 125, 150]

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
            
 
repair_img = pygame.transform.scale(pygame.image.load("img/repair.png"), (32,32))
armour_img = pygame.transform.scale(pygame.image.load("img/armour.png"), (32,32))


def draw_text(text, font, color, x,y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

f = pygame.font.SysFont('Terminal', 28)

def show_info():
    draw_text(f'Money: {castle.money}', f, (0,0,0), 20, 20)
    draw_text(f'Score: {castle.score}', f, (0,0,0), 180, 20)
    draw_text(f'Level: {level}', f, (0,0,0), 320, 20)
    draw_text(f'Health: {castle.health}', f, (0,0,0), 460, 20)




class Castle:
    def __init__(self, image100,image50, image25, x, y, scale):
        self.health = 1000
        self.max_health = self.health
        self.money = 0
        self.score = 0
        self.image100 = pygame.transform.scale(image100, (image100.get_width() * scale, image100.get_height() * scale))
        self.image50 = pygame.transform.scale(image50, (image50.get_width() * scale, image50.get_height() * scale))
        self.image25 = pygame.transform.scale(image25, (image25.get_width() * scale, image25.get_height() * scale))
        self.rect = self.image100.get_rect(topleft=(x, y))
        self.fired = False
        self.last_shoot_time = pygame.time.get_ticks()

    def draw(self):
        
        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def shoot(self):
        mouse_position = pygame.mouse.get_pos()
        x_dist = mouse_position[0] - self.rect.midleft[0]
        y_dist = -(mouse_position[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        if pygame.mouse.get_pressed()[0] and not self.fired and pygame.time.get_ticks() - self.last_shoot_time > 400 and mouse_position[1] > 70:
            self.fired = True
            fire_sound.play()
            self.last_shoot_time = pygame.time.get_ticks()
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False
            
    def repair(self):
        if self.money >= 1000 and self.health <= self.max_health:
            self.health += 500
            self.money -= 1000
            if self.health > self.max_health:
                self.health = self.max_health
                
    def armour(self):
        if self.money >= 500:
            self.max_health += 250
            self.money -= 500
        

class Tower(Sprite):
    def __init__(self, image100, image50, image25, x,y, scale):
        super().__init__()
        self.image100 = pygame.transform.scale(image100, (tower_width * scale, tower_height * scale))
        self.image50 = pygame.transform.scale(image50, (tower_width * scale, tower_height * scale))
        self.image25 = pygame.transform.scale(image25, (tower_width * scale, tower_height * scale))
        self.image = self.image100
        self.rect = self.image.get_rect(topleft = (x,y))
        
        self.angle = 0
        self.last_shot = pygame.time.get_ticks()
        self.got_target = False
        
    def update(self, enemy_group):
        self.got_target = False
        for enemy in enemy_group:
            if enemy.alive:
                self.got_target = True
                target_x, target_y = enemy.rect.midbottom
                break
        if self.got_target:
            y_distance = -(target_y - self.rect.midleft[1])
            x_distance = target_x - self.rect.midleft[0]
            self.angle = math.atan2(y_distance, x_distance)
            if pygame.time.get_ticks() - self.last_shot > 1000:
                self.last_shot = pygame.time.get_ticks()
                bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
                bullet_group.add(bullet)
        
        if castle.health <= 250:
            self.image = self.image25
        elif castle.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100
            
            
            
        




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
tower_group = pygame.sprite.Group()


crosshair = Crosshair(0.03)

castle = Castle(castle_img_100,castle_img_50, castle_img_25, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)

repair_button = Button(SCREEN_WIDTH - 120, 20, repair_img)
armour_button = Button(SCREEN_WIDTH - 75, 20, armour_img)
tower_button = Button(SCREEN_WIDTH - 15, 20, pygame.transform.scale(tower_img_100, (32,32)))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    show_info()
    castle.draw()
    castle.shoot()
    crosshair.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    tower_group.update(enemy_group)
    tower_group.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update(screen, castle, bullet_group)
    if repair_button.draw(screen):
        castle.repair()
    if armour_button.draw(screen):
        castle.armour()
        
    if tower_button.draw(screen):
        if castle.money >= 100 and len(tower_group) < max_towers:
            tower = Tower(tower_img_100,
                          tower_img_50,
                          tower_img_25,
                          tower_positions[len(tower_group)][0],
                          tower_positions[len(tower_group)][1],
                          0.2
                          )
            tower_group.add(tower)
            castle.money -= TOWER_COST
    if level_difficulty < target_difficulty:
        if pygame.time.get_ticks() - last_enemy > ENEMY_TIMER:
            i = randint(0, len(enemy_types) - 1)
            enemy = Enemy(enemy_health[i], enemy_animations[i], -100, SCREEN_HEIGHT-100, 1)
            enemy_group.add(enemy)
            last_enemy = pygame.time.get_ticks()
            level_difficulty += enemy_health[i]
    if level_difficulty >= target_difficulty:
        enemies_alive = 0
        for enemy in enemy_group:
            if enemy.alive:
                enemies_alive += 1
        if enemies_alive == 0 and not next_level:
            next_level = True
            level_reset_time = pygame.time.get_ticks()
    if next_level:
        # draw_text()
        if pygame.time.get_ticks() - level_reset_time > 2000:
            next_level = False
            level += 1
            last_enemy = pygame.time.get_ticks()
            target_difficulty *= DIFFICULTY_MULTIPLIER
            level_difficulty = 0
            enemy_group.empty()
        
    pygame.display.update()
    clock.tick(FPS)
