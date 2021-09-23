import pygame
import pygame.font
import pygame.mixer
import pygame.draw
import pygame.transform
import pygame.sprite
import pygame.image
import pygame.time
import pygame.event
import pygame.display
from background import Background
from constant import FONT, FSIZE_L, FSIZE_M, FSIZE_S, WIDTH, HEIGHT, up, down, left, right, g, d, a, s, FPS
from cursor import Cursor
from tilemap import Tilemap
from actor import Actor


class Map:
    def __init__(self, maps: list) -> None:

        # [Init]
        pygame.init()
        self.SIZE = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.window_surface = pygame.display.set_mode(self.SIZE)
        self.fontS = pygame.font.SysFont(FONT, FSIZE_S)
        self.fontM = pygame.font.SysFont(FONT, FSIZE_M)
        self.fontL = pygame.font.SysFont(FONT, FSIZE_L)
        pygame.display.set_caption('Isometric')
        self.clock = pygame.time.Clock()
        self.running = True

        # [Music]
        pygame.mixer.init()
        channel1 = pygame.mixer.Channel(0)
        ost = pygame.mixer.Sound("Assets/ting.wav")
        # channel1.play(ost, -1)

        # [User Interface]
        # self.ui_manager = pygame_gui.UIManager(self.SIZE)

        # [Object Init]
        self.maps = Tilemap(maps)
        self.background = Background(self.SIZE, "Assets/handpainted_07.png")
        self.cursor = Cursor(tile_map=self.maps.tile_map)
        self.player = Actor("Sandy", "thief", 5)
        self.player.move(self.cursor.pos)

    def run(self):
        self.ticks = 0
        while self.running:

            self.game_input()

            self.cursor.offset([self.maps, self.player])

            # [Render Window]
            self.background.render(self.window_surface)
            self.maps.render(self.window_surface)  # tilemap
            self.cursor.render(self.window_surface)
            self.player.render(self.window_surface)

            # [UI]
            label = self.fontM.render(
                "TIME : "+str(self.time()), 1, (255, 255, 255), 1)
            self.window_surface.blit(label, (20, 20))

            pygame.display.update()

            self.clock.tick(FPS)
            self.ticks += 1

    def time(self):
        self.detik = int(self.ticks/FPS)
        return self.detik

    def game_input(self):
        for event in pygame.event.get():

            # [Quit/Exit]
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # [Movement]
                if event.key == pygame.K_LEFT:
                    self.cursor.move(left, up)
                elif event.key == pygame.K_UP:
                    self.cursor.move(right, up)
                elif event.key == pygame.K_DOWN:
                    self.cursor.move(left, down)
                elif event.key == pygame.K_RIGHT:
                    self.cursor.move(right, down)
                # [Control]
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
