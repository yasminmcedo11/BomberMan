from PPlay.sprite import*
import time

class Bomba:
    def __init__(self, linha, coluna, tileSize, janela, tempo_antes_explodir=2, tempo_duracao_explosao=1):
        self.janela = janela  
        self.linha = linha
        self.coluna = coluna
        self.tileSize = tileSize

        self.explodiu = False
        self.tempo_criacao = time.time()
        self.tempo_antes_explodir = tempo_antes_explodir
        self.finalizada = False

        self.bomba = self.janela.carregar_sprite_escalado(
            "assets/bomb3.png", 32, 32, frames=1
        )
        self.bomba.set_position(coluna * tileSize, linha * tileSize)

        self.explosao = [
            self.janela.carregar_sprite_escalado(f"assets/explosion{i}.png", 128, 128, frames=1)
            for i in range(1, 7)
        ]

        self.tempo_duracao_explosao = tempo_duracao_explosao
        self.tempo_inicio_explosao = None

        self.frameAtual = 0
        self.tiles_explosao = []

    def propagar_explosao(self, mapa):
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        alcance = 1 #alcance de 1 tile em cada direcao (em formato de cruz)
        explosoes = [(self.linha, self.coluna)]

        for dx, dy in direcoes:
            for i in range(1, alcance + 1):
                nl = self.linha + dy * i
                nc = self.coluna + dx * i

                if 0 <= nl < len(mapa) and 0 <= nc < len(mapa[0]):
                    tile = mapa[nl][nc]
                    if tile == "B":
                        mapa[nl][nc] = "I"  # destrói bloco
                        explosoes.append((nl, nc))
                        break
                    elif tile in "WXYZ":
                        break
                    else:
                        explosoes.append((nl, nc))

        self.tiles_explosao = explosoes

    def update(self):
        if not self.explodiu:
            if time.time() - self.tempo_criacao >= self.tempo_antes_explodir:
                self.explodiu = True
                self.propagar_explosao(self.janela.getMapa())
                self.tempo_inicio_explosao = time.time()
                self.frame_atual = 0
                self.finalizada = False
        else:
            tempo_decorrido = time.time() - self.tempo_inicio_explosao
            duracao_por_frame = self.tempo_duracao_explosao / len(self.explosao)

            self.frame_atual = int(tempo_decorrido / duracao_por_frame)
            if self.frame_atual >= len(self.explosao):
                self.finalizada = True
            else:
                self.frame_atual = min(self.frame_atual, len(self.explosao) - 1)

    def draw(self):
        if not self.explodiu:
            self.bomba.draw()
        else:
            if self.frame_atual < len(self.explosao):
                frame = self.explosao[self.frame_atual]
                frame.set_position(
                    self.coluna * self.tileSize - (frame.width // 2 - self.tileSize // 2),
                    self.linha * self.tileSize - (frame.height // 2 - self.tileSize // 2)
                )
                frame.draw()
        
    def terminou(self):
        return self.explodiu and self.finalizada
    
    