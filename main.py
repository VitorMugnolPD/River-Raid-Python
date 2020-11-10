# Integrantes:
# Vicente Pinto Tomás Junior - RA 19199
# Vitor Mugnol Estevam de Araujo - RA 19200

import pygame
from pygame import mixer

import time
import io
import random

from fuel import Fuel               #
from enemy import Enemy             #
from player import Player           #
from decoration import Decoration   # importando as classes que nós criamos
from explosion import Explosion     #
from title import Title             #

imagePlane = pygame.image.load('plane.png')  # carregando a imagem do avião
if imagePlane == None:
    print("Erro ao carregar imagem")


imageFuel = pygame.image.load('fuel.png')  # carregando a imagem do combustível
if imageFuel == None:
    print("Erro ao carregar imagem")

imageBullet = pygame.image.load('bullet2.png')  # carregando a imagem da bala atirada pelo avião
if imageBullet == None:
    print("Erro ao carregar imagem")

imageEnemy = pygame.image.load('enemy1.png')  # carregando a imagem do inimigo
if imageEnemy == None:
    print("Erro ao carregar imagem")

imageDecoration = pygame.image.load('decoration.png')  # carregando a imagem das casas que aparecem no fundo
if imageDecoration == None:
        print("Erro ao carregar imagem")

background = pygame.image.load('background.png')  # carregando a imagem do fundo
if background == None:
    print("Erro ao carregar imagem")




background_rect = background.get_rect()  # pegando o tamanho da imagem de fundo do jogo

pygame.init()

height = 380  # altura
width = 600  # largura
screen = pygame.display.set_mode((width, height))  # ajeitando a tela do pygame
tela = 0  # 0 = menu, 1 = help, 2 = jogo, 3 = game over -> variável para sabermos a tela em que o jogador está

enemies = pygame.sprite.Group()  # sprites dos inimigos
bullets = pygame.sprite.Group()  # sprites das balas
fuels = pygame.sprite.Group()  # sprites dos combustíveis
player_group = pygame.sprite.Group()  # sprites do jogador (avião)
explosoes = pygame.sprite.Group()  # sprites dos inimigos
decoracoes = pygame.sprite.Group()  # sprites das casas

titles = pygame.sprite.Group()  # sprites do título
titles.add(Title('title.png',24,140,20))  # adicionando as sprites do título

done = False  # variável que usamos para dar continuidade ao while
clock = pygame.time.Clock()

player = Player(imagePlane, imageBullet,height,width,bullets)  # criando o objeto de jogador (avião)
player_group.add(player)  # adicionando a sprite do jogador

font = pygame.font.Font('freesansbold.ttf', 12)  # fonte que utilizamos para escrever na tela

mixer.init()                         #
mixer.music.load("soundtrack.mp3")   # tocar a música de fundo (em loop)
mixer.music.set_volume(0.03)         #
mixer.music.play(loops=-1)           #

