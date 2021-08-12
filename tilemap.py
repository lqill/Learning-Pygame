import pygame
import pygame.display
import pygame.sprite
import pygame.transform
import pygame.image
from constant import *
import random as r


class Tilemap(pygame.sprite.Sprite):
    def __init__(self, tiles: list) -> None:
        super().__init__()
        self.random = r.Random(1)
        # satu tile ukurannya 128*50
        self.tile_map = tiles
        self.texture = TEXTURES
        self.rect = pygame.Rect(
            0, 0, int(len(self.tile_map)*64), int(len(self.tile_map[0]*25)))
        self.tile_images = [
            [self.load_image(i) for i in ii] for ii in self.tile_map]

    def render(self, window_surface: pygame.Surface):
        x = 0
        xor = 0
        y = 0
        yor = 0
        for tilex in self.tile_images:
            for tiley in tilex:
                window_surface.blit(
                    tiley, ((x*right)+(self.rect.left), (y*down)+(self.rect.top)))
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

    def load_image(self, tipe: str):
        acak = None
        if tipe == g:
            acak = self.random.randint(0, 9)
        elif tipe == d:
            acak = self.random.randint(0, 3)
        elif tipe == s:
            acak = self.random.randint(0, 3)
        elif tipe == a:
            pass
        else:
            raise TypeError("Tipe yang masuk bukan d,g,s")
        # TODO:tambah parameter yang berhubungan samo collision
        image = pygame.image.load(self.texture.get(tipe).format(acak))
        size = image.get_rect()[2:]
        size = (size[0], int(size[1]/2))
        image = pygame.transform.scale(image, size)
        # self.pos = (0, 0)
        return image
