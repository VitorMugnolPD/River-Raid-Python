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

enemies=pygame.sprite.Group()
bullets=pygame.sprite.Group()
done = False

clock = pygame.time.Clock()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image, playerX, playerY):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect(top = playerY, left = playerX)
        self.alive = True

    def update(self):
        if self.rect.y > height:
            self.alive = False
        if self.alive == True:
            self.rect.y -= 9

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect= image.get_rect(topleft=(random.randrange(80,490),0))
        self.alive = True

    def update(self):
        if self.rect.y > height:
            self.alive = False

        if self.alive is True:
            self.rect.y+=1
            #screen.blit(enemy.image,enemy.rect)

    #def update(self):
        #wdwwdw

class Player(pygame.sprite.Sprite):
    def __init__(self,playerImage,shotImage):
        pygame.sprite.Sprite.__init__(self) 
        self.image = playerImage
        self.rect = playerImage.get_rect()
        self.alive = True

        self.rect.centerx = width / 2
        self.rect.bottom = height - 30

        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

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
     if pressed[pygame.K_SPACE]:    
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            #self.alive = False
            b = Bullet(imageBullet, self.rect.x, self.rect.y)
            all_active_sprites.add(b)
            bullets.add(b)
            self.last_shot = pygame.time.get_ticks()
    
 
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
   
    
    
    
    
    prob = int(random.random() * 1)
    if prob < 1:
        all_active_sprites.add(Enemy(imageEnemy))
        enemies.add(Enemy(imageEnemy))

    
    for enemy in enemies:
        if enemy.alive == False:
            enemies.remove(enemy)

    
    
    all_active_sprites.draw(screen)
    all_active_sprites.update()
    pygame.display.update()
    clock.tick(60)