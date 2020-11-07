import pygame
import random

class Decoration(pygame.sprite.Sprite):
    def __init__(self,image,height,width):
        super().__init__()
        self.image = image
        self.height = height
        if random.random() <= 0.5:
            self.rect = self.image.get_rect(topleft=(random.randrange(1, 50),0))
        else:
            self.rect = self.image.get_rect(topleft=(random.randrange(540, width),0))


    def update(self):
        self.rect.y+=2
        if self.rect.y > self.height:
            self.kill()

        