while not done:
    for event in pygame.event.get():    #
        if event.type == pygame.QUIT:   # botão de saída da aplicação
            done = True                 #

    if tela == 0:  # se estivermos na tela de menu
        for title in titles:
            title.alive = True
        screen.blit(background, background_rect)  # colocar o fundo na tela


        text2 = font.render('JOGAR - ENTER', True, (255,0,0))  #
        text2Rect = text2.get_rect(center =(280,150))          # escrevendo na tela
        screen.blit(text2, text2Rect)                          #

        text3 = font.render('AJUDA - H', True, (255,0,0))      #
        text3Rect = text3.get_rect(center =(280,180))          # escrevendo na tela
        screen.blit(text3, text3Rect)                          #

        pressed = pygame.key.get_pressed()  # pegar tecla pressionada
        if pressed[pygame.K_KP_ENTER]:  # se for enter (no keypad)
            tela = 2  # tela de jogo
        if pressed[pygame.K_h]:  # se for a letra H
            screen.fill((0,0,0))
            tela = 1  # tela de help
        
        titles.draw(screen)
        titles.update()
        

    if tela == 1:  # se for a tela de help
        for title in titles:
            title.alive = True
        screen.blit(background, background_rect)  # colocar o fundo na tela
           
        text = font.render('ESQUERDA - SETA PARA ESQUERDA', True, (255,0,0))  #
        textRect = text.get_rect(center =(280,80))                            # escrever na tela
        screen.blit(text, textRect)                                           #

        text2 = font.render('DIREITA - SETA PARA DIREITA', True, (255,0,0))   #
        text2Rect = text2.get_rect(center =(280,100))                         # escrever na tela
        screen.blit(text2, text2Rect)                                         #

        text3 = font.render('TURBO - SETA PARA CIMA', True, (255,0,0))        #
        text3Rect = text3.get_rect(center =(280,120))                         # escrever na tela
        screen.blit(text3, text3Rect)                                         #

        text4 = font.render('FREIO - SETA PARA BAIXO', True, (255,0,0))       #
        text4Rect = text4.get_rect(center =(280,140))                         # escrever na tela
        screen.blit(text4, text4Rect)                                         #

        text5 = font.render('ATIRAR - ESPAÇO', True, (255,0,0))               #
        text5Rect = text5.get_rect(center =(280,160))                         # escrever na tela
        screen.blit(text5, text5Rect)                                         #

        text6 = font.render('VOCÊ POSSUI TRÊS VIDAS', True, (255,0,0))        #
        text6Rect = text6.get_rect(center =(280,180))                         # escrever na tela
        screen.blit(text6, text6Rect)                                         #

        text7 = font.render('DESVIE DOS HELICÓPTEROS E NÃO DEIXE A GASOLINA ACABAR!', True, (255,0,0))  #
        text7Rect = text7.get_rect(center =(280,200))                                                   # escrever na tela
        screen.blit(text7, text7Rect)                                                                   #

        text8 = font.render('GANHE PONTOS DESTRUINDO HELICÓPTEROS E GASOLINA!', True, (255,0,0))  #
        text8Rect = text8.get_rect(center =(280,240))                                             # escrever na tela
        screen.blit(text8, text8Rect)                                                             #

        text9 = font.render('VOLTAR PARA O MENU - BACKSPACE', True, (255,0,0))  #
        text9Rect = text9.get_rect(center =(280,220))                           # escrever na tela
        screen.blit(text9, text9Rect)                                           #

        titles.draw(screen)
        titles.update()

        pressed = pygame.key.get_pressed()  # pega a tela pressionada
        if pressed[pygame.K_BACKSPACE]:  # se for backspace
            screen.fill((0,0,0))
            tela = 0  # tela de menu
        

    if tela == 3:  # se for a tela de game over

        text = font.render('VOCÊ PERDEU TODAS AS SUAS VIDAS!!!', True, (255,0,0))  #
        textRect = text.get_rect()                                                 # escrever na tela
        screen.blit(text, textRect)                                                #

        text2 = font.render('APERTE ESPAÇO PARA VOLTAR PARA O MENU', True, (255,0,0))  #
        text2Rect = text2.get_rect()                                                   # escrever na tela
        text2Rect.y = 20                                                               #
        screen.blit(text2, text2Rect)                                                  #

        pressed = pygame.key.get_pressed()  # pega a tela pressionada
        if pressed[pygame.K_SPACE]:  # se for espaço
            screen.fill((0,0,0))
            tela = 0  # tela de menu

    if tela == 2:  # se for a tela de jogo
        screen.blit(background, background_rect)  # colocar o fundo na tela

        bullets = player.get_shots()

        prob = int (random.random()*40)  # número aleatório de zero a 40
        if prob<1:  # se for menor do que 1
            decoracoes.add(Decoration(imageDecoration,height,width))  # adiciona uma sprite de casa

        prob = int(random.random() * 250)  # número aleatório de zero a 250
        if prob < (1 + player.points / 100):  # se for menor do que 1 acrescido de uma parcela dos pontos
            enemies.add(Enemy(imageEnemy,height))  # adiciona uma sprite de inimigo

        prob2 = int(random.random() * (100 + player.points / 20))  # número aleatório de zero a 100 acrescido de uma parcela dos pontos
        if prob2 < 1:  # se for menor do que 1
            fuels.add(Fuel(imageFuel,height))  # adiciona uma sprite de gasolina

        fuels.draw(screen)         #
        fuels.update()             #
        bullets.draw(screen)       #
        bullets.update()           #
        enemies.draw(screen)       # desenha na tela as sprites criadas
        enemies.update()           #
        decoracoes.draw(screen)    #
        decoracoes.update()        #
        player_group.draw(screen)  #
        player.update()            #

        if player.alive == False:  # se o jogador não estiver vivo
            screen.fill((0,0,0))
            tela = 3  # tela de game over
            player = Player(imagePlane, imageBullet,height,width,bullets)  # cria novo jogador (avião)
            player_group.add(player)

        hit = pygame.sprite.groupcollide(player_group, enemies, False, False)  # pega as colisões do jogador com os inimigos
        if hit:  # se houve colisão
            for enemy in enemies:
                enemy.kill()  # apaga inimigos existentes no momento
            if player.lives > 0:  # se o jogador estiver com mais do que zero vidas restantes
                player.lives -= 1  # retirar uma vida do jogador
                player.rect.centerx = width / 2   #
                player.rect.bottom = height - 30  # desenhar jogador novamente na tela
                player.fuel_left = 10000  # voltar quantidade inicial de combustível
            if player.lives == 0:  # se o jogador tiver zero vidas restantes
                player.alive = False  # ele está morto
                player.kill()  # apaga a sprite dele

        fuelhit = pygame.sprite.groupcollide(fuels, bullets, True, pygame.sprite.collide_circle)  # pega as colisões das balas com os combustíveis
        for bullet in fuelhit:
            player.points += 8  # adiciona 8 pontos ao jogador
            explosao = Explosion('explosion.png', 7, bullet.rect.x, bullet.rect.y)  # exibir explosão
            explosoes.add(explosao)                                                 #
            s = pygame.mixer.Sound("explosion.wav")  #
            s.set_volume(0.07)                       # tocar som de explosão
            s.play()                                 #

        hit = pygame.sprite.groupcollide(bullets, enemies,False,True, pygame.sprite.collide_circle)  # pega as colisões das balas com os inimigos
        if hit:  # se houve colisão
            for bullet in hit:
                explosao = Explosion('explosion.png', 7, bullet.rect.x, bullet.rect.y)  # exibir explosão
                explosoes.add(explosao)                                                 #
                s = pygame.mixer.Sound("explosion.wav")  #
                s.set_volume(0.07)                       # tocar som de explosão
                s.play()                                 #
            for player in player_group:
                player.points += 10  # adiciona 10 pontos ao jogador

        explosoes.draw(screen)
        explosoes.update()

        refuel = pygame.sprite.groupcollide(player_group, fuels, False, False)  # pega as colisões do jogador com os combustíveis
        if refuel:  # se houve colisão
            for player in player_group:
                if player.fuel_left <= 9960:
                    player.fuel_left += 40  # adiciona 40 na gasolina restante do jogador
                s = pygame.mixer.Sound("fuel.wav")  #
                s.set_volume(0.03)                  # tocar som da gasolina
                s.play()                            #

        text = font.render('Pontos: ' + str(player.points), True, (0,0,0))  #
        textRect = text.get_rect()                                          # escrever na tela
        screen.blit(text, textRect)                                         #

        fuelPercent = int((player.fuel_left / 10000) * 100)                        #
        text2 = font.render('Gasolina: ' + str(fuelPercent) + '%', True, (0,0,0))  #
        text2Rect = text2.get_rect()                                               # escrever na tela
        text2Rect.y = 20                                                           #
        screen.blit(text2, text2Rect)                                              #

        text3 = font.render('Vidas: ' + str(player.lives), True, (0,0,0))  #
        text3Rect = text3.get_rect()                                       # escrever na tela
        text3Rect.y = 40                                                   #
        screen.blit(text3, text3Rect)                                      #


    pygame.display.update()
    clock.tick(60)