import pygame
import pygame.display
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import *
import random


class Tile(pygame.sprite.Sprite):
    def __init__(self, tiles: str, tipe: int) -> None:
        super().__init__()
        acak = None
        if tipe == g:
            acak = random.randint(0, 9)
        elif tipe == d:
            acak = random.randint(0, 3)
        elif tipe == s:
            acak = random.randint(0, 3)
        elif tipe == a:
            pass
        else:
            raise TypeError("Tipe yang masuk bukan d,g,s")
        # TODO:tambah parameter yang berhubungan samo collision
        self.tipe = tipe
        self.image = pygame.image.load(tiles.format(acak))
        self.size = self.image.get_rect()[2:]
        self.size = (self.size[0], int(self.size[1]/2))
        self.image = pygame.transform.scale(self.image, self.size)
        self.pos = (0, 0)

    def render(self, window_surface: pygame.display, maps: list):
        def render_tiles(self):
            x = 0
            xor = 0
            y = 0
            yor = 0
            for tilex in maps:
                for tiley in tilex:
                    window_surface.blit(
                        tiley.image, ((x*right)+(4*right), (y*down)+(4*down)))
                    # x += 127
                    x += 1
                    y += 1
                # restart th x grid from the left of the former row
                xor += 1
                x = -xor
                # restart the y grid from below the former first grid
                y = yor
                yor += 1
                y += 1
