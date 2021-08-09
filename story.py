import pygame
from Actor import Actor


class Battle:
    def __init__(self, attacking: Actor, defending: Actor) -> None:
        self.Attacker = attacking
        self.Defender = defending
