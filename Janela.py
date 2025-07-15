from PPlay.sprite import *
from Player import Player
from Monstros import Monstro
import pygame
import os
import uuid
import random

class Janela:
    def __init__(self, mapa_arquivo, fase, singlePlayer,tile_size=46):
        self.tileSize = tile_size
        self.nome_arquivo = mapa_arquivo
        self.fase = fase
        self.numeroMonstros = 2 + self.fase 
        self.singlePlayer = singlePlayer
        
        self.mapa = self.carregarMapa(self.nome_arquivo)
        
        self.num_colunas = len(self.mapa[0])
        self.num_linhas = len(self.mapa)
        self.largura = self.num_colunas * self.tileSize
        self.altura = self.num_linhas * self.tileSize
        
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("BomberMan")
        
        self.tiles = {
            "W": self.carregarImagem("blocosFixos.png"),
            "X": self.carregarImagem("blocosFixos2.png"),
            "Y": self.carregarImagem("blocosFixos3.png"),
            "Z": self.carregarImagem("blocosFixos4.png"),
            "G": self.carregarImagem("grama.png"),  #sombra esq e superior
            "H": self.carregarImagem("grama2.png"), #sombra superior
            "I": self.carregarImagem("grama3.png"), #sem sombra 
            "J": self.carregarImagem("grama4.png"), #sombra esq
            "B": self.carregarImagem("blocosDestrutivos.png")
        }

        self.player = Player(self, 1)

        if(self.singlePlayer):
            self.monstros = self.criarMonstros()
        else: 
            self.player2 = Player(self, 2)
        
                

    def carregarMapa(self, arquivo):
        with open(arquivo, "r") as f:
            linhas = f.readlines()
        
        self.mapaOriginal = [list(linha.strip()) for linha in linhas]

        return [linha.copy() for linha in self.mapaOriginal]
    
    def carregarImagem(self, nome):
        imagem = pygame.image.load(os.path.join("assets", nome)).convert_alpha()
        return pygame.transform.scale(imagem, (self.tileSize, self.tileSize))

    def carregar_sprite_escalado(self, caminho, largura_frame, altura_frame, frames):
        imagemOriginal = pygame.image.load(caminho)
        larguraTotal = largura_frame * frames
        imagemEscalada = pygame.transform.scale(imagemOriginal, (larguraTotal, altura_frame))

        temp_path = f"assets/temp_scaled_{uuid.uuid4().hex}.png"
        pygame.image.save(imagemEscalada, temp_path)

        sprite = Sprite(temp_path, frames=frames)
        os.remove(temp_path)
        return sprite
    
    def encontrarPosicoesValidas(self, excluidos=set()):
        posicoes = []
        for i, linha in enumerate(self.mapa):
            for j, tile in enumerate(linha):
                if tile in "GHIJ" and (i, j) not in excluidos:
                    posicoes.append((i, j))
        return posicoes
    
    def criarMonstros(self):
        posicoes_validas = self.encontrarPosicoesValidas(excluidos={(1, 1)})
        posicoes_monstros = random.sample(posicoes_validas, self.numeroMonstros)
        return [Monstro(self, l, c) for l, c in posicoes_monstros]

    def desenharMapa(self):
        self.tela.fill((0, 0, 0))  

        for y, linha in enumerate(self.mapa):
            for x, tile in enumerate(linha):
                self.tela.blit(self.tiles[tile], (x * self.tileSize, y * self.tileSize))

    def desenharPlayer(self):
        self.player.draw()
        if(self.singlePlayer == False):
            self.player2.draw()
    
    def desenharMonstro(self):
        for monstro in self.monstros:
            monstro.draw()

    def atualizarJanela(self, delta_time):
        self.player.update(delta_time)
        self.player.verificarColisaoBombas(self.player.getBombas())

        if (self.singlePlayer):
            for monstro in self.monstros:
                monstro.update(delta_time, self.mapa)
            for monstro in self.monstros:
                monstro.verificarColisaoBombas(self.player.getBombas())
            self.player.verificarColisaoPlayerMonstros(self.monstros)
            self.monstros = [m for m in self.monstros if m.getEstaVivo()]
        else:
            self.player2.update(delta_time)
            self.player2.verificarColisaoBombas(self.player2.getBombas())
            self.player2.verificarColisaoBombas(self.player.getBombas())
            self.player.verificarColisaoBombas(self.player2.getBombas())

        pygame.display.flip()
    
    def verificarVitoria(self):
        if len(self.monstros) == 0:
            return True
        else:
            return False
    
    def verificarDerrota(self):
        return not self.player.getEstaVivo()

    def verificarDerrotaPlayer2(self):
        return not self.player2.getEstaVivo()

    def reiniciarJogo(self):
        self.mapa = [linha.copy() for linha in self.mapaOriginal]    
        self.player = Player(self, 1)
        self.monstros = self.criarMonstros()
    
    def reiniciarFase(self):
        self.mapa = [linha.copy() for linha in self.mapaOriginal]    
        self.player = Player(self, 1)
        self.monstros = self.criarMonstros()
    
    def proximaFase(self):
        self.fase += 1
        try:
            novo_mapa = f"mapas/mapa{self.fase}.txt"
            self.mapaOriginal = self.carregarMapa(novo_mapa)  
            self.mapa = [linha.copy() for linha in self.mapaOriginal]
            self.player = Player(self, 1)
            self.numeroMonstros += self.fase//2
            self.monstros = self.criarMonstros()
        except FileNotFoundError:
            self.fase = 1
            self.numeroMonstros = 3 + self.fase //2
            self.mapaOriginal = self.carregarMapa(f"mapas/mapa1.txt")
            self.mapa = [linha.copy() for linha in self.mapaOriginal]
            self.player = Player(self, 1)
            self.monstros = self.criarMonstros()
            return False  
        return True
    
    def pausarJogo(self, tela, largura, altura):
        fonte_titulo = pygame.font.SysFont("Arial", 60, bold=True)
        fonte_subtitulo = pygame.font.SysFont("Arial", 30)

        pausando = True
        while pausando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key in [pygame.K_RETURN, pygame.K_ESCAPE]:
                        pausando = False

            fundo = pygame.Surface((largura, altura))
            fundo.set_alpha(60)  # Transparência do fundo
            fundo.fill((0, 0, 0))  # Fundo preto transparente
            tela.blit(fundo, (0, 0))

            # Mensagem de pausa
            texto1 = fonte_titulo.render("JOGO PAUSADO", True, (255, 255, 255))
            texto2 = fonte_subtitulo.render("Pressione ENTER para continuar ou ESC para sair", True, (255, 255, 255))

            tela.blit(texto1, ((largura - texto1.get_width()) // 2, altura // 2 - 40))
            tela.blit(texto2, ((largura - texto2.get_width()) // 2, altura // 2 + 30))

            pygame.display.update()
            pygame.time.delay(100)

    def mostrarMensagem(self, tela, largura, altura):
        fundo = pygame.Surface((largura, altura))
        fundo.set_alpha(180)  # Transparência do fundo
        fundo.fill((0, 0, 0))  # Fundo preto transparente
        tela.blit(fundo, (0, 0))

        fonte_titulo = pygame.font.SysFont("Arial", 60, bold=True)
        fonte_subtitulo = pygame.font.SysFont("Arial", 30)

        if(self.singlePlayer):
            if(self.player.getEstaVivo()):
                texto1 = fonte_titulo.render("VOCÊ GANHOU!", True, (255, 215, 0))  # Ouro
                texto2 = fonte_subtitulo.render("Pressione ENTER para ir para a próxima fase", True, (255, 255, 255))
            else: 
                texto1 = fonte_titulo.render("VOCÊ PERDEU!", True, (255, 215, 0))  # Ouro
                texto2 = fonte_subtitulo.render("Pressione ENTER para reiniciar a fase", True, (255, 255, 255))
        else:
            if(self.player.getEstaVivo()):
                texto1 = fonte_titulo.render("PLAYER1 GANHOU!", True, (255, 215, 0))  # Ouro
                texto2 = fonte_subtitulo.render("Pressione ESC para voltar ao menu", True, (255, 255, 255))
            if(self.player2.getEstaVivo()):
                texto1 = fonte_titulo.render("PLAYER2 GANHOU!", True, (255, 215, 0))  # Ouro
                texto2 = fonte_subtitulo.render("Pressione ESC para voltar ao menu", True, (255, 255, 255))

        tela.blit(texto1, ((largura - texto1.get_width()) // 2, altura // 3))
        tela.blit(texto2, ((largura - texto2.get_width()) // 2, altura // 3 + 80))

        pygame.display.update()

    def getMapa(self):
        return self.mapa
    
    def setFase(self, fase):
        self.fase = fase
    
    def getTipoJogo(self):
        return self.singlePlayer   #true -> single ; false -> multiplayer 

