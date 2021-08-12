import pygame
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import *


class Cursor(pygame.sprite.Sprite):
    def __init__(self, mode: str = None, size: tuple = None) -> None:
        super().__init__()
        file = TEXTURES[cursor]
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
        self.pos = self.rect.move(5*right, 5*down)

    def render(self, window_surface: pygame.Surface):
        self.n += 1
        if self.n >= len(self.images):
            self.n = 0
        self.image = self.images[self.n].next()
        window_surface.blit(self.image, self.pos)

    def move(self, dirX: int, dirY: int):
        self.pos = self.pos.move(dirX, dirY)

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
