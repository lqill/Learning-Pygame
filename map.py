from background import Background
import pygame
import pygame.transform
import pygame.sprite
import pygame.image
import pygame.time
import pygame.event
import pygame.display
import pygame_gui
from constant import *
from player import Player
from cursor import Cursor
from tilemap import Tile


class Map:
    def __init__(self) -> None:
        pygame.init()
        self.SIZE = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.FONT = pygame.freetype.Font(FONT, FONTSIZE)
        pygame.display.set_caption('Tile Map')
        self.window_surface = pygame.display.set_mode(self.SIZE)
        self.ui_manager = pygame_gui.UIManager(self.SIZE)
        self.clock = pygame.time.Clock()
        self.is_active = True
        self.map = [[s, s, a, g, s, s, a, a, s, s, a],
                    [g, s, s, d, d, s, d, a, a, s, s],
                    [s, s, s, d, d, s, d, d, d, d, d],
                    [a, d, s, s, s, s, s, s, s, s, d],
                    [a, a, a, a, d, d, d, a, a, d, a]
                    ]
        self.maps = [[Tile(TEXTURES.get(i), i)for i in ii]
                     for ii in self.map]
        self.background = Background(self.SIZE)
        self.cursor = Cursor()
        self.player = Player()
        self.player.move(self.cursor.pos)

    def run(self):
        while self.is_active:
            self.window_surface.blit(self.background.render(), (0, 0))
            self.check_event()
            time_delta = self.clock.tick(10)/1000.0
            # Render Window
            self.ui_manager.update(time_delta)
            self.render_tiles()
            self.window_surface.blit(self.cursor.image, self.cursor.pos)
            self.window_surface.blit(self.player.image, self.player.pos)
            self.cursor.update()
            self.player.update()
            self.ui_manager.draw_ui(self.window_surface)
            pygame.display.update()
            self.clock.tick(FPS)

    def check_event(self):
        # event
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                self.is_active = False
            # Control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.cursor.move(left, up)
                elif event.key == pygame.K_UP:
                    self.cursor.move(right, up)
                elif event.key == pygame.K_DOWN:
                    self.cursor.move(left, down)
                elif event.key == pygame.K_RIGHT:
                    self.cursor.move(right, down)
                elif event.key == pygame.K_SPACE:
                    self.player.move(self.cursor.pos)

    def render_tiles(self):
        x = 0
        xor = 0
        y = 0
        yor = 0
        for tilex in self.maps:
            for tiley in tilex:
                self.window_surface.blit(
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


if __name__ == "__main__":
    app = Map()
    app.run()
