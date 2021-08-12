import pygame
import pygame.sprite
from constant import *


class Camera:
    def __init__(self) -> None:
        pygame.init()
        self.SIZE = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.window_surface = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.is_active = True
