# Integrantes:
# Vicente Pinto Tomás Junior - RA 19199
# Vitor Mugnol Estevam de Araujo - RA 19200

import pygame

from bullet import Bullet
from fuel import Fuel

class Player(pygame.sprite.Sprite):  # classe do jogador (avião)
    def __init__(self, playerImage, bulletImage,height,width,bullets):
        pygame.sprite.Sprite.__init__(self)
        self.height = height  # altura da tela
        self.width = width  # largura da tela
        self.image = playerImage  # imagem do jogador
        self.bulletImage = bulletImage  # imagem da bala
        self.rect = playerImage.get_rect()
        self.alive = True
        self.points = 0  # quantidade de pontos
        self.lives = 3  # número de vidas

        self.bullets =pygame.sprite.Group()  # grupo de sprites das balas
        self.rect.centerx = width / 2   # posicionando o jogador
        self.rect.bottom = height - 30  #

        self.shoot_delay = 250  # delay dos tiros
        self.last_shot = pygame.time.get_ticks()  # horário do último tiro dado

        self.fuel_left = 10000  # quantidade de combustível restante

    def shoot(self):  # atirar
        current_time = pygame.time.get_ticks()  # pega o horário atual, para ser o horário do último tiro
        if current_time - self.last_shot > self.shoot_delay:  # se o horario atual menos o do último tiro for maior do que o delay do tiro
            b = Bullet(self.bulletImage, self.rect.x, self.rect.y,self.height)  # objeto de bala
            self.bullets.add(b)
            self.last_shot = pygame.time.get_ticks()  # atualiza a hora do último tiro dado
            
            
    def get_shots(self):
        return self.bullets  # retorna o grupo de tiros

    def update(self):

        freio = False

        pressed = pygame.key.get_pressed()  # pega a tela pressionada
        if pressed[pygame.K_UP]:  # se for a seta pra cima
            self.rect.y -= 2  # decrementa a altura por 2
        if pressed[pygame.K_DOWN]:  # se for a seta para baixo
            freio = True  # o jogador está "freando"
        if pressed[pygame.K_LEFT]:  # se for a seta para a esquerda
            self.rect.x -= 4  # decrementa o comprimento por 4
        if pressed[pygame.K_RIGHT]:  # se for a seta para a direita
            self.rect.x += 4  # incrementa a altura por 4
        if pressed[pygame.K_SPACE]:  # se for espaço
            if self.alive:    # se ele estiver vivo, ele atira
                self.shoot()  #

        if freio == True:  # se estiver freando
            self.rect.y += 1  # incrementa a altura por 1

        if self.rect.x < 75:   # estabelecendo os limites para o jogador se locomover no mapa
            self.rect.x += 4   #

        if self.rect.x > 490:  # estabelecendo os limites para o jogador se locomover no mapa
            self.rect.x -= 4   #

        if self.rect.y < 0:    # estabelecendo os limites para o jogador se locomover no mapa
            self.rect.y += 3   #

        if self.rect.y > 320:  # estabelecendo os limites para o jogador se locomover no mapa
            self.rect.y -= 1   #

        if self.fuel_left >= 0 and self.alive:
            self.fuel_left -= 10  # decrementa a quantidade de combustível sobrando por 10

        if self.fuel_left <= 0:  # se não houver combustível sobrando
            if self.lives > 0:  # se houver mais do que zero vidas restantes
                self.lives -= 1  # diminui o número de vidas
                self.rect.centerx = self.width / 2   # posicionando o jogador
                self.rect.bottom = self.height - 30  #
                self.fuel_left = 10000  # colocando no máximo novamente a quantidade de combustível restante
            if self.lives == 0:  # se estiver com zero vidas
                self.alive = False  # "matar" o jogador
                self.kill()         #
