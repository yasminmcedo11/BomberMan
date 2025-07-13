from PIL import Image
import os

# Caminhos
sprite_sheet_path = "assets/bomberman sprite.png"
output_dir = "recortes"
tile_size = 16  # tamanho dos sprites (largura e altura)

# Criar pasta de saída
os.makedirs(output_dir, exist_ok=True)

# Abrir imagem
sheet = Image.open(sprite_sheet_path)
sheet_width, sheet_height = sheet.size

# Cortar imagem em tiles 16x16
count = 0
for y in range(0, sheet_height, tile_size):
    for x in range(0, sheet_width, tile_size):
        box = (x, y, x + tile_size, y + tile_size)
        tile = sheet.crop(box)
        tile.save(os.path.join(output_dir, f"tile_{count:02}.png"))
        count += 1

print(f"{count} sprites salvos em '{output_dir}'")