import pygame
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import HEIGHT


class Background(pygame.Surface):
    def __init__(self, size: tuple, image: str):
        self.background = pygame.Surface(size)
        # self.background.fill(pygame.Color("#f0f0f0"))
        self.bg_image = pygame.image.load(image)
        self.bg_pos = self.bg_image.get_rect()
        self.background.blit(self.bg_image, self.bg_pos)
        self.bg_turn = True

    def render(self, window_surface: pygame.Surface):
        if self.bg_turn:
            self.bg_pos = self.bg_pos.move(-1, -1)
            if self.bg_pos.bottom < HEIGHT:
                self.bg_turn = False
        else:
            self.bg_pos = self.bg_pos.move(1, 1)
            if self.bg_pos.left > 0:
                self.bg_turn = True
        self.background.blit(self.bg_image, self.bg_pos)
        window_surface.blit(self.background, (0, 0))
