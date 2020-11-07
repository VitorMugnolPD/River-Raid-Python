import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image,height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.image = image
        self.rect = image.get_rect(topleft=(random.randrange(80, 490), 0))
        self.alive = True

    def update(self):
        if self.rect.y > self.height:
            self.kill()

        if self.alive == True:
            self.rect.y += 2