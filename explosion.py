from spritesheet import Spritesheet
import pygame

class Explosion(pygame.sprite.Sprite):  # classe da explosão
    def __init__(self,filename,numberFrames,X,Y):
        super().__init__()
        self.filename = filename  # arquivo
        self.spritesheet = Spritesheet(filename)
        self.numberFrames = numberFrames  # número de frames
        self.sprites = []  # vetor das sprites
        for i in range(0,numberFrames):                                       # adicionando todas as sprites
            self.sprites.append(self.spritesheet.get_sprite(0+i*32,0,32,32))  #

        self.current_sprite =0  # sprite atual
        self.image = self.sprites[self.current_sprite]  # carrega a sprite atual, no caso a primeira

        self.rect =self.image.get_rect(top=Y, left=X)  # posição da explosão


    def update(self):
        self.current_sprite +=1  # muda a sprite atual, indo para a próxima
        if self.current_sprite >= len(self.sprites):  #
            self.current_sprite = 0                   # se passar por todas as sprites, ela "morre"
            self.kill()                               #

        self.image = self.sprites[self.current_sprite]  # muda a imagem para a sprite atual