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
player_group=pygame.sprite.Group()
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
            self.kill()
        if self.alive == True:
            self.rect.y -= 9      
        pygame.sprite.groupcollide(enemies, bullets, True, pygame.sprite.collide_circle)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect= image.get_rect(topleft=(random.randrange(80,490),0))
        self.alive = True


    def update(self):
        if self.rect.y > height:
            self.kill()

        if self.alive == True:
            self.rect.y+=1
            
        pygame.sprite.groupcollide(player_group,enemies,True,False)

    

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
        self.rect.x -= 4
     if pressed[pygame.K_RIGHT]:
        self.rect.x += 4
     if pressed[pygame.K_SPACE]:    
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            b = Bullet(imageBullet, self.rect.x, self.rect.y)
            bullets.add(b)
            self.last_shot = pygame.time.get_ticks()
    
 
     if freio == True:
        self.rect.y += 1

     if self.rect.x < 75:
         self.rect.x += 4

     if self.rect.x > 490:
           self.rect.x -= 4

     if self.rect.y < 0:
        self.rect.y += 3

     if self.rect.y> 320:
         self.rect.y -= 1

    
player = Player(imagePlane,imageBullet)
player_group.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background,background_rect)
   
    
    
    prob = int(random.random() * 100)
    if prob < 1:
        enemies.add(Enemy(imageEnemy))


    
    

    bullets.draw(screen)
    bullets.update()
    enemies.draw(screen)
    enemies.update()
    player_group.draw(screen)
    player.update()
   

    pygame.display.update()
    clock.tick(60)