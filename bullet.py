import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, playerX, playerY,height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.image = image
        self.rect = image.get_rect(top=playerY, left=playerX)
        self.alive = True

    def update(self):
        if self.rect.y > self.height:
            self.alive= False
            self.kill()
            
        if self.alive == True:
            self.rect.y -= 9