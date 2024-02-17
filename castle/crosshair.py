import pygame
class Crosshair:
    def __init__(self, scale):
        img = pygame.image.load("img/crosshair.png")
        w = img.get_width()
        h = img.get_height()
        self.image = pygame.transform.scale(img, (w * scale, h * scale))
        self.rect = self.image.get_rect()
        
        pygame.mouse.set_visible(False)
        
    def draw(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)
        screen.blit(self.image, self.rect)