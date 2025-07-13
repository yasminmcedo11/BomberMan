from PIL import Image
import os

# Lista com os nomes das imagens (ordem da animação)
imagens = [
    "assets/explosion1.png",
    "assets/explosion2.png",
    "assets/explosion3.png",
    "assets/explosion4.png",
    "assets/explosion5.png"
]

# Abrir todas as imagens
frames = [Image.open(img).convert("RGBA") for img in imagens]

# Pegar largura e altura de uma imagem (assumindo que todas têm o mesmo tamanho)
largura, altura = frames[0].size
total_largura = largura * len(frames)

# Criar imagem nova (spritesheet) com largura total e altura única
spritesheet = Image.new("RGBA", (total_largura, altura))

# Colar cada imagem na posição correta
for i, frame in enumerate(frames):
    spritesheet.paste(frame, (i * largura, 0))

# Salvar resultado
spritesheet.save("assets/explosao_spritesheet.png")
print("Spritesheet salvo como 'assets/explosao_spritesheet.png'")