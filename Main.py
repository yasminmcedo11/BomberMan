from Menu import Menu
from Janela import Janela
from PPlay.mouse import *
import time
import pygame

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
rodando = True
menu = Menu()
mouse = Mouse()
botao_mouse_antes = False
jogo_congelado = False

pygame.mixer.music.load("sounds/main.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


while True:
    botao_mouse_agora = mouse.is_button_pressed(1)
    clicou_agora = botao_mouse_agora and not botao_mouse_antes

    if menu.getEstadoAtual() == "menu":
        menu.desenharMenu()

        if mouse.is_over_object(menu.botaoJogar) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa1.txt", 1, True)
        if mouse.is_over_object(menu.botaoModoDeJogo) and clicou_agora:
            menu.setEstadoAtual("modoDeJogo")
        if mouse.is_over_object(menu.botaoSair) and clicou_agora:
            menu.clicarSair()

    elif menu.getEstadoAtual() == "modoDeJogo":
        menu.desenharModoDeJogo()

        if menu.teclado.key_pressed("ESC"):
            menu.setEstadoAtual("menu")

        if mouse.is_over_object(menu.modoSingle) and clicou_agora:
            menu.setEstadoAtual("fases")
        if mouse.is_over_object(menu.modoMultiplayer) and clicou_agora:
            menu.setEstadoAtual("mapas")
   
    elif menu.getEstadoAtual() == "fases":
        menu.desenharFases()

        if menu.teclado.key_pressed("ESC"):
            menu.setEstadoAtual("menu")
        if mouse.is_over_object(menu.botaoMapa1) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa1.txt", 1, True)
        if mouse.is_over_object(menu.botaoMapa2) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa2.txt", 2, True)
        if mouse.is_over_object(menu.botaoMapa3) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa3.txt", 3, True)
        if mouse.is_over_object(menu.botaoMapa4) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa4.txt", 4, True)
        if mouse.is_over_object(menu.botaoMapa5) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa5.txt", 5, True)
        if mouse.is_over_object(menu.botaoMapa6) and clicou_agora:
            menu.setEstadoAtual("jogoSingle")
            janela = Janela("mapas/mapa6.txt", 6, True)
    
    elif menu.getEstadoAtual() == "mapas":
        menu.desenharMapas()

        if menu.teclado.key_pressed("ESC"):
            menu.setEstadoAtual("menu")
        if mouse.is_over_object(menu.botaoMapa1) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa1.txt", 1, False)
        if mouse.is_over_object(menu.botaoMapa2) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa2.txt", 2, False)
        if mouse.is_over_object(menu.botaoMapa3) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa3.txt", 3, False)
        if mouse.is_over_object(menu.botaoMapa4) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa4.txt", 4, False)
        if mouse.is_over_object(menu.botaoMapa5) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa5.txt", 5, False)
        if mouse.is_over_object(menu.botaoMapa6) and clicou_agora:
            menu.setEstadoAtual("jogoMultiplayer")
            janela = Janela("mapas/mapa6.txt", 6, False)


    elif menu.getEstadoAtual() == "jogoSingle":
        menu.clicarJogar()
        delta_time = clock.tick(60) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    janela.pausarJogo(janela.tela, janela.largura, janela.altura)

        teclas = pygame.key.get_pressed()
        if not jogo_congelado:
            if teclas[pygame.K_SPACE]:
                janela.player.plantar_bomba()
            if not janela.player.esta_se_movendo():
                if teclas[pygame.K_UP]:
                    janela.player.mover("cima", janela.getMapa())
                elif teclas[pygame.K_DOWN]:
                    janela.player.mover("baixo", janela.getMapa())
                elif teclas[pygame.K_LEFT]:
                    janela.player.mover("esquerda", janela.getMapa())
                elif teclas[pygame.K_RIGHT]:
                    janela.player.mover("direita", janela.getMapa())


            # Desenhar mapa
            janela.desenharMapa()
            janela.desenharPlayer()
            janela.desenharMonstro()
            janela.atualizarJanela(delta_time)


        if janela.verificarDerrota():
            jogo_congelado = True
            janela.mostrarMensagem(janela.tela, janela.largura, janela.altura)
            pygame.display.update()
            if teclas[pygame.K_RETURN]:
                jogo_congelado = False
                janela.reiniciarFase()
                time.sleep(1)
        
        if janela.verificarVitoria():
            jogo_congelado = True
            janela.mostrarMensagem(janela.tela, janela.largura, janela.altura)
            pygame.display.update()
            if teclas[pygame.K_RETURN]:
                jogo_congelado = False
                janela.proximaFase()
                time.sleep(1)

        if menu.teclado.key_pressed("ESC"):
            jogo_congelado = False
            janela.reiniciarJogo()
            menu.setEstadoAtual("menu")
    

    elif menu.getEstadoAtual() == "jogoMultiplayer":
        menu.clicarJogar()
        delta_time = clock.tick(60) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    janela.pausarJogo(janela.tela, janela.largura, janela.altura)

        teclas = pygame.key.get_pressed()
        if not jogo_congelado:
            if teclas[pygame.K_p]:
                janela.player2.plantar_bomba()
            if not janela.player.esta_se_movendo():
                if teclas[pygame.K_w]:
                    janela.player2.mover("cima", janela.getMapa())
                elif teclas[pygame.K_s]:
                    janela.player2.mover("baixo", janela.getMapa())
                elif teclas[pygame.K_a]:
                    janela.player2.mover("esquerda", janela.getMapa())
                elif teclas[pygame.K_d]:
                    janela.player2.mover("direita", janela.getMapa())
            
            if teclas[pygame.K_SPACE]:
                janela.player.plantar_bomba()
            if not janela.player.esta_se_movendo():
                if teclas[pygame.K_UP]:
                    janela.player.mover("cima", janela.getMapa())
                elif teclas[pygame.K_DOWN]:
                    janela.player.mover("baixo", janela.getMapa())
                elif teclas[pygame.K_LEFT]:
                    janela.player.mover("esquerda", janela.getMapa())
                elif teclas[pygame.K_RIGHT]:
                    janela.player.mover("direita", janela.getMapa())


            # Desenhar mapa
            janela.desenharMapa()
            janela.desenharPlayer()
            janela.atualizarJanela(delta_time)


        if janela.verificarDerrota():
            jogo_congelado = True
            janela.mostrarMensagem(janela.tela, janela.largura, janela.altura)
            pygame.display.update()
            if teclas[pygame.K_RETURN]:
                jogo_congelado = False
                janela.reiniciarJogo()
                time.sleep(1)
                menu.setEstadoAtual("menu")
        
        if janela.verificarDerrotaPlayer2():
            jogo_congelado = True
            janela.mostrarMensagem(janela.tela, janela.largura, janela.altura)
            pygame.display.update()
            if teclas[pygame.K_RETURN]:
                jogo_congelado = False
                janela.reiniciarJogo()
                time.sleep(1)
                menu.setEstadoAtual("menu")

        if menu.teclado.key_pressed("ESC"):
            jogo_congelado = False
            janela.reiniciarJogo()
            menu.setEstadoAtual("menu")

    botao_mouse_antes = botao_mouse_agora
    menu.atualizarMenu()
