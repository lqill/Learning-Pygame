import pygame
from pygame.constants import K_p
import pygame.font
import pygame.draw
import pygame.transform
import pygame.sprite
import pygame.image
import pygame.time
import pygame.event
import pygame.display
# import pygame_gui
from background import Background
from constant import FONT, FSIZE_L, FSIZE_M, FSIZE_S, WIDTH, HEIGHT, up, down, left, right, g, d, a, s, FPS
from cursor import Cursor
from tilemap import Tilemap
from actor import Actor


class Map:
    def __init__(self, maps: list) -> None:
        pygame.init()
        self.SIZE = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.fontS = pygame.font.SysFont(FONT, FSIZE_S)
        self.fontM = pygame.font.SysFont(FONT, FSIZE_M)
        self.fontL = pygame.font.SysFont(FONT, FSIZE_L)
        pygame.display.set_caption('Isometric')
        self.window_surface = pygame.display.set_mode(self.SIZE)
        # self.ui_manager = pygame_gui.UIManager(self.SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        # TODO: MAKE GRID OBJECT, MAKE IT SO EVERYTHING WORKS WITH GRID
        self.maps = Tilemap(maps)
        self.background = Background(self.SIZE, "Assets/handpainted_07.png")
        self.cursor = Cursor(tile_map=self.maps.tile_map)
        # self.player = Player("thief")
        self.player = Actor("Sandy", "thief", 5)
        self.player.move(self.cursor.pos)

    def run(self):
        self.detik = 0
        angka = 0
        while self.running:
            self.check_event()
            self.background.render(self.window_surface)
            self.cursor.offset([self.maps, self.player])
            # time_delta = self.clock.tick(FPS)/1000.0
            # self.ui_manager.update(time_delta)
            # Render Window
            self.maps.render(self.window_surface)  # tilemap
            self.cursor.render(self.window_surface)
            self.player.render(self.window_surface)
            label = self.fontM.render(
                "TIME : "+str(self.detik), 1, (255, 255, 255), 1)
            self.window_surface.blit(label, (20, 20))
            # self.ui_manager.draw_ui(self.window_surface)
            pygame.display.update()
            self.clock.tick(FPS)
            angka += 1
            self.detik = int(angka / 10)

    def check_event(self):
        # event
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                self.running = False
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
                elif event.key == pygame.K_p:
                    pause = True
                    pygame.draw.rect(self.window_surface,
                                     0, pygame.Rect(0, 0, self.WIDTH, self.HEIGHT))
                    teks = self.fontL.render("PAUSE", 1, (255, 255, 255))
                    self.window_surface.blit(
                        teks, (self.HEIGHT/2+20, self.WIDTH/2-120))
                    pygame.display.update()
                    while pause:
                        for event2 in pygame.event.get():
                            # QUIT
                            if event2.type == pygame.QUIT:
                                pause = False
                                self.running = False
                            elif event2.type == pygame.KEYDOWN and event2.key == pygame.K_p:
                                pause = False


if __name__ == "__main__":
    map = [[s, s, a, s, s, s, a, a, s, s, a],
           [s, s, s, d, d, s, d, a, s, s, s],
           [s, s, s, d, d, s, d, d, s, s, d],
           [a, s, s, s, s, s, s, s, s, s, d],
           [a, a, a, a, d, d, d, s, s, s, a]
           ]
    app = Map(map)
    app.run()
