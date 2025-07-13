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
        

        if menu.teclado.key_pressed("ESC"):
            menu.setEstadoAtual("menu")


    menu.atualizarMenu()
