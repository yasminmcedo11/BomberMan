from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import pygame
import sys

class Menu:
    def __init__(self):
        self.estadoAtual = "menu"
        self.dificuldade = 1

        self.telaMenu = Window(width=600, height=600)
        self.telaMenu.set_background_color([27, 48, 50])
        self.fundo = pygame.image.load("assets/background_menu(1).png").convert()
        self.telaMenu.set_title("BomberMan - Yasmin Macedo")
        self.alturaMenu = self.telaMenu.height
        self.larguraMenu = self.telaMenu.width
        self.teclado = self.telaMenu.get_keyboard()

        self.botaoJogar = Sprite("assets/botaoJogar.png")
        self.botaoModoDeJogo = Sprite("assets/botaoModoDeJogo(1).png")
        #self.botaoRanking = Sprite("assets/texto_ranking.png")
        self.botaoSair = Sprite("assets/botaoSair(1).png")
        self.posicaoX = (self.larguraMenu/2) - self.botaoJogar.width/2
        self.posicaoY = (self.alturaMenu/6)

        self.botaoJogar.set_position(self.posicaoX, self.posicaoY)
        self.botaoModoDeJogo.set_position(self.posicaoX, self.posicaoY + 120)
        self.botaoSair.set_position(self.posicaoX, self.posicaoY + 240)

        self.modoSingle = Sprite("assets/botaoModoHistoria.png")
        self.modoMultiplayer = Sprite("assets/botaoModoMultiplayer.png")

        posicaoX = (self.larguraMenu - self.modoSingle.width) / 2 
        altura_total = self.modoSingle.height + 40 + self.modoMultiplayer.height
        topo = (self.alturaMenu - altura_total) / 3
        self.modoSingle.set_position(posicaoX, topo)
        self.modoMultiplayer.set_position(posicaoX, topo + self.modoSingle.height + 40)

        self.botaoFases = Sprite("assets/botaoFases.png")
        self.botaoMapas = Sprite("assets/botaoMapas.png")

        posicaoXTopo = (self.larguraMenu - self.botaoFases.width) / 2
        self.botaoFases.set_position(posicaoXTopo, 70)
        self.botaoMapas.set_position(posicaoXTopo, 70)

        self.botaoMapa1 = Sprite("assets/botaoMapa1.png")
        self.botaoMapa2 = Sprite("assets/botaoMapa2.png")
        self.botaoMapa3 = Sprite("assets/botaoMapa3.png")
        self.botaoMapa4 = Sprite("assets/botaoMapa4.png")
        self.botaoMapa5 = Sprite("assets/botaoMapa4.png")
        self.botaoMapa6 = Sprite("assets/botaoMapa4.png")

        botoes_mapa = [
            self.botaoMapa1, self.botaoMapa2, self.botaoMapa3,
            self.botaoMapa4, self.botaoMapa5, self.botaoMapa6
        ]
        espaco_horizontal = 40
        espaco_vertical = 40
        botoes_por_linha = 3
        largura_total_botoes = sum(botao.width for botao in botoes_mapa[:3]) + espaco_horizontal * (botoes_por_linha - 1)
        posX_inicial = (self.larguraMenu - largura_total_botoes) / 2
        altura_botoes = botoes_mapa[0].height
        altura_total = altura_botoes * 2 + espaco_vertical
        posY_inicial = (self.alturaMenu - altura_total) / 2
        for i, botao in enumerate(botoes_mapa):
            linha = i // botoes_por_linha
            coluna = i % botoes_por_linha
            x = posX_inicial + coluna * (botao.width + espaco_horizontal)
            y = posY_inicial + linha * (botao.height + espaco_vertical)
            botao.set_position(x, y)



    def clicarJogar(self):
       self.telaMenu.set_background_color([27, 48, 50])

    def clicarSair(self):
        pygame.quit()
        sys.exit()

    def desenharMenu(self):
        self.telaMenu.draw_surface(self.fundo, (0, 0))
        self.botaoJogar.draw()
        self.botaoModoDeJogo.draw()
        self.botaoSair.draw()
    
    def desenharModoDeJogo(self):
        self.telaMenu.draw_surface(self.fundo, (0, 0))
        self.modoSingle.draw()
        self.modoMultiplayer.draw()
        self.atualizarMenu()

    def desenharListaDeMapas(self):
        self.botaoMapa1.draw()
        self.botaoMapa2.draw()
        self.botaoMapa3.draw()
        self.botaoMapa4.draw()
        self.botaoMapa5.draw()
        self.botaoMapa6.draw()
    
    def desenharMapas(self):
        self.telaMenu.draw_surface(self.fundo, (0, 0))
        self.botaoMapas.draw()
        self.desenharListaDeMapas()
        self.atualizarMenu()

    def desenharFases(self):
        self.telaMenu.draw_surface(self.fundo, (0, 0))
        self.botaoFases.draw()
        self.desenharListaDeMapas()
        self.atualizarMenu()

    def atualizarMenu(self):
        self.telaMenu.update()


    def setEstadoAtual(self, estado):
        self.estadoAtual = estado

    def getEstadoAtual(self):
        return self.estadoAtual

    def setDificuldade(self, dificuldade):
        self.dificuldade = dificuldade

    def getDificuldade(self):
        return self.dificuldade