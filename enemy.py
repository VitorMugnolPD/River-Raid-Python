import pygame
import random


class Enemy(pygame.sprite.Sprite):  # classe do inimigo
    def __init__(self, image,height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height  # altura da tela
        self.image = image  # imagem do inimigo
        self.rect = image.get_rect(topleft=(random.randrange(80, 490), 0))  # posição aleatória, dentro dos limites
        self.alive = True

    def update(self):
        if self.rect.y > self.height:  # se a altura passar dos limites da tela, ela "morre"
            self.kill()                #

        if self.alive == True:  # enquanto estiver "vivo", sua altua se incrementa por 2
            self.rect.y += 2    #