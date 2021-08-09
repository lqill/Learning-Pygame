import pygame
import pygame.freetype
import pygame.font

FONT, FONTSIZE = "Assets/UniversCondensed.ttf", 65
SIZE = WIDTH, HEIGHT = 1000, 750


# direction  beacause the tiles is 128x50
left = -63
right = 63
# direction Y
up = -25
down = 25

# FPS
FPS = 60
frames = int(FPS / 4)

# Assets
# tiles
g = grass = 0
d = dirt = 1
s = stone = 2
a = air = 3
c = cursor = 101
TEXTURES = {
    grass: "Assets/isometric-nature-pack/grass{}.png",
    dirt: "Assets/isometric-nature-pack/dirt{}.png",
    stone: "Assets/isometric-nature-pack/stone{}.png",
    air: "Assets/isometric-nature-pack/air.png",
    cursor: "Assets/isometric-nature-pack/cursor{}.png"
}

# job
mage = 1
healer = 2
thief = 3
warrior = 4
skeleton = 5
goblin = 6
slime = 7
