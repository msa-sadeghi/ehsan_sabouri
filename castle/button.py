import pygame
class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect(center = (x,y))
        self.clicked = False
        self.last_clicked_time = pygame.time.get_ticks()


    def draw(self, screen):
        action = False
        screen.blit(self.image, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
                self.last_clicked_time = pygame.time.get_ticks()
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action
