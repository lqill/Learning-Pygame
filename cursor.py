import pygame
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import TEXTURES, cursor, frames, right, left, up, down, WIDTH, HEIGHT, a


class Cursor(pygame.sprite.Sprite):
    def __init__(self, mode: str = None, tile_map: list = None) -> None:
        super().__init__()
        file = TEXTURES[cursor]
        self.tile_map = tile_map
        for ix, i in enumerate(self.tile_map):
            for j in i:
                if j != a:
                    self.grid_pos = [ix, j]
                    break
            if j != a:
                break
        self.grid_pos = [0, 0]
        self.images = [
            ssAnim(file.format(1), (0, 0, 128, 50), 1, 0, True, frames),
            ssAnim(file.format(2), (0, 0, 128, 50), 1, 0, True, frames),
            ssAnim(file.format(3), (0, 0, 128, 50), 1, 0, True, frames),
            ssAnim(file.format(4), (0, 0, 128, 50), 1, 0, True, frames)
        ]
        self.n = 0
        self.images[self.n].iter()
        self.image = self.images[self.n].next()
        self.rect = self.image.get_rect()
        # TODO: Jadikan self.pos cursor berdasarkan matrix map
        # TODO: buat jarak move, pathfinding
        self.pos = self.rect.move(
            self.grid_pos[0]*right, self.grid_pos[1]*down)
        print("grid", self.grid_pos)

    def render(self, window_surface: pygame.Surface):
        self.n += 1
        if self.n >= len(self.images):
            self.n = 0
        self.image = self.images[self.n].next()
        window_surface.blit(self.image, self.pos)

    def move(self, dirX: int, dirY: int):
        if (dirX, dirY) == (left, up):
            dx = 0
            dy = -1
        elif (dirX, dirY) == (right, up):
            dx = -1
            dy = 0
        elif (dirX, dirY) == (left, down):
            dx = 1
            dy = 0
        elif (dirX, dirY) == (right, down):
            dx = 0
            dy = 1
        try:
            if self.grid_pos[0]+dx < 0 or self.grid_pos[1]+dy < 0:
                raise IndexError
            if self.tile_map[self.grid_pos[0]+dx][self.grid_pos[1]+dy] == a:
                pass
                print("air", self.grid_pos,
                      self.grid_pos[0]+dy, self.grid_pos[1]+dx)
            else:
                self.pos = self.pos.move(dirX, dirY)
                self.grid_pos[0] += dx
                self.grid_pos[1] += dy
                print(self.grid_pos)

        except IndexError as e:
            print("Error", e, self.grid_pos)

    def offset(self, items: list):
        if self.pos.left < 0+200:
            x, y = right, 0
        elif self.pos.right > WIDTH-200:
            x, y = left, 0
        elif self.pos.top < 0+100:
            x, y = 0, down
        elif self.pos.bottom > HEIGHT-100:
            x, y = 0, up
        else:
            x, y = 0, 0
        for item in items:
            item.rect.move_ip(x, y)
        self.pos.move_ip(x, y)
