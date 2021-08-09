import pygame
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import *


class Cursor(pygame.sprite.Sprite):
    def __init__(self) -> None:
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
        self.update()
        self.pos = self.image.get_rect()
        # TODO: Jadikan self.pos cursor berdasarkan matrix map
        # TODO: buat jarak move, pathfinding
        self.pos = self.pos.move(5*right, 5*down)

    def update(self):
        self.n += 1
        if self.n >= len(self.images):
            self.n = 0
        self.image = self.images[self.n].next()

    def move(self, dirX: int, dirY: int):
        self.pos = self.pos.move(dirX, dirY)
