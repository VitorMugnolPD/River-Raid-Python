import pygame

from bullet import Bullet
from fuel import Fuel

class Player(pygame.sprite.Sprite):
    def __init__(self, playerImage, bulletImage,height,width,bullets):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.width = width
        self.image = playerImage
        self.bulletImage = bulletImage
        self.rect = playerImage.get_rect()
        self.alive = True
        self.points = 0

        self.bullets =pygame.sprite.Group()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 30

        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

        self.fuel_left = 10000

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            b = Bullet(self.bulletImage, self.rect.x, self.rect.y,self.height)
            self.bullets.add(b)
            self.last_shot = pygame.time.get_ticks()
            
            
    def get_shots(self):
        return self.bullets

    def update(self):

        freio = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.y -= 2
        if pressed[pygame.K_DOWN]:
            freio = True
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 4
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 4
        if pressed[pygame.K_SPACE]:
            self.shoot()

        if freio == True:
            self.rect.y += 1

        if self.rect.x < 75:
            self.rect.x += 4

        if self.rect.x > 490:
            self.rect.x -= 4

        if self.rect.y < 0:
            self.rect.y += 3

        if self.rect.y > 320:
            self.rect.y -= 1

        self.fuel_left -= 10
        #if self.alive:
           #print(self.fuel_left)

        if self.fuel_left <= 0:
           #print("perdeste")
           #print(self.points)
            self.alive = False
