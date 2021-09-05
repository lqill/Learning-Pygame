FONT = "Assets/joystix monospace.ttf"
FSIZE_S=16
FSIZE_M=32
FSIZE_L=64
SIZE = WIDTH, HEIGHT = 800, 600

offset = (0, 0)


# direction  beacause the tiles is 128x50
left = -63
right = 63
# direction Y
up = -25
down = 25

# FPS setiap 10 frame satu detik
FPS = 10
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
