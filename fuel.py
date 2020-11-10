# Integrantes:
# Vicente Pinto Tomás Junior - RA 19199
# Vitor Mugnol Estevam de Araujo - RA 19200

import pygame
import random

class Fuel(pygame.sprite.Sprite):  # classe do combustível
    def __init__(self, image,height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height  # altura da tela
        self.image = image  # imagem do combustível
        self.rect = image.get_rect(topleft=(random.randrange(80, 490), 0))  # posição aleatória, dentro dos limites
        self.alive = True

    def update(self):
        if self.rect.y > self.height:  # se a altura estiver acima dos limites da tela, ela "morre"
            self.kill()                #

        if self.alive == True:  # enquanto estiver "viva", sua altura se incrementa por 2
            self.rect.y += 2    #
