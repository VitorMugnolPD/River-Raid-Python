# Integrantes:
# Vicente Pinto Tomás Junior - RA 19199
# Vitor Mugnol Estevam de Araujo - RA 19200

import pygame

class Bullet(pygame.sprite.Sprite):  # classe da bala
    def __init__(self, image, playerX, playerY,height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height  # altura da tela
        self.image = image  # imagem da bala
        self.rect = image.get_rect(top=playerY, left=playerX)  # posição
        self.alive = True

    def update(self):
        if self.rect.y > self.height:  #
            self.alive= False          # se estiver acima do limite da tela, ela "morre"
            self.kill()                #
            
        if self.alive == True:  # enquanto estiver "viva", sua altura se decrementa por 9
            self.rect.y -= 9    #