from Menu import Menu
from Janela import Janela
from PPlay.mouse import *
import pygame
import os

pygame.init()
clock = pygame.time.Clock()
rodando = True
menu = Menu()
mouse = Mouse()
janela = Janela("mapas/mapa1.txt")


while True:
    if menu.getEstadoAtual() == "menu":
        menu.desenharMenu()

        if mouse.is_over_object(menu.botaoJogar) and mouse.is_button_pressed(1):
            menu.setEstadoAtual("jogo")
        if mouse.is_over_object(menu.botaoDificuldade) and mouse.is_button_pressed(1):
            menu.setEstadoAtual("dificuldade")
        if mouse.is_over_object(menu.botaoSair) and mouse.is_button_pressed(1):
            menu.clicarSair()

    #elif menu.getEstadoAtual() == "dificuldade":
      #  menu.desenharDificuldade()

      #  if mouse.is_over_object(menu.dif1) and mouse.is_button_pressed(1):
     #       menu.setDificuldade(1)
     #       menu.setEstadoAtual("jogo")
     #   if mouse.is_over_object(menu.dif2) and mouse.is_button_pressed(1):
      #      menu.setDificuldade(2)
    #        menu.setEstadoAtual("jogo")
     #   if mouse.is_over_object(menu.dif3) and mouse.is_button_pressed(1):
       #     menu.setDificuldade(3)
       #     menu.setEstadoAtual("jogo")
    
   # elif menu.getEstadoAtual() == "fases":
    #    menu.desenharFases()


    elif menu.getEstadoAtual() == "jogo":
        menu.clicarJogar()
        delta_time = clock.tick(60) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            janela.player.plantar_bomba()
        if not janela.player.esta_se_movendo():
            if teclas[pygame.K_w] or teclas[pygame.K_UP]:
                janela.player.mover("cima", janela.getMapa())
            elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
                janela.player.mover("baixo", janela.getMapa())
            elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
                janela.player.mover("esquerda", janela.getMapa())
            elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
                janela.player.mover("direita", janela.getMapa())


        # Desenhar mapa
        janela.desenharMapa()
        janela.desenharPlayer()
        janela.desenharMonstro()
        janela.atualizarJanela(delta_time)

        if janela.verificarDerrota():
            janela.reiniciarJogo()
            menu.setEstadoAtual("menu")
        
        if janela.verificarVitoria():
            janela.reiniciarJogo()
            menu.setEstadoAtual("menu")
        

        if menu.teclado.key_pressed("ESC"):
            janela.reiniciarJogo()
            menu.setEstadoAtual("menu")


    menu.atualizarMenu()
