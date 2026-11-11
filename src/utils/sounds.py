import sys

import pygame

from .resources import resource_path


class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"

        self.die = pygame.mixer.Sound(
            resource_path(f"assets/audio/die.{ext}")
        )
        self.hit = pygame.mixer.Sound(
            resource_path(f"assets/audio/hit.{ext}")
        )
        self.point = pygame.mixer.Sound(
            resource_path(f"assets/audio/point.{ext}")
        )
        self.swoosh = pygame.mixer.Sound(
            resource_path(f"assets/audio/swoosh.{ext}")
        )
        self.wing = pygame.mixer.Sound(
            resource_path(f"assets/audio/wing.{ext}")
        )
