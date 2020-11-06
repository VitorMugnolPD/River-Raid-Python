import pygame
import time
import _thread
import io
import random

BLACK = (0,0,0)


pygame.init()

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


screen = pygame.display.set_mode((600, 380))
done = False
clock = pygame.time.Clock()
enemies=[]


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background,background_rect)
    prob = int(random.random() * 15)
    if prob < 1:
        enemies.append(imageEnemy.get_rect(topleft=(random.randrange(80,490),0)))
    for enemy_rect in enemies:
        enemy_rect.y+=5
        screen.blit(imageEnemy,enemy_rect)

  
    pygame.display.flip()

    clock.tick(20)


