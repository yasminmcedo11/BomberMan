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
        self.botaoDificuldade = Sprite("assets/botaoConfig (1).png")
        #self.botaoRanking = Sprite("assets/texto_ranking.png")
        self.botaoSair = Sprite("assets/botaoSair(1).png")
        self.posicaoX = (self.larguraMenu/2) - self.botaoJogar.width/2
        self.posicaoY = (self.alturaMenu/6)

        self.botaoJogar.set_position(self.posicaoX, self.posicaoY)
        self.botaoDificuldade.set_position(self.posicaoX, self.posicaoY + 120)
        #self.botaoRanking.set_position(self.posicaoX, self.posicaoY + 200)
        self.botaoSair.set_position(self.posicaoX, self.posicaoY + 240)

        self.dif1 = Sprite("assets/texto_facil.png")
        self.dif2 = Sprite("assets/texto_medio.png")
        self.dif3 = Sprite("assets/texto_dificil.png")

        self.dif1.set_position(self.posicaoX, self.posicaoY + 50)
        self.dif2.set_position(self.posicaoX, self.posicaoY + 150)
        self.dif3.set_position(self.posicaoX, self.posicaoY + 250)



    def clicarJogar(self):
       self.telaMenu.set_background_color([27, 48, 50])

    def clicarSair(self):
        pygame.quit()
        sys.exit()

    def desenharDificuldade(self):
        self.telaMenu.set_background_color([27, 48, 50])
        self.dif1.draw()
        self.dif2.draw()
        self.dif3.draw()
        self.atualizarMenu()

    def desenharMenu(self):
        self.telaMenu.draw_surface(self.fundo, (0, 0))
        self.botaoJogar.draw()
        self.botaoDificuldade.draw()
        #self.botaoRanking.draw()
        self.botaoSair.draw()

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