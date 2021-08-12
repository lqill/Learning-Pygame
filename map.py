import pygame
import pygame.freetype
import pygame.transform
import pygame.sprite
import pygame.image
import pygame.time
import pygame.event
import pygame.display
# import pygame_gui
from background import Background
from constant import *
from player import Player
from cursor import Cursor
from tilemap import Tilemap
from actor import Actor


class Map:
    def __init__(self, maps: list) -> None:
        pygame.init()
        self.SIZE = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        # self.FONT = pygame.freetype.Font(FONT, FONTSIZE)
        pygame.display.set_caption('Tile Map')
        self.window_surface = pygame.display.set_mode(self.SIZE)
        # self.ui_manager = pygame_gui.UIManager(self.SIZE)
        self.clock = pygame.time.Clock()
        self.is_active = True
        # TODO: MAKE GRID OBJECT, MAE IT SO EVERYTHING WORKS WITH GRID
        # TODO: MAKE CAMERA, OR FOLLOW CURSOR
        self.maps = Tilemap(maps)
        self.background = Background(self.SIZE)
        self.cursor = Cursor()
        # self.player = Player("thief")
        self.player = Actor("Sandy", "thief", 5)
        self.player.move(self.cursor.pos)

    def run(self):
        while self.is_active:
            self.check_event()
            self.background.render(self.window_surface)
            self.cursor.offset([self.maps, self.player])
            # time_delta = self.clock.tick(FPS)/1000.0
            # self.ui_manager.update(time_delta)
            # Render Window
            self.maps.render(self.window_surface)  # tilemap
            self.cursor.render(self.window_surface)
            self.player.render(self.window_surface)
            # self.ui_manager.draw_ui(self.window_surface)
            pygame.display.update()
            print(self.cursor.pos)
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
                elif event.key == pygame.K_c:
                    self.player.switch_animation("attack")
                elif event.key == pygame.K_x:
                    self.player.status()


if __name__ == "__main__":
    map = [[s, s, a, s, s, s, a, a, s, s, a],
           [s, s, s, d, d, s, d, a, s, s, s],
           [s, s, s, d, d, s, d, d, s, s, d],
           [a, s, s, s, s, s, s, s, s, s, d],
           [a, a, a, a, d, d, d, s, s, s, a]
           ]
    app = Map(map)
    app.run()
