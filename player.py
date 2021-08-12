import pygame
import pygame.sprite
from spritesheet import SpriteStripAnim as ssAnim
from constant import frames

# joblist
joblist = {
    "mage": 1,
    "healer": 2,
    "thief": 3,
    "warrior": 4,
    "skeleton": 5,
    "goblin": 6,
    "slime": 7
}


class Player(pygame.sprite.Sprite):
    def __init__(self, job: str) -> None:
        super().__init__()
        self.job = job
        self.state = "idle"
        self.switch_animation(self.state)
        self.n = 0
        self.images[self.n].iter()
        self.render()
        self.rect = self.image.get_rect()

    def render(self, window_surface: pygame.Surface = None):
        self.n += 1
        if self.n >= len(self.images):
            self.n = 0
            if self.state != "idle":
                self.switch_animation("idle")
        self.image = self.images[self.n].next()
        self.size = self.image.get_rect()[2:]
        self.size = (self.size[0]*6, self.size[1]*6)
        self.image = pygame.transform.scale(self.image, self.size)
        if window_surface != None:
            window_surface.blit(self.image, (self.rect.left, self.rect.top))

    def move(self, cursor: tuple):
        # 20 untuk nyamoi pixel sprite samo cursor, 64 kareno chara ukurannyo 48x16
        self.rect.left = cursor[0]-80
        self.rect.top = cursor[1]-64

    def switch_animation(self, mode: str):
        # Ada mode idle,attack,run,jump,climb
        self.n = 0
        self.state = mode
        file = f"Assets/Heroes_and_Enemies/heroes_and_enemies_{mode}.png"
        self.images = [ssAnim(file, (i, 16*joblist.get(self.job), 48, 16), 1, 0, True, frames)
                       for i in range(0, 145, 48)]

    '''
    kalok nak single image pakek ini
    heroes = ss("Assets/Heroes_and_Enemies/heroes_and_enemies_idle.png")
    self.image = heroes.image_at(
        (16, 18, 16, 16), colorkey=(0, 0, 0))
    self.size = self.image.get_rect()[2:]
    self.size = (self.size[0]*4, self.size[1]*4)
    self.image = pygame.transform.scale(self.image, self.size)
    self.pos = self.image.get_rect().move(5*right, 5*down)
    '''
