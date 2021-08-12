from game import Map
from background import Background
import pygame
import pygame.sprite
import pygame.display
import pygame.time
import pygame.image
import pygame.event
from spritesheet import SpriteStripAnim as ssAnim

from constant import FPS, SIZE, frames, g, d

pygame.init()
pygame.display.set_caption("Isometric")
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
background = Background(SIZE, "Assets/Handpainted_02.png")
frame = pygame.image.load("Assets/menu/Menu.png")
title = pygame.image.load("Assets/title.png")

menu = {
    "new": [pygame.image.load("Assets/Titlescreen/Command_0.png")]
}
check = pygame.image.load("Assets/Titlescreen/Command_0.png")

while running:
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = Map([[g, g, g, g, g, g, d, d, d], [g, g, g, g, g, d, d, d, d], [
                       g, g, g, g, g, g, d, d, d], [g, g, g, d, d, d, d, d, d], [g, g, g, g, g, d, d, d, d]])
            test.run()
            running = False
    #
    background.render(window)
    window.blit(frame, (-170, 0))
    window.blit(title, (190, 0))
    window.blit(check, (0, 0))

    #
    pygame.display.update()
    clock.tick(FPS)
