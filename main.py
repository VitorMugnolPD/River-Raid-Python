import pygame
import time
import thread
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

pygame.init()
screen = pygame.display.set_mode((600, 380))
x = 280
y = 320
i = x
j = y
done = False
clock = pygame.time.Clock()

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

def enemy(m, n):
    a = int(random.random() * 440)
    j = 0
    enemyLive = True
    while enemyLive == True:
        screen.blit(imageEnemy,(a, j))
        j += 1
        time.sleep(0.01)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    prob = int(random.random() * 100)
    if prob < 1:
        thread.start_new_thread(enemy, (0,0))
    freio = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 2
    if pressed[pygame.K_DOWN]:
        freio = True
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if pressed[pygame.K_SPACE]:
        thread.start_new_thread(shoot, (x, y))
    if freio == True:
        y += 1
    if x < 75:
        x += 3
    if x > 490:
        x -= 3
    if y < 0:
        y += 3
    if y > 320:
        y -= 1
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, 80, 380))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(520, 0, 80, 380))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(80, 0, 440, 380))
    screen.blit(imagePlane,(x, y))
    pygame.display.flip()
    clock.tick(60)