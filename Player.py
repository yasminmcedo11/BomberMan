from PPlay.sprite import *
from Bomba import Bomba
import time

class Player:
    def __init__(self, janela, tile_size=46):
        self.tileSize = tile_size
        self.janela = janela
        self.velocidade = 250

        # Posição lógica/alvo no grid
        self.linha = 1
        self.coluna = 1
        self.alvo_linha = 1
        self.alvo_coluna = 1

        self.player = self.janela.carregar_sprite_escalado("assets/walking pose 1.png", 32, 48, frames=4)
        self.player.set_position(1 * self.tileSize, 1 * self.tileSize)  # Posição no grid
        self.player.set_total_duration(800)

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
    
    def esta_se_movendo(self):
        destino_x = self.alvo_coluna * self.tileSize
        destino_y = self.alvo_linha * self.tileSize
        return self.player.x != destino_x or self.player.y != destino_y
    
    def atualizarPosicao(self, delta_time):
        destino_x = self.alvo_coluna * self.tileSize
        destino_y = self.alvo_linha * self.tileSize

        dx = destino_x - self.player.x
        dy = destino_y - self.player.y
        distancia = (dx**2 + dy**2) ** 0.5

        if distancia < 1:
            self.player.x = destino_x
            self.player.y = destino_y
            self.linha = self.alvo_linha
            self.coluna = self.alvo_coluna
            return

        dir_x = dx / distancia
        dir_y = dy / distancia

        mover_x = dir_x * self.velocidade * delta_time
        mover_y = dir_y * self.velocidade * delta_time

        # Corrigir se for ultrapassar
        if abs(mover_x) > abs(dx): mover_x = dx
        if abs(mover_y) > abs(dy): mover_y = dy

        self.player.x += mover_x
        self.player.y += mover_y
        self.player.set_position(self.player.x, self.player.y)
    
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
    
    def draw(self):
        for bomba in self.bombas:
            bomba.draw()
        self.player.draw()

    def update(self, delta_time):
        self.atualizarPosicao(delta_time)
        self.player.update()
        for bomba in self.bombas:
            bomba.update()
        self.bombas = [b for b in self.bombas if not b.terminou()]


    
    