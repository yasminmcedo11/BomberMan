from PPlay.sprite import*
import time

class Bomba:
    def __init__(self, linha, coluna, tileSize, tempo_antes_explodir=2):
        self.linha = linha
        self.coluna = coluna
        self.tileSize = tileSize

        self.explodiu = False
        self.tempo_criacao = time.time()
        self.tempo_antes_explodir = tempo_antes_explodir

        self.bomba = Sprite("assets/bomb3.png")
        self.bomba.set_position(coluna * tileSize, linha * tileSize)

        # Animação da explosão
        self.explosao = [
            Sprite(f"assets/explosion{i}.png") for i in range(1, 7)
        ]
        for spr in self.explosao:
            spr.set_position(coluna * tileSize, linha * tileSize)
            spr.set_total_duration(300)  # ajustável
        self.frameAtual = 0

    def update(self):
        if not self.explodiu:
            if time.time() - self.tempo_criacao >= self.tempo_antes_explodir:
                self.explodiu = True
        else:
            if self.frameAtual < len(self.explosao):
                self.explosao[self.frameAtual].update()
                explosao = self.explosao[self.frameAtual]

                if explosao.get_curr_frame() == explosao.get_final_frame():
                    self.finalizada = True

    def draw(self):
        if not self.explodiu:
            self.bomba.draw()
        elif self.frameAtual < len(self.explosao):
            self.explosao[self.frameAtual].draw()
        
    def terminou(self):
        return self.explodiu and self.frameAtual >= len(self.explosao)
    
    