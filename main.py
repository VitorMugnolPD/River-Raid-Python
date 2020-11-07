import pygame
from pygame import mixer

import time
import io
import random

from fuel import Fuel
from enemy import Enemy
from player import Player
from explosion import Explosion


imagePlane = pygame.image.load('plane.png')
if imagePlane == None:
    print("Erro ao carregar imagem")

imageFuel = pygame.image.load('fuel.png')
if imageFuel == None:
    print("Erro ao carregar imagem")

imageBullet = pygame.image.load('bullet2.png')
if imageBullet == None:
    print("Erro ao carregar imagem")

imageEnemy = pygame.image.load('enemy1.png')
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

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
fuels = pygame.sprite.Group()
player_group = pygame.sprite.Group()
explosoes = pygame.sprite.Group()

done = False
clock = pygame.time.Clock()

player = Player(imagePlane, imageBullet,height,width,bullets)
player_group.add(player)

mixer.init() 
mixer.music.load("soundtrack.mp3") 
mixer.music.set_volume(0.03) 
mixer.music.play() 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, background_rect)
    bullets = player.get_shots()
    prob = int(random.random() * 250)
    if prob < (1 + player.points / 100):
        enemies.add(Enemy(imageEnemy,height))

    prob2 = int(random.random() * (100 + player.points / 20))
    if prob2 < 1:
        fuels.add(Fuel(imageFuel,height))

    fuels.draw(screen)
    fuels.update()
    bullets.draw(screen)
    bullets.update()
    enemies.draw(screen)
    enemies.update()
    player_group.draw(screen)
    player.update()

    hit = pygame.sprite.groupcollide(player_group, enemies, True, False)
    if hit:
        player.alive = False
        #print("perdeste")
        #print(player.points)

    pygame.sprite.groupcollide(fuels, bullets, True, pygame.sprite.collide_circle)

    hit = pygame.sprite.groupcollide(bullets, enemies,False,True, pygame.sprite.collide_circle)
    if hit:
        for bullet in hit:
            explosao = Explosion('explosion.png', 7, bullet.rect.x, bullet.rect.y)
            explosoes.add(explosao)
            print(explosoes)
            #mixer.init() 
            #mixer.music.load("explosion.mp3") 
            #mixer.music.set_volume(0.03) 
            #mixer.music.play() 
            #pygame.mixer.Sound.play("explosion.wav")
            s = pygame.mixer.Sound("explosion.wav")
            s.set_volume(0.05)
            s.play()
        for player in player_group:
            player.points += 10

    explosoes.draw(screen)
    explosoes.update()

    refuel = pygame.sprite.groupcollide(player_group, fuels, False, False)
    if refuel:
        for player in player_group:
            if player.fuel_left <= 9960:
                player.fuel_left += 40
            #mixer.music.load("fuel.mp3") 
            #mixer.music.set_volume(0.03) 
            #mixer.music.play() 
            #pygame.mixer.Sound.play("fuel.wav")
            s = pygame.mixer.Sound("fuel.wav")
            s.set_volume(0.05)
            s.play()


    pygame.display.update()
    clock.tick(60)