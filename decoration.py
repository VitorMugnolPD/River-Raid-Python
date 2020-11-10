import pygame
import random

class Decoration(pygame.sprite.Sprite):  # classe das casas vistas no fundo
    def __init__(self,image,height,width):
        super().__init__()
        self.image = image  # imagem das casas
        self.height = height  # altura da tela
        if random.random() <= 0.5:  # se um número aleatório for menor do que 0.5
            self.rect = self.image.get_rect(topleft=(random.randrange(1, 50),0))  # desenha em algumo ponto do lado esquerdo
        else:  # se não for menor do que 0.5
            self.rect = self.image.get_rect(topleft=(random.randrange(540, width),0))  # desenha em algum ponto do lado direito


    def update(self):
        self.rect.y+=2  # altura se incrementa por 2
        if self.rect.y > self.height:  # se a altura for menor do que o limite da tela, ela "morre"
            self.kill()                #

        