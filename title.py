from spritesheet import Spritesheet
import pygame


class Title(pygame.sprite.Sprite):
    def __init__(self,filename,numberFrames,X,Y):
        super().__init__()
        self.filename = filename
        self.spritesheet = Spritesheet(filename)
        self.numberFrames = numberFrames
        self.sprites = []
        for i in range(0,numberFrames):
            self.sprites.append(self.spritesheet.get_sprite(0+i*312,0,312,38))

        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]

        self.rect =self.image.get_rect(top=Y, left=X)

    def update(self):
        if self.alive == True:
            self.current_sprite +=1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]   


    def die(self):
        self.alive = False