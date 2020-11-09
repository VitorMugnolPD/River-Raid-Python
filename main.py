import pygame
from pygame import mixer

import time
import io
import random

from fuel import Fuel
from enemy import Enemy
from player import Player
from decoration import Decoration
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

imageDecoration = pygame.image.load('decoration.png')
if imageDecoration == None:
        print("Erro ao carregar imagem")

background = pygame.image.load('background.png')
if background == None:
    print("Erro ao carregar imagem")

background_rect = background.get_rect()

pygame.init()

height = 380
width = 600
screen = pygame.display.set_mode((width, height))
tela = 0  # 0 = menu, 1 = help, 2 = jogo, 3 = perdeu

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
fuels = pygame.sprite.Group()
player_group = pygame.sprite.Group()
explosoes = pygame.sprite.Group()
decoracoes = pygame.sprite.Group()

done = False
clock = pygame.time.Clock()

player = Player(imagePlane, imageBullet,height,width,bullets)
player_group.add(player)

font = pygame.font.Font('freesansbold.ttf', 12) 

mixer.init() 
mixer.music.load("soundtrack.mp3") 
mixer.music.set_volume(0.03) 
mixer.music.play() 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if tela == 0:
        text = font.render('RIVER RAID', True, (255,0,0)) 
        textRect = text.get_rect() 
        screen.blit(text, textRect)

        text2 = font.render('JOGAR - ENTER', True, (255,0,0)) 
        text2Rect = text2.get_rect() 
        text2Rect.y = 20
        screen.blit(text2, text2Rect)

        text3 = font.render('AJUDA - H', True, (255,0,0)) 
        text3Rect = text3.get_rect() 
        text3Rect.y = 40
        screen.blit(text3, text3Rect)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_KP_ENTER]:
            tela = 2
        if pressed[pygame.K_h]:
            screen.fill((0,0,0))
            tela = 1

    if tela == 1:
        text = font.render('ESQUERDA - SETA PARA ESQUERDA', True, (255,0,0)) 
        textRect = text.get_rect() 
        screen.blit(text, textRect)

        text2 = font.render('DIREITA - SETA PARA DIREITA', True, (255,0,0)) 
        text2Rect = text2.get_rect() 
        text2Rect.y = 20
        screen.blit(text2, text2Rect)

        text3 = font.render('TURBO - SETA PARA CIMA', True, (255,0,0)) 
        text3Rect = text3.get_rect() 
        text3Rect.y = 40
        screen.blit(text3, text3Rect)

        text4 = font.render('FREIO - SETA PARA BAIXO', True, (255,0,0)) 
        text4Rect = text4.get_rect() 
        text4Rect.y = 60
        screen.blit(text4, text4Rect)

        text5 = font.render('ATIRAR - ESPAÇO', True, (255,0,0)) 
        text5Rect = text5.get_rect() 
        text5Rect.y = 80
        screen.blit(text5, text5Rect)

        text6 = font.render('VOCÊ POSSUI TRÊS VIDAS', True, (255,0,0)) 
        text6Rect = text6.get_rect() 
        text6Rect.y = 100
        screen.blit(text6, text6Rect)

        text7 = font.render('DESVIE DOS HELICÓPTEROS E NÃO DEIXE A GASOLINA ACABAR!', True, (255,0,0)) 
        text7Rect = text7.get_rect() 
        text7Rect.y = 120
        screen.blit(text7, text7Rect)

        text8 = font.render('GANHE PONTOS DESTRUINDO HELICÓPTEROS E GASOLINA!', True, (255,0,0)) 
        text8Rect = text8.get_rect() 
        text8Rect.y = 140
        screen.blit(text8, text8Rect)

        text9 = font.render('VOLTAR PARA O MENU - BACKSPACE', True, (255,0,0)) 
        text9Rect = text9.get_rect() 
        text9Rect.y = 160
        screen.blit(text9, text9Rect)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_BACKSPACE]:
            screen.fill((0,0,0))
            tela = 0

    if tela == 3:
        text = font.render('VOCÊ PERDEU TODAS AS SUAS VIDAS!!!', True, (255,0,0)) 
        textRect = text.get_rect() 
        screen.blit(text, textRect)

        text2 = font.render('APERTE ESPAÇO PARA VOLTAR PARA O MENU', True, (255,0,0)) 
        text2Rect = text2.get_rect() 
        text2Rect.y = 20
        screen.blit(text2, text2Rect)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            screen.fill((0,0,0))
            tela = 0

    if tela == 2:
        screen.blit(background, background_rect)
        bullets = player.get_shots()

        prob = int (random.random()*40)
        if prob<1:
            decoracoes.add(Decoration(imageDecoration,height,width))

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
        decoracoes.draw(screen)
        decoracoes.update()
        player_group.draw(screen)
        player.update()

        if player.alive == False:
            screen.fill((0,0,0))
            tela = 3
            player = Player(imagePlane, imageBullet,height,width,bullets)
            player_group.add(player)

        hit = pygame.sprite.groupcollide(player_group, enemies, False, False)
        if hit:
            for enemy in enemies:
                enemy.kill()
            if player.lives > 0:
                player.lives -= 1
                player.rect.centerx = width / 2
                player.rect.bottom = height - 30
                player.fuel_left = 10000
            if player.lives == 0:
                player.alive = False
                player.kill()

        fuelhit = pygame.sprite.groupcollide(fuels, bullets, True, pygame.sprite.collide_circle)
        for bullet in fuelhit:
            player.points += 8
            explosao = Explosion('explosion.png', 7, bullet.rect.x, bullet.rect.y)
            explosoes.add(explosao)
            s = pygame.mixer.Sound("explosion.wav")
            s.set_volume(0.07)
            s.play()

        hit = pygame.sprite.groupcollide(bullets, enemies,False,True, pygame.sprite.collide_circle)
        if hit:
            for bullet in hit:
                explosao = Explosion('explosion.png', 7, bullet.rect.x, bullet.rect.y)
                explosoes.add(explosao)
                s = pygame.mixer.Sound("explosion.wav")
                s.set_volume(0.07)
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
                s = pygame.mixer.Sound("fuel.wav")
                s.set_volume(0.03)
                s.play()

        text = font.render('Pontos: ' + str(player.points), True, (0,0,0)) 
        textRect = text.get_rect() 
        screen.blit(text, textRect)

        fuelPercent = int((player.fuel_left / 10000) * 100)
        text2 = font.render('Gasolina: ' + str(fuelPercent) + '%', True, (0,0,0))
        text2Rect = text2.get_rect()
        text2Rect.y = 20
        screen.blit(text2, text2Rect)

        text3 = font.render('Vidas: ' + str(player.lives), True, (0,0,0))
        text3Rect = text3.get_rect()
        text3Rect.y = 40
        screen.blit(text3, text3Rect)


    pygame.display.update()
    clock.tick(60)