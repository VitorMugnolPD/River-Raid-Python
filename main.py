import pygame
import time
import _thread
import io
import random

imagePlane = pygame.image.load('plane.png')
if imagePlane == None:
    print("Erro ao carregar imagem")

imageBullet = pygame.image.load('bullet2.png')
if imageBullet == None:
    print("Erro ao carregar imagem")

imageEnemy = pygame.image.load('agreeGe.png')
if imageEnemy == None:
    print("Erro ao carregar imagem")

background = pygame.image.load('background.png')
if background == None:
    print("Erro ao carregar imagem")
    
background_rect = background.get_rect()

pygame.init()

height = 380
width = 600
screen = pygame.display.set_mode((width, height))

enemies=[]
done = False

clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect= image.get_rect(topleft=(random.randrange(80,490),0))
        self.alive = True

    def update(self):
        wdwwdw

class Player(pygame.sprite.Sprite):
    def __init__(self,playerImage,shotImage):
        pygame.sprite.Sprite.__init__(self) 
        self.image = playerImage
        self.rect = playerImage.get_rect()
        self.alive = True

        self.rect.centerx = width / 2
        self.rect.bottom = height - 30

    def update(self):
     
     freio = False
     
     pressed = pygame.key.get_pressed()
     if pressed[pygame.K_UP]:
       self.rect.y -= 2
     if pressed[pygame.K_DOWN]:
        freio = True
     if pressed[pygame.K_LEFT]:
        self.rect.x -= 3
     if pressed[pygame.K_RIGHT]:
        self.rect.x += 3
     # if pressed[pygame.K_SPACE]:    
    
 
     if freio == True:
        self.rect.y += 1

     if self.rect.x < 75:
         self.rect.x += 3

     if self.rect.x > 490:
           self.rect.x -= 3

     if self.rect.y < 0:
        self.rect.y += 3

     if self.rect.y> 320:
         self.rect.y -= 1

    



def shoot(m, n):
    i = m
    j = n
    shooting = True
    while shooting == True:
        screen.blit(imageBullet,(i, j))
        j -= 1
        time.sleep(0.0007)
        if j == 0:
            shooting = False



player = Player(imagePlane,imageBullet)
all_active_sprites = pygame.sprite.Group()
all_active_sprites.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background,background_rect)
   
    
    
    
    
    prob = int(random.random() * 12)
    if prob < 1:
         enemies.append(Enemy(imageEnemy))

    
    for enemy in enemies:
        if enemy.image_rect.y > height:
            enemy.alive = False

        if enemy.alive is True:
            enemy.image_rect.y+=3
            screen.blit(enemy.image,enemy.image_rect)
        else:
            enemies.remove(enemy)

    
    
    all_active_sprites.draw(screen)
    all_active_sprites.update()
    pygame.display.update()
    clock.tick(60)