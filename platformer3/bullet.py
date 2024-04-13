from pygame.sprite import Sprite
from constants import bullet_image, SCREEN_WIDTH, pygame
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.speed = 10
        self.image = bullet_image
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        group.add(self)
        self.group = group
        
    def update(self, player, enemy):
        self.rect.x += self.direction * self.speed
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        if pygame.sprite.spritecollide(player, self.group, False):
            if player.alive:
                player.health -= 5
                self.kill()
        if pygame.sprite.spritecollide(enemy, self.group, False):
            if enemy.alive:
                enemy.health -= 25
                self.kill()
        