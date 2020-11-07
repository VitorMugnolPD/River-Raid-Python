import pygame
import time
import _thread
import io
import random
from spritesheet import Spritesheet
BLACK = (0,0,0)


pygame.init()



explosion = pygame.image.load('explosion.png')

background = pygame.image.load('background.png')
if background == None:
    print("Erro ao carregar imagem")

background_rect = background.get_rect()

  

screen = pygame.display.set_mode((600, 380))
done = False
clock = pygame.time.Clock()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,filename,numberFrames):
        super().__init__()
        self.filename = filename
        self.spritesheet = Spritesheet(filename)
        self.numberFrames = numberFrames
        self.sprites = []
        for i in range(0,numberFrames):
            self.sprites.append(self.spritesheet.get_sprite(0+i*32,0,32,32))

        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

        self.rect =self.image.get_rect()


    def update(self):
        self.current_sprite +=1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

explosoes = pygame.sprite.Group()
explosao = Explosion('explosion.png',7)
explosoes.add(explosao)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.blit(background, background_rect)
    explosoes.draw(screen)
    explosoes.update()
    pygame.display.update()
    clock.tick(20)


