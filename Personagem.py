from PPlay.sprite import *

class Personagem:
    def __init__(self, janela, sprite_path, linha, coluna, tile_size=46, velocidade=250):
        self.janela = janela
        self.tileSize = tile_size
        self.velocidade = velocidade

        self.linha = linha
        self.coluna = coluna
        self.alvo_linha = linha
        self.alvo_coluna = coluna

        self.sprite = self.janela.carregar_sprite_escalado(sprite_path, 32, 48, frames=4)
        self.sprite.set_position(coluna * self.tileSize, linha * self.tileSize)
        self.sprite.set_total_duration(800)
        self.vivo = True

    def esta_se_movendo(self):
        destino_x = self.alvo_coluna * self.tileSize
        destino_y = self.alvo_linha * self.tileSize
        return self.sprite.x != destino_x or self.sprite.y != destino_y

    def atualizar_posicao(self, delta_time):
        destino_x = self.alvo_coluna * self.tileSize
        destino_y = self.alvo_linha * self.tileSize

        dx = destino_x - self.sprite.x
        dy = destino_y - self.sprite.y
        distancia = (dx**2 + dy**2) ** 0.5

        if distancia < 1:
            self.sprite.x = destino_x
            self.sprite.y = destino_y
            self.linha = self.alvo_linha
            self.coluna = self.alvo_coluna
            return

        dir_x = dx / distancia
        dir_y = dy / distancia
        mover_x = dir_x * self.velocidade * delta_time
        mover_y = dir_y * self.velocidade * delta_time

        if abs(mover_x) > abs(dx): mover_x = dx
        if abs(mover_y) > abs(dy): mover_y = dy

        self.sprite.x += mover_x
        self.sprite.y += mover_y
        self.sprite.set_position(self.sprite.x, self.sprite.y)
    
    def verificarColisaoBombas(self, bombas):
        if not self.vivo:
            return

        for bomba in bombas:
            if bomba.explodiu and not bomba.finalizada:
                if (self.linha, self.coluna) in bomba.tiles_explosao:
                    self.morrer()
                    break

    def morrer(self):
        self.vivo = False
    
    def getEstaVivo(self):
        return self.vivo

    def draw(self):
        if not self.vivo:
            return
        self.sprite.draw()

    def update(self, delta_time):
        if not self.vivo:
            return
        self.atualizar_posicao(delta_time)
        self.sprite.update()