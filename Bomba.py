from PPlay.sprite import*
import time

class Bomba:
    def __init__(self, linha, coluna, tileSize, janela, tempo_antes_explodir=2):
        self.janela = janela  
        self.linha = linha
        self.coluna = coluna
        self.tileSize = tileSize

        self.explodiu = False
        self.tempo_criacao = time.time()
        self.tempo_antes_explodir = tempo_antes_explodir
        self.finalizada = False

        # Usa o método da janela para carregar e escalar o sprite da bomba
        self.bomba = self.janela.carregar_sprite_escalado(
            "assets/bomb3.png", 32, 32, frames=1
        )
        self.bomba.set_position(coluna * tileSize, linha * tileSize)

        self.explosao = [
            self.janela.carregar_sprite_escalado(
                f"assets/explosion{i}.png", 32, 32, frames=4
            )
            for i in range(1, 7)
        ]
        for spr in self.explosao:
            spr.set_position(coluna * tileSize, linha * tileSize)
            spr.set_total_duration(300)  

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
    
    