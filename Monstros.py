from Personagem import Personagem
import random

class Monstro(Personagem):
    def __init__(self, janela, linha, coluna, tile_size=46):
        cores = ["blue", "green", "red", "pink"]
        cor_escolhida = random.choice(cores)
        caminho_sprite = f"assets/{cor_escolhida}1.png"
        super().__init__(janela, caminho_sprite, linha, coluna, tile_size)
        self.direcoes = ["cima", "baixo", "esquerda", "direita"]
        self.tempo_mudar_direcao = 1
        self.tempo_restante = self.tempo_mudar_direcao

    def mover(self, mapa):
        if self.esta_se_movendo():
            return

        direcao = random.choice(self.direcoes)

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
                self.alvo_linha = nova_linha
                self.alvo_coluna = nova_coluna

    def update(self, delta_time, mapa):
        self.tempo_restante -= delta_time
        if self.tempo_restante <= 0:
            self.mover(mapa)
            self.tempo_restante = self.tempo_mudar_direcao
        super().update(delta_time)
