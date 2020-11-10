from spritesheet import Spritesheet
import pygame


class Title(pygame.sprite.Sprite):  # classe do título
    def __init__(self,filename,numberFrames,X,Y):
        super().__init__()
        self.filename = filename  # arquivo
        self.spritesheet = Spritesheet(filename)  # sprites do arquivo
        self.numberFrames = numberFrames  # quantidade de frames
        self.sprites = []  # vetor das sprites
        for i in range(0,numberFrames):                                         # adicionando todas as sprites
            self.sprites.append(self.spritesheet.get_sprite(0+i*312,0,312,38))  #

        self.current_sprite =0  # sprite atual
        self.image = self.sprites[self.current_sprite]  # imagem atual

        self.rect =self.image.get_rect(top=Y, left=X)  # posição da sprite

    def update(self):
        if self.alive == True:
            self.current_sprite +=1  # muda a sprite, indo para a seguinte
            if self.current_sprite >= len(self.sprites):  # se passar por todas as sprites, volta para a inicial 
                self.current_sprite = 0                   #

            self.image = self.sprites[self.current_sprite]  # atualiza a imagem atual  


    def die(self):
        self.alive = False