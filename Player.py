from PPlay.sprite import *
from Bomba import Bomba
from Personagem import Personagem
import time

class Player(Personagem):
    def __init__(self, janela, tile_size=46):
        super().__init__(janela, "assets/walking pose 1.png", 1, 1, tile_size)

        self.bombas = []
        self.tempo_ultima_bomba = 0
        self.cooldown_bomba = 2
        

    def mover(self, direcao, mapa):
        if self.esta_se_movendo():
            return  

        nova_linha = self.linha
        nova_coluna = self.coluna

        if direcao == "cima":
            nova_linha -= 1
        elif direcao == "baixo":
            nova_linha += 1
        elif direcao == "esquerda":
            nova_coluna -= 1
        elif direcao == "direita":
            nova_coluna += 1

        if 0 <= nova_linha < len(mapa) and 0 <= nova_coluna < len(mapa[0]):
            if mapa[nova_linha][nova_coluna] in "GHIJ":  
                if nova_linha != self.linha or nova_coluna != self.coluna:
                    self.alvo_linha = nova_linha
                    self.alvo_coluna = nova_coluna
    
    def plantar_bomba(self):
        tempo_atual = time.time()
        
        if tempo_atual - self.tempo_ultima_bomba < self.cooldown_bomba:
            return  
        for bomba in self.bombas:
            if bomba.linha == self.linha and bomba.coluna == self.coluna:
                return

        nova_bomba = Bomba(self.linha, self.coluna, self.tileSize, self.janela)
        self.bombas.append(nova_bomba)
        self.tempo_ultima_bomba = tempo_atual
    
    def getBombas(self):
        return self.bombas
    
    def draw(self):
        for bomba in self.bombas:
            bomba.draw()
        super().draw()

    def update(self, delta_time):
        super().update(delta_time)
        for bomba in self.bombas:
            bomba.update()
        self.bombas = [b for b in self.bombas if not b.terminou()]


    
    