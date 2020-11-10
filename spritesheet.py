import pygame

class Spritesheet:  # classe para utilizar as sprites
    def __init__(self,filename):
        self.filename = filename  # arquivo
        self.sprite_sheet = pygame.image.load(self.filename).convert()  # convertem o arquivo passado


    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0)) 
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite 